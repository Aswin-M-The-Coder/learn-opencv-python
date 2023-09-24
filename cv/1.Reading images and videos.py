import cv2

#reading images
img = cv2.imread("C:/Users/aswin/Desktop/Pycharm Projects/learn cv/Resources/Photos/cat.jpg")
cv2.imshow("cat",img)
#setting wait time
cv2.waitKey(0)

#reading videos
#0,1,2.. can be given to open webcam or path
capture = cv2.VideoCapture("C:/Users/aswin/Desktop/Pycharm Projects/learn cv/Resources/Videos/dog.mp4")
while True:
    isTrue,frame=capture.read()
    cv2.imshow("video",frame)
    if cv2.waitKey(1) and 0xFF==ord("q"):
       break
capture.release()
cv2.destroyAllWindows()