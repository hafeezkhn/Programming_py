import cv2 as cv

#reading video
capture = cv.VideoCapture(r'pycv\video.mkv')

while True:
    isTrue,frame = capture.read()
    cv.imshow('Video',frame)


    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()

