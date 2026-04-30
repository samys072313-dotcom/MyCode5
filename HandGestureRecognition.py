import cv2
import mediapipe as mp
from mediapipe.python.solutions import hands as mp_hands
from mediapipe.python.solutions import drawing_utils as mp_drawing
wCam,hCam = 720,640
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)
while True:
    success, image = cap.read()

    cv2.imshow("Media Controller", image)

    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()

