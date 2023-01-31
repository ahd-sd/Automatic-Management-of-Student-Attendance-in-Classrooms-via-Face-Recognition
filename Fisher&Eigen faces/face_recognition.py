import numpy as np
import cv2
import os
import json

faceDetect = cv2.CascadeClassifier('./utils/haarcascade_frontalface_default.xml')
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
#face_recognizer = cv2.face.EigenFaceRecognizer_create()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer.read("./utils/model/model.yml")

# EigenFace and FisherFace require all images for training to be of equal dimensions
width = 215
height = 215

with open('./utils/model/config.json') as f:
    data = json.load(f)

vid = cv2.VideoCapture("rtsp://admin:YourPassword@192.168.1.64:554/Streaming/Channels/101")
img_id = 0
while(True):
    ret,img = vid.read()
    img = cv2.resize(img,(1920,1080))
    if not ret:
        print("no frame:(the system finished attendance registration")
        break
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.1,7)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        #label,dist = face_recognizer.predict(gray[y:y+h,x:x+w])
        label,dist = face_recognizer.predict(cv2.resize(gray[y:y+h,x:x+w],(218,218)))
        confidence=int((100*(1-dist/300)))
        if abs(confidence)>72.9:
            cv2.putText(img,str(data[str(label)]).upper(),(x,y+h+25),cv2.FONT_HERSHEY_PLAIN,1,(255, 255, 0),2)
        else:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,254),3)
            cv2.putText(img,"Unknown",(x,y-20),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,255),2)
    cv2.imwrite('F:/Thesis/OpenCV/lpbh,eigenfaces,fisherfaces/TestImages/LBPH/'+str(img_id)+'.png',img)
    cv2.imshow("Face",img)
    img_id = img_id+1

    if(cv2.waitKey(1)==ord('q')):
        break
vid.release()
cv2.destroyAllWindows()