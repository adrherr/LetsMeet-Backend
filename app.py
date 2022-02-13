from flask import Flask, render_template, redirect, request, session
from db import maria
import json

app = Flask(__name__, template_folder='website')
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
            return sql.add_user(info)

        elif post_type == 'event':
            info = request.json
            print(info)
            sql.add_event(info)
            return 'Success'
        
        elif post_type == 'login':
            info = request.json
            print(info)
            userid = sql.login(info)
            print("userid:",userid)
            return str(userid)

    return '😐 OOPS 😐'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    sql.close()