from flask import Flask, render_template, redirect, request, session
from db import maria
import json

app = Flask(__name__, template_folder='website')

@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')

@app.route('/get', methods = ['GET'])
def users():
    if (request.method == 'GET'):
        sql = maria()
        user = request.args.get('user')

        if request.args.get('users') == "all":
            users = sql.get_allusers()
            return json.dumps({"users": users})            

    return '😐 OOPS 😐'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')