import cv2 as cv

img = cv.imread('pycv\cat.jpeg')
cv.imshow('Cat',img)

cv.waitKey(0)