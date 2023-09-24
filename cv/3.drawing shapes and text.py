import cv2
import numpy as np

#empty image
empty=np.zeros((500,500,3),dtype='uint8')
cv2.imshow('blank',empty)

#paint the image
#empty[height:width]
empty[200:300,200:400]=0,0,255
cv2.imshow('blank',empty)

#drawing rectangle
#cv2.rectangle(image,start,end,color,thickness=(-1 or cv.FILLED for full paint))
empty=cv2.rectangle(empty,(0,0),(250,250),(0,255,0),thickness=3)
cv2.imshow('blank',empty)

#cv2.circle(image,centre,radius,color,thickness)
empty=cv2.circle(empty,(250,250),15,(255,0,0),thickness=2)
cv2.imshow('blank',empty)

#cv2.line(image,start,end,color,thickness)
empty=cv2.line(empty,(0,0),(250,250),(255,255,255),thickness=2)
cv2.imshow('blank',empty)

#cv2.putText(image,string,start point,font, ,color,thickness)
empty=cv2.putText(empty,"Hello I'm Aswin",(150,225),cv2.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv2.imshow('blank',empty)

cv2.waitKey(0)