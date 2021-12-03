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
def users():
    if (request.method == 'GET'):
        user = request.args.get("user")
        event = request.args.get("event")

        if user == "all":
            users = sql.get_allusers()
            return json.dumps({"users": users})

        elif user:
            user = sql.get_user(user)
            return json.dumps(user)

        elif event == "all":
            info = sql.get_allevents()
            return json.dumps({"events": info})

        elif event:
            info = sql.get_event(event)
            return json.dumps(info)

    return '😐 OOPS 😐'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
