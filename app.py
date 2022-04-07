from flask import Flask, render_template, redirect, request, session
from flask_socketio import SocketIO
from db import maria
import json

app = Flask(__name__, template_folder='website')
socketio = SocketIO(app)
sql = maria()


@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')


@app.route('/get', methods=['GET'])
def parse_get_request():
    if (request.method == 'GET'):
        user = request.args.get("user")
        event = request.args.get("event")

        if user == "all":
            users = sql.get_all_users()
            return json.dumps({"users": users})

        elif event == "all":
            info = sql.get_all_events()
            return json.dumps({"events": info})

        elif event == "userevents" and user:
            info = sql.get_user_events(user)
            return json.dumps({"events": info})

        elif event == "conversations" and user:
            info = sql.get_conversations(user)
            return json.dumps({"messages": info})

        elif user:
            user = sql.get_user(user)
            return json.dumps(user)

        elif event:
            info = sql.get_event(event)
            return json.dumps(info)

    return '😐 OOPS 😐'


@app.route('/post', methods=['POST'])
def parse_post_request():
    if (request.method == 'POST'):
        post_type = request.args.get("type")

        if post_type == 'user':
            info = request.json
            print(info)
            userid = sql.add_user(info)
            return str(userid)

        elif post_type == 'event':
            info = request.json
            print(info)
            sql.add_event(info)

        elif post_type == 'participant':
            info = request.json
            print(info)
            sql.add_participant(info['eventid'], info['userid'])
        
        elif post_type == 'login':
            info = request.json
            print(info)
            userid = sql.login(info)
            return str(userid)

        elif post_type == 'removeevent':
            info = request.json
            print(info)
            sql.remove_event(info['eventid'])

        elif post_type == 'leaveevent':
            info = request.json
            print(info)
            sql.leave_event(info['eventid'], info['userid'])

    return '😐 OOPS 😐'


@socketio.on('message')
def handle_my_custom_event(msg):
    print('received my event: ' + msg)
    socketio.send("Hello sir!!!!!!!!!!!!!!")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    sql.close()