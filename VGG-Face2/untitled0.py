# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 10:03:21 2022

@author: ahmad
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
import os
import glob as gb
from tqdm import tqdm
import tensorflow as tf
#defining train data set
train_dir='data'
Train_Data=tf.keras.preprocessing.image.ImageDataGenerator(
    horizontal_flip=True,
    rescale=1/255.0,
).flow_from_directory(train_dir,batch_size=16,subset="training",target_size=(224,224),shuffle=False)

list(Train_Data.class_indices.keys())

classes=list(Train_Data.class_indices.keys())
plt.figure(figsize=(30,30))
for X_batch, y_batch in Train_Data:
    # create a grid of 7x7 images
    for i in range(0,16):
        plt.subplot(4,4,i+1)
        plt.imshow(X_batch[i])
        plt.title(classes[np.where(y_batch[i]==1)[0][0]])
    # show the plot
    plt.show()
    break

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import ZeroPadding2D, Convolution2D, MaxPooling2D, Dropout, Flatten, Activation

def vgg_face():
    model = Sequential()
    model.add(ZeroPadding2D((1,1),input_shape=(224,224, 3)))
    model.add(Convolution2D(64, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))
    
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(128, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))
    
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(256, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(256, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(256, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))
    
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))
    
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))
    
    model.add(Convolution2D(4096, (7, 7), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Convolution2D(4096, (1, 1), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Convolution2D(2622, (1, 1)))
    model.add(Flatten())
    model.add(Activation('softmax'))
    return model

model = vgg_face()

model.load_weights('vgg_face_weights.h5')

from tensorflow.keras.models import Model
model = Model(inputs=model.layers[0].input, outputs=model.layers[-2].output)

model.summary()

embedding_vector = model.predict(Train_Data,steps=len(Train_Data), verbose=1)

y_train=Train_Data.labels

np.save('Xdata',embedding_vector)
np.save('ydata',y_train)

embedding_vector = np.load('Xdata.npy')
y_train = np.load('ydata.npy')

embedding_vector[0]

embedding_vector[500]

y_train[0]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(embedding_vector,y_train,test_size=0.1,shuffle=True, stratify=y_train,random_state=42)
from sklearn.utils import shuffle
X_train,y_train = shuffle(X_train,y_train)
# Standarize features
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
from sklearn.decomposition import PCA

pca = PCA(n_components=128)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

X_train.shape

from sklearn.svm import SVC

clf = SVC(kernel='linear',C=2.,class_weight='balanced',decision_function_shape='ovo',probability=True)
clf.fit(X_train, y_train)

y_predict = clf.predict(X_test)
y_predict[:5]

# Find the classification accuracy
from sklearn.metrics import accuracy_score
print(f'The Accuracy of VGGFace2 is {accuracy_score(y_test,y_predict)*100} %')

import seaborn as sns
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_predict)
plt.figure(figsize=(10,10))
sns.heatmap(cm,  annot=True, fmt="d" ,cmap="YlGnBu")

from sklearn.metrics import classification_report
print(classification_report(y_test,y_predict))

from sklearn.tree import DecisionTreeClassifier

DTC = DecisionTreeClassifier()
DTC.fit(X_train, y_train)

y_predict_1 = DTC.predict(X_test)
y_predict_1[:5]

# Find the classification accuracy
from sklearn.metrics import accuracy_score
print(f'The Accuracy of VGGFace2 is {accuracy_score(y_test,y_predict_1)*100} %')

import seaborn as sns
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_predict_1)
plt.figure(figsize=(10,10))
sns.heatmap(cm,  annot=True, fmt="d" ,cmap="YlGnBu")

from sklearn.ensemble import RandomForestClassifier

RFC = RandomForestClassifier()
RFC.fit(X_train, y_train)

y_predict_2 = RFC.predict(X_test)
y_predict_2[:5]

# Find the classification accuracy
from sklearn.metrics import accuracy_score
print(f'The Accuracy of VGGFace2 is {accuracy_score(y_test,y_predict_2)*100} %')

import seaborn as sns
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_predict_2)
plt.figure(figsize=(10,10))
sns.heatmap(cm,  annot=True, fmt="d" ,cmap="YlGnBu")

from numpy import expand_dims
from cv2 import resize,INTER_CUBIC
from tensorflow.keras.preprocessing.image import  img_to_array

def preprocess_image(img):
    img = img_to_array(img)
    img = img/255.0
    img = expand_dims(img, axis=0)
    return img

def Face_Recognition(roi,model,scaler,pca,clf):
    roi=resize(roi,dsize=(224,224),interpolation=INTER_CUBIC)
    roi=preprocess_image(roi)
    embedding_vector = model.predict(roi)[0]

    embedding_vector=scaler.transform(embedding_vector.reshape(1, -1))
    embedding_vector_pca = pca.transform(embedding_vector)
    result1 = clf.predict(embedding_vector_pca)[0]
    #print(result1)
    y_predict = clf.predict_proba(embedding_vector_pca)[0]
    #print(y_predict)
    
    result = np.where(y_predict > 0.3)[0]
    
    return result , y_predict
print((list(Train_Data.class_indices.keys())))

import numpy as np
import matplotlib.pyplot as plt
from facenet_pytorch import MTCNN
import cv2
mtcnn = MTCNN(image_size=100, margin=10, min_face_size=5,device='cpu', post_process=False)

cap=cv2.VideoCapture('1_1_1.mp4')
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
classes = {'1': 0, '10': 1,'11':2,'12':3, '13':4, '14':5, '15':6, '16':7, '17':8, '18':9, '19':10,
           '2':11, '20':12, '21':13, '22':14, '23':15, '24':16, '25':17, '26':18, '27':19, 
           '28':20, '29':21, '3':22, '30':23, '31':24, '4':25, '5':26, '6':27, '7':28, 
           '8':29, '9':30}


def ImageClass(n):
    for x , y in classes.items():
        if n == y :
            return x
size = (1920, 1080)

result_video = cv2.VideoWriter('1.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)
font = cv2.FONT_HERSHEY_SIMPLEX     
fontScale = 1
color = (255, 0, 0)
thickness = 2
other = 0
while True :
    ret, frame = cap.read()
    if not ret:
        break  
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame=cv2.resize(frame,(1920,1080),interpolation=cv2.INTER_CUBIC)
    #frame=cv2.GaussianBlur(frame, ksize=(3,3), sigmaX=0)
    #frame_face = frame.copy()
    frame_face=cv2.resize(frame,(640,640),interpolation=cv2.INTER_CUBIC)
    boxes, probs = mtcnn.detect(frame_face, landmarks=False)

    if  not probs.all() == None and probs.all()> 0.2 :
        for x1,y1,x2,y2 in boxes :
            x1,x2,y1,y2=int(x1) * 1920 //640,int(x2) * 1920 //640,int(y1) * 1080 //640,int(y2) * 1080 //640
            roi=frame[y1:y2,x1:x2]
            result , y_predict=Face_Recognition(roi,model,scaler,pca,clf)
            if len(result) > 1 :
                cv2.putText(frame, ImageClass(result[0]) , (x1-5,y1-5), font,fontScale, color, thickness, cv2.LINE_AA)
                cv2.putText(frame, str(np.round(y_predict[result[0]],2)) , (x2,y2-10), font,fontScale, color, thickness, cv2.LINE_AA)
            elif  len(result)== 0 :
                roi=cv2.cvtColor(roi,cv2.COLOR_RGB2BGR)  
                #cv2.imwrite(f'Pic{other}.png', roi)
                cv2.putText(frame, 'Other' , (x1-5,y1-5), font,fontScale, color, thickness, cv2.LINE_AA)
                other = other + 1
            else :
                cv2.putText(frame, ImageClass(result) , (x1-5,y1-5), font,fontScale, color, thickness, cv2.LINE_AA)
                cv2.putText(frame, str(np.round(y_predict[result[0]],2)) , (x2,y2-10), font,fontScale, color, thickness, cv2.LINE_AA)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)             
    result_video.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
result_video.release()
cv2.destroyAllWindows() 

from joblib import dump
dump(scaler, 'scaler.joblib') 

dump(pca, 'pca_model.joblib')

dump(clf, 'SVC.joblib') 

import numpy as np
import cv2
import os
import tensorflow as tf
from joblib import  load
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import ZeroPadding2D, Convolution2D, MaxPooling2D, Dropout, Flatten, Activation

def vgg_face():
    model = Sequential()
    model.add(ZeroPadding2D((1,1),input_shape=(224,224, 3)))
    model.add(Convolution2D(64, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))
    
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(128, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))
    
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(256, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(256, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(256, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))
    
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))
    
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))
    
    model.add(Convolution2D(4096, (7, 7), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Convolution2D(4096, (1, 1), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Convolution2D(2622, (1, 1)))
    model.add(Flatten())
    model.add(Activation('softmax'))
    return model
model = vgg_face()

model.load_weights('vgg_face_weights.h5')
from tensorflow.keras.models import Model
model = Model(inputs=model.layers[0].input, outputs=model.layers[-2].output)
scaler=load( 'scaler.joblib') 
pca=load( 'pca_model.joblib') 
clf=load( 'SVC.joblib') 
from numpy import expand_dims
from cv2 import resize,INTER_CUBIC
from tensorflow.keras.preprocessing.image import  img_to_array

def preprocess_image(img):
    img = img_to_array(img)
    img = img/255.0
    img = expand_dims(img, axis=0)
    return img

def Face_Recognition(roi,model,scaler,pca,clf):
    roi=resize(roi,dsize=(224,224),interpolation=INTER_CUBIC)
    roi=preprocess_image(roi)
    embedding_vector = model.predict(roi)[0]

    embedding_vector=scaler.transform(embedding_vector.reshape(1, -1))
    embedding_vector_pca = pca.transform(embedding_vector)
    result1 = clf.predict(embedding_vector_pca)[0]
    #print(result1)
    y_predict = clf.predict_proba(embedding_vector_pca)[0]
    #print(y_predict)
    
    result = np.where(y_predict > 0.1)[0]
    
    return result , y_predict

import numpy as np
import matplotlib.pyplot as plt
from facenet_pytorch import MTCNN
import cv2
mtcnn = MTCNN(image_size=160, margin=14, min_face_size=20,device='cpu', post_process=False)

cap=cv2.VideoCapture('1_1.mp4')
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
classes = {'1': 0, '10': 1,'11':2,'12':3, '13':4, '14':5, '15':6, '16':7, '17':8, '18':9, '19':10,
           '2':11, '20':12, '21':13, '22':14, '23':15, '24':16, '25':17, '26':18, '27':19, 
           '28':20, '29':21, '3':22, '30':23, '31':24, '4':25, '5':26, '6':27, '7':28, 
           '8':29, '9':30}


def ImageClass(n):
    for x , y in classes.items():
        if n == y :
            return x
size = (1920, 1080)

result_video = cv2.VideoWriter('Face.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)
font = cv2.FONT_HERSHEY_SIMPLEX     
fontScale = 1
color = (255, 0, 255)
thickness = 2
other = 0
nu = 0
while True :
    ret, frame = cap.read()
    if not ret:
        break  
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame=cv2.resize(frame,(1920,1080),interpolation=cv2.INTER_CUBIC)
    #frame=cv2.GaussianBlur(frame, ksize=(3,3), sigmaX=0)
    #frame_face = frame.copy()
    #frame_face=cv2.resize(frame_face,(640,640),interpolation=cv2.INTER_CUBIC)
    boxes, probs = mtcnn.detect(frame, landmarks=False)
    
    if  not probs.all() == None and probs.all()> 0.99 :
        for x1,y1,x2,y2 in boxes :
            x1,x2,y1,y2=int(x1),int(x2),int(y1),int(y2)
            roi=frame[y1:y2,x1:x2]
            result , y_predict=Face_Recognition(roi,model,scaler,pca,clf)
            if len(result) > 1 :
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, ImageClass(result[0]) , (x1-5,y1-5), font,fontScale, color, thickness, cv2.LINE_AA)
                #cv2.putText(frame, str(np.round(y_predict[result[0]],2)) , (x2,y1-10), font,fontScale, color, thickness, cv2.LINE_AA)
            elif  len(result)== 0 :
                roi=cv2.cvtColor(roi,cv2.COLOR_RGB2BGR)  
                #cv2.imwrite(f'Pic{other}.png', roi)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, 'Other' , (x1-5,y1-5), font,fontScale, color, thickness, cv2.LINE_AA)
                other = other + 1
            else :
                cv2.putText(frame, ImageClass(result) , (x1-5,y1-5), font,fontScale, color, thickness, cv2.LINE_AA)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                #cv2.putText(frame, str(np.round(y_predict[result[0]],2)) , (x2,y1-10), font,fontScale, color, thickness, cv2.LINE_AA)
    frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)             
    #result_video.write(frame)
    cv2.imwrite('F:/Thesis/VGG_face2/Test/test'+str(nu)+'.png',frame)
    nu = nu+1
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
result_video.release()
cv2.destroyAllWindows() 