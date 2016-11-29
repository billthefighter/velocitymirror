import numpy as np
import cv2

cap = cv2.VideoCapture('movie6.mp4')
ret, frame = cap.read()
frame1 = frame
frame2 = frame
accumulate = frame

while(cap.isOpened()):
    ret, frame = cap.read()
    frame1 = frame
    gray = cv2.subtract(frame2,frame1)
    accumulate += gray
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame2 = frame
    cv2.imshow('frame',accumulate)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()