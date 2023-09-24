import cv2

alg = 'haarcascade_frontalface_default.xml'
cas = cv2.CascadeClassifier(alg)
cam = cv2.VideoCapture(0)
while True:
    succ, img = cam.read()
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = cas.detectMultiScale(grayimg, 1.3, 4)
    for (x, y, z, h) in face:
        cv2.rectangle(img, (x, y), (x + z, y + h), color=(0, 0, 225), thickness=2)
    cv2.imshow("detected", img)
    cv2.waitKey(10)
    if cv2.waitKey(1) & 0xff == 'q':
        break
# img=cv2.imread("C:/Users/aswin/PycharmProjects/opencv_python/Resource/lady.jpg")
# grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# face = cas.detectMultiScale(grayimg,1.3,4)
# for (x,y,z,h) in face:
#     cv2.rectangle(img,(x,y),(x+z,y+h),color=(0,0,225),thickness=2)
cv2.imshow("detected", img)
cv2.waitKey(10)
