from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
from scipy.spatial.distance import cosine
import mtcnn
from keras.models import load_model
from utils import *
import csv
from playsound import playsound


class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("منظومة تمييز الوجوه")
        self.root.iconbitmap(r"img/icons/facial_recognition.ico")

        self.var_class=StringVar()
        self.var_subject=StringVar()



        
        
        #the label
        title_lbl=Label(self.root,text="الوجوه تمييز",font=("times new roman",30,"bold","italic"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top=Image.open(r"img\face_detector1.jpg") 
        img_top=img_top.resize((650,700),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
    
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)
        
        img_bottom=Image.open(r"img\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg") 
        img_bottom=img_bottom.resize((950,700),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
    
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)
        
        b1_1=Button(f_lbl,text="تمييز الوجوه",cursor="hand2",command=self.face_recog,font=("lemonada",17,"bold"),bg="white",fg="blue")
        b1_1.place(x=365,y=615,width=200,height=50)

        f_subjects = ["المادة الدراسية","كهربائية","فيزياء حديثة","خواص مادة","كيمياء","فيزياء رياضية","معالجة صور","ميكانيك كلاسيكي"]
        s_subjects = ["المادة الدراسية","ثرموداينمك","علم المواد","حاسبات","تحليل عددي","كهربائية متقدمة","مغناطيسية","فيزياء رياضية"]
        t_subjects = ["المادة الدراسية","ليزر","ميكانيك تحليلي","الكترونيات","فيزياء رياضية","معالجة الصور","فيزياء صحية","بصريات"]
        fo_subjects = ["المادة الدراسية","كهرومغناطيسية","صلبة","اطياف","كمية","بلازما","فيزياء رياضية","معالجة الصور"]
        fi_subjects = ["المادة الدراسية","فيزياء رياضية","فيزياء الكم","كهرومغناطيسية","نووية","برمجة في الفيزياء","ميكانيك كلاسيكي","بصريات لاخطية"]
        si_subjects = ["المادة الدراسية","b","c","d","f","g","h","i"]

        def pick_subjects(e):
            if class_combo.get()=="المرحلة الدراسية":
                subject_combo.config(value=["المرحلة الدراسية اولا",""])
                subject_combo.current(0)
            if class_combo.get()=="المرحلة الاولى":
                subject_combo.config(value=f_subjects)
                subject_combo.current(0)
            elif class_combo.get()=="المرحلة الثانية":
                subject_combo.config(value=s_subjects)
                subject_combo.current(0)
            elif class_combo.get()=="المرحلة الثالثة":
                subject_combo.config(value=t_subjects)
                subject_combo.current(0)
            elif class_combo.get()=="المرحلة الرابعة":
                subject_combo.config(value=fo_subjects)
                subject_combo.current(0)
            elif class_combo.get()=="الماجستير":
                subject_combo.config(value=fi_subjects)
                subject_combo.current(0)
            elif class_combo.get()=="الدكتوراه":
                subject_combo.config(value=si_subjects)
                subject_combo.current(0)

        class_combo=ttk.Combobox(f_lbl,textvariable=self.var_class,font=("lemonada",15,"bold"),width=20,state="read only",justify=RIGHT)
        class_combo["values"]=("المرحلة الدراسية","المرحلة الاولى","المرحلة الثانية","المرحلة الثالثة","المرحلة الرابعة","الماجستير","الدكتوراه")
        class_combo.current(0)
        class_combo.place(x=25,y=260,width=250,height=80)
        class_combo.bind("<<ComboboxSelected>>",pick_subjects)

        
        subject_combo=ttk.Combobox(f_lbl,textvariable=self.var_subject,font=("lemonada",14,"bold"),width=20,state="read only",justify=RIGHT)
        subject_combo["values"]=("المرحلة الدراسية اولا","")
        subject_combo.place(x=25,y=435,width=260,height=80)
        subject_combo.current(0)
    
    
    #======attendance=================
    def mark_attendance(self,i,r,n,d):
        with open("Attendance.csv","r+",encoding='utf8',newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
                
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((r not in name_list) and (n not in name_list) and (d not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{r},{n},{d},{dtString},{d1},حاضر,{self.var_subject.get()}")
                
                
                
                
            
           
        
        
    #========face recognition==================
    def face_recog(self):
        
        if self.var_class.get()=="المرحلة الدراسية" or self.var_subject.get()=="" or self.var_subject.get()=="المرحلة الدراسية اولا" or self.var_subject.get()=="المادة الدراسية":
            messagebox.showerror("هناك خطأ ما          ","من فضلك، قم باختيار المرحلة والمادة",parent=self.root)
            return
            
            
        playsound("hello.mp3")
        playsound("abc.mp3")
        
        if os.path.isfile(r'Attendance.csv')==False:
            with open('Attendance.csv',"x",encoding='utf-8-sig',newline='') as z:
                writer = csv.DictWriter(z, fieldnames = ["رقم التسجيل", "اسم الطالب", "القسم" , "الوقت" , "التأريخ" , "حالة الحضور","المادة"])
                writer.writeheader()
                z.close()
        
# =============================================================================
#         filename = 'video.avi'
#         frames_per_seconds = 20.0
#         my_res = '720p'
# 
#         def change_res(cap, width, height):
#             cap.set(3, width)
#             cap.set(4, height)
#             
#             
#         STD_DIMENSIONS = {"480p":(640,480),
#                           "720p":(1280,720),
#                           "1080p":(1920,1080),
#                           "4k":(3840,2160),}
# 
#         def get_dims(cap, res='1080p'):
#             width, height = STD_DIMENSIONS['480p']
#             if res in STD_DIMENSIONS:
#                 width, height = STD_DIMENSIONS[res]
#             change_res(cap, width, height)
#             return width, height
# 
#         VIDEO_TYPE = {
#             'avi':cv2.VideoWriter_fourcc(*'XVID'),
#             'mp4':cv2.VideoWriter_fourcc(*'XVID'),
#             }
# 
#         def get_video_type(filename):
#             filename, ext = os.path.splitext(filename)
#             if ext in VIDEO_TYPE:
#                 return VIDEO_TYPE[ext]
#             return VIDEO_TYPE['avi']
# 
# 
# 
# 
# 
#         cap = cv2.VideoCapture("rtsp://admin:Ahmad1997@192.168.1.64:554/Streaming/Channels/101")
#         dims = get_dims(cap, res=my_res)
# 
#         video_type_cv2 = get_video_type(filename)
#         out = cv2.VideoWriter(filename, video_type_cv2, frames_per_seconds, dims)
# 
#         while True:
#             ret, frame = cap.read()
#             out.write(frame)
#             cv2.imshow('frame', frame)
#             if cv2.waitKey(1) &0xFF== ord('q'):
#                 break
#         cap.release()
#         out.release()
#         cv2.destroyAllWindows()
# =============================================================================
        
        
        
        def recognize(img,
                      detector,
                      encoder,
                      encoding_dict,
                      recognition_t=0.6,
                      confidence_t=0.99,
                      required_size=(160, 160), ):
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = detector.detect_faces(img_rgb)
            for res in results:
                if res['confidence'] < confidence_t:
                    continue
                face, pt_1, pt_2 = get_face(img_rgb, res['box'])
                encode = get_encode(encoder, face, required_size)
                encode = l2_normalizer.transform(encode.reshape(1, -1))[0]
                name = 'unknown'

                distance = float("inf")
                for db_name, db_encode in encoding_dict.items():
                    dist = cosine(db_encode, encode)
                
                
                    if dist < recognition_t and dist < distance:
                        name = db_name
                        distance = dist
                    

                if name == 'unknown':
                    cv2.rectangle(img, pt_1, pt_2, (0, 0, 255), 2)
                    cv2.putText(img, name, pt_1, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
                else:
                    cv2.rectangle(img, pt_1, pt_2, (0, 255, 0), 2)
                    cv2.putText(img, name, (pt_1[0], pt_1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 200, 200), 2)
                    id=int(name)
                
                    
                    conn=mysql.connector.connect(host="localhost",username="root",password="aHmAdSaEeD1997",database="face_recognizer")
                    my_cursor=conn.cursor()
            
                    my_cursor.execute("select Name from student where Student_id="+str(id))
                    n=my_cursor.fetchone()
                    n="+".join(n)
                
                    my_cursor.execute("select Roll from student where Student_id="+str(id))
                    r=my_cursor.fetchone()
                    r="+".join(r)
                
                    my_cursor.execute("select Dep from student where Student_id="+str(id))
                    d=my_cursor.fetchone()
                    d="+".join(d)
                
                    my_cursor.execute("select Student_id from student where Student_id="+str(id))
                    i=my_cursor.fetchone()
                    i="+".join(i)
                    self.mark_attendance(i,r,n,d)
            return img
            


        if __name__ == '__main__':
            encoder_model = 'data/model/facenet_keras.h5'
            encodings_path = 'data/encodings/encodings.pkl'

            face_detector = mtcnn.MTCNN()
            face_encoder = load_model(encoder_model, compile=False)
            encoding_dict = load_pickle(encodings_path)
            

            vc = cv2.VideoCapture('2w_1.mp4')
            nu = 0
            while vc.isOpened():
                ret, frame = vc.read()
                frame = cv2.resize(frame,(1920,1080))
                if not ret:
                    print("no frame:(the system finished attendance registration")
                    now = datetime.now()
                    date_time = now.strftime("%m_%d_%Y@%H_%M_%S")
                    os.rename('Attendance.csv', rf'data\الحضور\[%s] [%s] %s.csv'%(self.var_class.get(),self.var_subject.get(),date_time))
                    break
# =============================================================================
#                 frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#                 h, s, v = frame[:, :, 0], frame[:, :, 1], frame[:, :, 2]
#                 clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize = (8,8))
#                 v = clahe.apply(v)
#                 frame = np.dstack((h,s,v))
#                 frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
# =============================================================================
                frame = recognize(frame, face_detector, face_encoder, encoding_dict)
                cv2.imshow('camera', frame)
                cv2.imwrite('TestImages/ImgNo.'+str(nu)+'.png',frame)
                nu = nu+1

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    now = datetime.now()
                    date_time = now.strftime("%m_%d_%Y@%H_%M_%S")
                    os.rename('Attendance.csv', rf'data\الحضور\[%s] [%s] %s.csv'%(self.var_class.get(),self.var_subject.get(),date_time))
                    break
            vc.release()
            cv2.destroyAllWindows()
        
                            
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
