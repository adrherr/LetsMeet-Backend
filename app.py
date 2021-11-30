from flask import Flask, render_template, redirect, request, session
import sys, json

app = Flask(__name__, template_folder='website')

@app.route('/')
@app.route('/index.html', methods = ['POST', 'GET'])
def index():
    if (request.method == 'GET'):
        if request.args.get('id') == "123":
            return json.dumps({'name': 'hi'})
    return render_template('/index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')