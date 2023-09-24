import cv2
import os

alg = "haarcascade_frontalface_default.xml"
datasets = 'datasets'
sub_data = 'Aswin M'

path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.mkdir(path)

(width, height) = (130, 100)

cas = cv2.CascadeClassifier(alg)
cam = cv2.VideoCapture(0)

count = 1

while count < 61:
    succ, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cas.detectMultiScale(gray, 1.3, 4)
    for w, x, y, z in faces:
        cv2.rectangle(img, (w, x), (w + y, x + z), (255, 0, 0), 2)
        face = gray[y:x + z, x:w + y]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('%s/%s.png' % (path, count), face_resize)
    count += 1
    print(count)

    cv2.imshow('img', img)
    key = cv2.waitKey(10)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
