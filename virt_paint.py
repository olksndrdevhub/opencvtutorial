import cv2

import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 20)




while True:
    success, img = cap.read()
    cv2.imshow('result', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break