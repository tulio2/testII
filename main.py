from flask import Flask
import os

app = Flask(__name__)

@app.route("/test")
def hello_world():
    return os.getcwd()
