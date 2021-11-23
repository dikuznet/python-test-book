from flask import Flask, render_template, Response
from markupsafe import escape
import cv2
import glob
import asyncio

loop = asyncio.get_event_loop()

camera_index  = glob.glob("/dev/video?")

# "rtsp://root:pass@192.168.0.91:554/axis-media/media.amp")

CAM_PATH = "rtsp://admin:123456@10.0.10.123:554/ISAPI/Streaming/Channels/101"
cap = cv2.VideoCapture(CAM_PATH)
app = Flask(__name__)
frame = None


def gen_frames(camid):
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 

# async def getcam():
#     while True: 
#         frame = gen_frames(0)  

@app.route('/video_feed/<int:cam_id>')
def video_feed(cam_id):
    return Response(gen_frames(cam_id), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"