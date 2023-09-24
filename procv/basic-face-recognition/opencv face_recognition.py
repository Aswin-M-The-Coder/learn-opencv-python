import cv2
import numpy
import os

size = 4
alg = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'
cas = cv2.CascadeClassifier(alg)
print('Training...')
(images, labels, names, ID) = ([], [], {}, 0)
for (dirpaths, dirnames, filenames) in os.walk(datasets):
    for dirname in dirnames:
        names[ID] = dirname
        subjectpath = os.path.join(datasets, dirname)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            label = ID
            images.append(cv2.imread(path, 0))
            labels.append(ID)
        ID += 1
(width, height) = (130, 100)
(images, labels) = [numpy.array(lis) for lis in [images, labels]]
# model
model = cv2.face.LBPHFaceRecognizer_create()
# model = cv2.face.FisherFaceRecognizer_create()
model.train(images, labels)
cam = cv2.VideoCapture(0)
cnt = 0
while True:
    succ, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cas.detectMultiScale(gray, 1.3, 4)
    if len(faces)!=0:
        for w, x, y, z in faces:
            cv2.rectangle(img, (w, x), (w + y, x + z), (255, 0, 0), 2)
            face = gray[y:x + z, x:w + y]
            face_resize = cv2.resize(face, (width, height))
            predictions = model.predict(face_resize)
            print(predictions)
            if predictions[1] > 50:
                cv2.putText(img, names[predictions[0]], (w, x-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 225, 0),1)
                print(names[predictions[0]])
            else:
                cv2.putText(img, names[predictions[0]], (w, x - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 225, 0), 1)
                print('unknown')
    cv2.imshow('classification', img)
    key = cv2.waitKey(10)
    if key == 27:
        break
