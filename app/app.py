from flask import Flask

import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hostname")
def hostname():
    hostname = os.popen("hostname").read()
    return f"<p>{hostname}</p>"

@app.route("/author")
def author():
    author = os.environ.get('AUTHOR', "not exist")
    return f"<p>{author}</p>"

@app.route("/id")
def id():
    uuid = os.environ.get('UUID', "not exist")
    return f"<p>{uuid}</p>"

@app.route("/liveness")
@app.route("/readiness")
def check():
    return "OK"