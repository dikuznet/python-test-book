#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#Micont smoke app
#Autor: dkuznetsov@micont.ru
#version v1.0 (2017-2018)

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, disconnect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from threading import Lock
import memcache
import sys
import json,jsonify
import time
from random import random
from config import Config


async_mode = None
app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'login'

socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

db = SQLAlchemy(app)
# migrate = Migrate(app, db)


def background_thread():
    count = 0
    while True:
        socketio.sleep(1)
        data = []
        socketio.emit('my_response', {'data': json.dumps(data), 'count': count}, namespace='/test')

@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    print('connect')
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})


@socketio.on('my_ping', namespace='/test')
def ping_pong():
    emit('my_pong')


@socketio.on('resetall', namespace='/test')
def resetall():
    res0, res1, res2, res3 = 0, 0, 0, 0


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)

if __name__ == '__main__':   
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
