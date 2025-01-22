from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student     
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter
from time import strftime
import tkinter

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("منظومة تمييز الاوجه")
        self.root.iconbitmap(r"img/icons/hnet.com-image.ico")

        
        #image
        img1=Image.open(r"img\20.png") 
        img1=img1.resize((1530,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
    
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=1530,height=130)
        


        #big image
        img3=Image.open(r"img\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg") 
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        
        #the label
        title_lbl=Label(bg_img,text="المستنصرية الجامعة في العلوم لكلية الالكتروني الحضور نظام",font=("times new roman",30,"bold","italic"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=75)
        
        #==========time==============
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        lbl = Label(title_lbl, font = ('loopy',35,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=(0),width=220,height=60)
        time()
        
       
        #student button
        img4=Image.open(r"img\clg.jpg") 
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="الطالب معلومات",command=self.student_details,cursor="hand2",font=("times new roman",15),bg="white",fg="blue")
        b1_1.place(x=200,y=300,width=220,height=40)
        
        #detect button
        img5=Image.open(r"img\face_detector1.jpg") 
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text=" البشري الوجه محدد",cursor="hand2",command=self.face_data,font=("times new roman",15),bg="white",fg="blue")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        #attendance button
        img6=Image.open(r"img\smart-attendance.jpg") 
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text=" الحضور",cursor="hand2",command=self.attendance_data,font=("times new roman",15),bg="white",fg="blue")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        #help button
        img7=Image.open(r"img\help1.jpg") 
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text=" المساعدة على الحصول",cursor="hand2",command=self.help_data,font=("times new roman",15),bg="white",fg="blue")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        #train button
        img8=Image.open(r"img\train1.png") 
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="الاوجه تمييز على التطبيق تدريب",cursor="hand2",command=self.train_data,font=("times new roman",15),bg="white",fg="blue")
        b1_1.place(x=200,y=580,width=220,height=40)
        
        
        #photos button
        img9=Image.open(r"img\train.png") 
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="البيانات قاعدة",cursor="hand2",command=self.open_img,font=("times new roman",15),bg="white",fg="blue")
        b1_1.place(x=500,y=580,width=220,height=40)
        
        #developer button
        img10=Image.open(r"img\developer1.png") 
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="المطور",cursor="hand2",command=self.developer_data,font=("times new roman",15),bg="white",fg="blue")
        b1_1.place(x=800,y=580,width=220,height=40)
        
        
        #exit button
        img11=Image.open(r"img\exit.png") 
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="خروج",cursor="hand2",command=self.iExit,font=("times new roman",15),bg="white",fg="blue")
        b1_1.place(x=1100,y=580,width=220,height=40)
        
    def open_img(self):
        os.startfile(r'data\people')
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("face recognition","are you sure exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
         
        
    #===============functions buttons========================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
        
        
    
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
            