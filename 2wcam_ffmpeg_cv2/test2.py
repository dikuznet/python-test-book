import os
import cv2
cap = cv2.VideoCapture("rtsp://10.0.10.123:554/stream0?username=admin&password=123456")

dirname = 'output'
count = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    else:
        cv2.imshow('frame', frame)
        name = "rec_frame"+str(count)+".jpg"
        cv2.imwrite(os.path.join(dirname,name), frame)
        count += 1
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
