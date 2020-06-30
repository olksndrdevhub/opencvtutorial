import cv2
import numpy as np


img = cv2.imread('resources/img1.jpg')

kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialition = cv2.dilate(imgCanny, kernel, iterations=3)
imgEroded = cv2.erode(imgDialition, kernel, iterations=1)

# cv2.imshow('imgGray', imgGray)
# cv2.imshow('imgBlur', imgBlur)
cv2.imshow('imgCanny', imgCanny)
cv2.imshow('imgDialition', imgDialition)
cv2.imshow('imgEroded', imgEroded)
cv2.waitKey(0)