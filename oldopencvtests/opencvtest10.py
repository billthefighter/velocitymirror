import numpy as np
import cv2


#cap = cv2.VideoCapture('movie2.mov')	
cap = cv2.VideoCapture('movie6.mp4')
ret, frame = cap.read()
#print frame.shape
frame1 = frame
frame2 = frame
#accumulate = cv2.subtract(frame,frame)
#accumulate = cv2.cvtColor(accumulate, cv2.COLOR_BGR2GRAY)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
fourcc = cv2.cv.CV_FOURCC(*'XVID')
height , width , layers =  frame.shape
video = cv2.VideoWriter('video.avi',-1,1,(width,height))
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))


def brighten(img):
    return cv2.equalizeHist(img)
    # hist,bins = np.histogram(img.flatten(),256,[0,256])
   
    # cdf = hist.cumsum()
    # cdf_normalized = cdf * hist.max()/ cdf.max()

    # cdf_m = np.ma.masked_equal(cdf,0)
    # cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    # cdf = np.ma.filled(cdf_m,0).astype('uint8')
    # img2 = cdf[img]
    # return img2

while(cap.isOpened()):
    ret, frame = cap.read()
    frame1 = frame
    difference = cv2.subtract(frame2,frame1)
    #frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    #frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    #difference = cv2.subtract(frame2,frame1)
    #difference = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    #difference = cv2.addWeighted(difference, 2, frame1, 1, 1)
    #difference = brighten(difference) 
    #difference = cv2.adaptiveThreshold(difference,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,3)
    #difference = cv2.applyColorMap(difference, cv2.COLORMAP_HSV)
	#difference = cv2.bitwise_not(difference);
    #accumulate += gray
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #accumulate = difference + accumulate
    #difference = cv2.applyColorMap(difference, cv2.COLORMAP_JET)
    frame2 = frame
    #cv2.imshow('frame',accumulate)
    #print difference.shape
    #video.write(difference)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()