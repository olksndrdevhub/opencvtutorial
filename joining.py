import cv2

import numpy as np

img = cv2.imread('resources/img2.jpg')

hor = np.hstack((img, img))
ver = np.vstack((img, img))

cv2.imshow('horisont', hor)
cv2.imshow('vertical', ver)


cv2.waitKey(0)