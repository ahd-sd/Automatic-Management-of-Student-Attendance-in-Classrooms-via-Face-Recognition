from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import os
import pickle
import numpy as np
import cv2
import mtcnn
from keras.models import load_model
from utils import get_face, get_encode, l2_normalizer, normalize

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("منظومة تمييز الاوجه")
        self.root.iconbitmap(r"C:/Users/ahmad/OneDrive/Desktop/thesis/attendance project/img/icons/brain.ico")

        
        
        

        img_top=Image.open(r"C:\Users\ahmad\Desktop\Desktop\designs\bottom.jpg") 
        img_top=img_top.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
    
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=5,width=1530,height=325)
        
        b1_1=Button(self.root,text="البيانات تدريب",command=self.train_classifier,cursor="hand2",font=("times new roman",40,"bold"),bg="white",fg="blue")
        b1_1.place(x=0,y=330,width=1530,height=100)
        
        
        
        img_bottom=Image.open(r"img\facialrecognition.png") 
        img_bottom=img_bottom.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
    
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)
        
    def train_classifier(self):
        # hyper-parameters
        encoder_model = 'data/model/facenet_keras.h5'
        people_dir = 'data/people'
        encodings_path = 'data/encodings/encodings.pkl'
        required_size = (160, 160)

        face_detector = mtcnn.MTCNN()
        face_encoder = load_model(encoder_model)

        encoding_dict = dict()
        
        for person_name in os.listdir(people_dir):
            person_dir = os.path.join(people_dir, person_name)
            encodes = []
            for img_name in os.listdir(person_dir):
                img_path = os.path.join(person_dir, img_name)
                img = cv2.imread(img_path)
                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                results = face_detector.detect_faces(img_rgb)
                if results:
                    res = max(results, key=lambda b: b['box'][2] * b['box'][3])
                    face, _, _ = get_face(img_rgb, res['box'])

                    face = normalize(face)
                    face = cv2.resize(face, required_size)
                    encode = face_encoder.predict(np.expand_dims(face, axis=0))[0]
                    encodes.append(encode)
            if encodes:
                encode = np.sum(encodes, axis=0)
                encode = l2_normalizer.transform(np.expand_dims(encode, axis=0))[0]
                encoding_dict[person_name] = encode


        for key in encoding_dict.keys():
            print(key)

        with open(encodings_path, 'bw') as file:
            pickle.dump(encoding_dict, file)


        messagebox.showinfo("النتيجة","تم الانتهاء من عملية تدريب البيانات")
        
     
        
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()