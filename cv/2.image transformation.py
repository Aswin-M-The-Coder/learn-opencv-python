import cv2

def rescaleframe(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv2.resize(frame,dimensions)

capture = cv2.VideoCapture("C:/Users/aswin/Desktop/Pycharm Projects/learn cv/Resources/Videos/kitten.mp4")
while True:
    isTrue,frame=capture.read()
    frame_resize=rescaleframe(frame)
    cv2.imshow("video",frame)
    cv2.imshow("video resize",frame_resize)
    if cv2.waitKey(20) and 0xFF==ord("q"):
       break
capture.release()
cv2.destroyAllWindows()