import cv2

# img = cv2.imread('C:/Users/aswin/PycharmProjects/opencv_python/Resource/park.jpg')
# cv2.waitKey(0)
vid = cv2.VideoCapture(0)
vid.set(3,480)
vid.set(4,640)
labelslist = []
lis = 'Copy of labels.txt'
with open(lis) as f:
    labelslist = f.read().rstrip('\n').split('\n')
config = 'Copy of ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weight = 'Copy of frozen_inference_graph.pb'

con = cv2.dnn_DetectionModel(weight,config)
con.setInputSize(320,320)
con.setInputScale(1.0/ 127.5)
con.setInputMean(127.5)
con.setInputSwapRB(True)

while True:
    succ,img=vid.read()
    ids, confi, bboxs = con.detect(img,confThreshold=.7)
    print(ids,bboxs)
    if len(ids)!=0:
        for id, confidence, bbox in zip(ids.flatten(),confi.flatten(),bboxs):
            cv2.rectangle(img,bbox,color=(0,0,225),thickness=1)
            cv2.putText(img, str(round(confidence*100,2)), (bbox[0]+150, bbox[1] +30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 225),1)
            cv2.putText(img,labelslist[id-1],(bbox[0]+10,bbox[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,225),1)
    cv2.imshow("img",img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

