from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, disconnect
from threading import Lock
import sys
import time
from random import random
from markupsafe import escape

async_mode = None
app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

def background_thread():
    try:
        while True:
            # socketio.emit('response',{'data': value},namespace='/test')
            # print("F")
            time.sleep(5)
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            sys.exit(1)

@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)
    emit('response', {'data': 'Connected'})

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

if __name__ == '__main__':
    socketio.start_background_task(background_thread)
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
