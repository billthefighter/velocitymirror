import numpy as np
import cv2

cap = cv2.VideoCapture(0)

w = 1280
h = 1024

#w=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ))
#h=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT ))
# video recorder
fourcc = cv2.cv.CV_FOURCC(*'XVID')  # cv2.VideoWriter_fourcc() does not exist
video_writer = cv2.VideoWriter("output.avi", fourcc, 25, (w, h))

# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()