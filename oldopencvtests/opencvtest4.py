import cv2

 # Load two images
img1 = cv2.imread('photo2.jpg')
img2 = cv2.imread('photo3.jpg')
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
 
# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
img2gray2 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
#ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
#mask_inv = cv2.bitwise_not(mask)
difference = cv2.subtract(img1,img2)
difference = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

difference = cv2.adaptiveThreshold(difference,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3)
#difference = cv2.bitwise_not(difference);
  

cv2.imshow('res',difference)
cv2.waitKey(0)
cv2.destroyAllWindows()