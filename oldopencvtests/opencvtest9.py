import numpy as np
import cv2


cap = cv2.VideoCapture('movie2.mov')	
#cap = cv2.VideoCapture('movie5.m4v')
ret, frame = cap.read()
frame1 = frame
frame2 = frame
accumulate = cv2.subtract(frame,frame)

while(cap.isOpened()):
    ret, frame = cap.read()
    frame1 = frame
    #difference = cv2.subtract(frame2,frame1)
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    difference = cv2.subtract(frame2,frame1)
    #difference = cv2.adaptiveThreshold(difference,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,3)
    difference = cv2.applyColorMap(difference, cv2.COLORMAP_JET)
	#difference = cv2.bitwise_not(difference);
    #accumulate += gray
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame2 = frame
    cv2.imshow('frame',difference)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()