from flask import Flask, render_template, request
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
        value = request.args.get("value")
        get_type = request.args.get("type")

        if get_type == "user" and value == "all":
            users = sql.get_all_users()
            return json.dumps({"users": users})

        elif get_type == "event" and value == "all":
            info = sql.get_all_events()
            return json.dumps({"events": info})

        elif get_type == "userevents" and value:
            info = sql.get_user_events(value)
            return json.dumps({"events": info})

        elif get_type == "conversations" and value:
            info = sql.get_conversations(value)
            return json.dumps({"messages": info})

        elif get_type == "messages" and value:
            info = sql.get_messages(value)
            return json.dumps({"messages": info})

        elif get_type == "profile" and value:
            info = sql.get_profile(value)
            return json.dumps(info)

        elif get_type == "user" and value:
            user = sql.get_user(value)
            return json.dumps(user)

        elif get_type == "event" and value:
            info = sql.get_event(value)
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

        elif post_type == 'profile':
            info = request.json
            print(info)
            sql.save_profile(info['userid'], info['name'], info['bio'], info['tags'])

    return '😐 OOPS 😐'


@socketio.on('send')
def handle_my_custom_event(msg):
    print('RECEIVED:', msg)
    socketio.emit(msg['toUid'] + msg['convoId'], msg)
    sql.add_message(msg['convoId'], msg['message'][0]['text'], msg['message'][0]['createdAt'], msg['fromUid'])

if __name__ == "__main__":
    # app.run(debug=True, host='0.0.0.0', port=5000)
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
    sql.close()