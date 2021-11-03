import ffmpeg

stream = ffmpeg.input("rtsp://10.0.10.123:554/stream1?username=admin&password=123456", ss=0)
i = 0
while True:
    i = i + 1
    file = stream.output("out/test"+str(i)+".png", vframes=1)
    testfile = file.run()
    if i == 100: break
