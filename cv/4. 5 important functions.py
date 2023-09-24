import cv2
import numpy as np

img = cv2.imread("C:/Users/aswin/Desktop/Pycharm Projects/learn cv/Resources/Photos/cat.jpg")
cv2.imshow("cat",img)

#gray
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray img",gray)

#blur
#cv2.GaussianBlur(image,ksize,
blur=cv2.GaussianBlur(img,(9,9),cv2.BORDER_DEFAULT)
cv2.imshow("blur img",blur)

#edge cascade
#cv2.Canny(img,thresh1,thresh2)
canny=cv2.Canny(img,150,250)
cv2.imshow("edge",canny)
#setting wait time
cv2.waitKey(0)