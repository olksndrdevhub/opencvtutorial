import cv2

import numpy as np

img = cv2.imread('resources/img2.jpg')
print(img.shape)
width, height = 250, 350

# cv2.rectangle(img, (254,63), (380,217), (255,0,0), 2)

pts1 = np.float32([[297,69], [383,92], [257,187], [347,218]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

img_output = cv2.warpPerspective(img, matrix, (width, height))


cv2.imshow('image', img)
cv2.imshow('image_out', img_output)
cv2.waitKey(0)