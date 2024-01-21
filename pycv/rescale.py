import cv2 as cv

def rescaleimg(img,scale=0.2):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(img,dimensions,interpolation=cv.INTER_AREA)


img = cv.imread('pycv/arrow.png')
cv.imshow('arrow',img)
resized_image = rescaleimg(img)
cv.imshow('arrow',resized_image)


cv.waitKey(0)

