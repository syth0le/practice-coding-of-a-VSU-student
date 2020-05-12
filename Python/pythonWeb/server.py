import datetime
import time
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session

app = Flask(__name__)

messages = {'username': 'Nike', 'text': 'Hello', 'time': 0.0}


@app.route('/')
def hello():
    return "Hello!"


@app.route("/status")
def status():
    return{
        'status': True,
        'name': 'VSU messenger',
        'time': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    }


@app.route("/send", methods=['POST'])
def send():
    username = request.json['username']
    text = request.json['text']
    current_time = time.time()
    message = {'username': username, 'text': text, 'time': current_time}
    messages.append(message)

    print(messages)

    return {"ok": True}


app.run()
