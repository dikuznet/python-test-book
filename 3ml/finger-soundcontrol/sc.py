import cv2
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
import math

def get_color(v):
    return {
        0 <= v <= 20:   (255,0,0),
        21 <= v <= 50:  (0,128,0),
        51 <= v <= 80:  (0,0,255),
        81 <= v <= 100: (192,192,192),
    } [True]

FINGER_MAX = 100
FINGER_MIN = 10
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mpDraw = mp.solutions.drawing_utils
device = AudioUtilities.GetSpeakers()

#Получим текущий уровень звука
interace = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interace, POINTER(IAudioEndpointVolume))
volMin, volMax = volume.GetVolumeRange()[:2]

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# print(cv2)
# print(dir(cv2))
# print(cv2.BORDER_WRAP,cv2.BORDER_TRANSPARENT)
vol = 0
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue


    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    lmList = []

    vol = volume.GetMasterVolumeLevel()
    prc = int((100*vol)/volMin)  
    end_point = (5, 5 + prc)
    cl = get_color(prc)

    cv2.rectangle(image, (5, 5), (30, 105), (192,192,192), cv2.BORDER_WRAP)
    cv2.rectangle(image, (30,105), end_point, cl, cv2.FILLED)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        for id,lm in enumerate(hand_landmarks.landmark):
            h,w,_ = image.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append([id,cx,cy])

        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    if lmList != []:
        x1,y1 = lmList[4][1],lmList[4][2]
        x2,y2 = lmList[8][1],lmList[8][2]
        # print(x1-x2,y1-y2)
        cv2.circle(image,(x1,y1),5,(255,0,0),cv2.FILLED)
        cv2.circle(image,(x2,y2),5,(255,0,0),cv2.FILLED)
        cv2.line(image,(x1,y1),(x2,y2),(255,0,0),3)
        l = hypot(x2-x1, y2-y1)
        vol = np.interp(l,[10,100],[volMin,volMax])
        print(vol,l, volMin,volMax)
        volume.SetMasterVolumeLevel(vol, None)

    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == ord('q'):
      break
cap.release()


# while True:
#     success,img = cap.read()
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     result = hands.process(imgRGB)

#     lmList = []

#     if result.multi_hand_landmarks: