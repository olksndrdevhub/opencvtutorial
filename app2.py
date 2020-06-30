import cv2

import numpy as np

img = cv2.imread('resources/img1.jpg')
print(img.shape)

imgResize = cv2.resize(img, (450, 300))
print(imgResize.shape)

imgCropd = img[0:200, 200:450]


cv2.imshow('img', img)
cv2.imshow('imgresize', imgResize)
cv2.imshow('imgcropd', imgCropd)


cv2.waitKey(0)