import numpy as np
import cv2

cap = cv2.VideoCapture('movie6.mp4')
#cap = cv2.VideoCapture('movie2.mov')
ret, frame = cap.read()
frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
frame2 = frame
gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
dst = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


while(cap.isOpened()):
    ret, frame = cap.read()
    frame1 = frame
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray = cv2.subtract(frame2,frame1)
    cv2.addWeighted( gray, 1, gray2, .9, 0.0, dst);
    cv2.equalizeHist(dst)
    frame2 = frame
    gray2 = dst
    display = cv2.applyColorMap(dst, cv2.COLORMAP_JET)
    cv2.imshow('frame',display)
    #cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()