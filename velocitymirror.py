import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#Open video capture from device 0 (which is usually built-in webcam)
cap = cv2.VideoCapture(0)
#Set up variables to store output of webcam capture and pass to subsequent functions
ret, frame = cap.read()
#Store initial frame, convert to grey
frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#since we need two frames to subtract from each other in subsequent steps, we need to store something in frame 2. but it also needs to be a color image.
frame2 = frame
#these are placeholders. see above comment.
gray2 = frame1
dst = frame1

def facedetect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces

def drawfaces(faces,img):
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        #This dosn't seem to work right now; it works in another test program. Fix later?
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
            #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return(img)

#Start main loop. This is where the program processes images.
while(cap.isOpened()):
    #recapture frame
    ret, frame = cap.read()

    frame1 = frame
    frame_face = facedetect(frame1)
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    #Compare frame 1 and frame 2. this gives the difference between images, which should map to velocity.
    gray = cv2.subtract(frame2,frame1)
    #Here's the hacked "accumulator". it does a weighted add of the subtraction we just preformed to the "history" of previous subtractions. By changing the parameter after gray2, we can change the amount of time before things decay to grey. Try values of .99 or .1 
    cv2.addWeighted( gray, 1, gray2, .6, 0, dst);
    #I haven't yet determined if this does anything.
    cv2.equalizeHist(dst)

    frame2 = frame
    gray2 = dst
    
    dst = drawfaces(frame_face,dst)
    #Two of my favorite color schemes
    display = cv2.applyColorMap(dst, cv2.COLORMAP_PINK)
    #display = cv2.applyColorMap(dst, cv2.COLORMAP_JET)
    cv2.imshow('frame',display)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()