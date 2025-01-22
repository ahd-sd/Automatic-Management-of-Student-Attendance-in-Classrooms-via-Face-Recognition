from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import webbrowser

class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        root.configure(background = '#f9bf6a')
        self.root.title("منظومة تمييز الاوجه")
        self.root.iconbitmap(r"C:/Users/ahmad/OneDrive/Desktop/thesis/attendance project/img/icons/help.ico")

        
        
        title_lbl=Label(self.root,text="معنا التواصل يمكنكم ،مساعدة اي على للحصول",font=("times new roman",28,"bold","italic"),bg="#f9bf6a",fg="#141414")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #left label frame
        Left_frame=LabelFrame(self.root,bd=4,bg="#f9bf6a",fg="#141414",relief=RIDGE,text="الطالب معلومات",font=("times new roman",16,"bold"))
        Left_frame.place(x=0,y=46,width=730,height=780)
        
        img1=Image.open(r"img\myimg.jpg") 
        img1=img1.resize((250,250),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        bg_img=Label(Left_frame,image=self.photoimg1)
        bg_img.place(x=0,y=5,width=220,height=240)
        
        search_label=Label(Left_frame,text="احمد سعيد لطيف \n خريج كلية العلوم الجامعة المستنصرية \nقسم الفيزياء \n 07809331261: رقم الهاتف",font=("lemonada",15,"bold"),anchor='center',bg="#9c332d",fg="#f3f1e9")
        search_label.place(x=221,y=5,width=500,height=240)
        
        save_btn=Button(Left_frame,text="Email",command=self.gmail1,width=20, height=2,font=("times new roman",16,"bold"),bg="#9c332d",fg="#f3f1e9")
        save_btn.place(x=0,y=250)
        
        save_btn=Button(Left_frame,text="Facebook",command=self.facebook1,width=20, height=2,font=("times new roman",16,"bold"),bg="#9c332d",fg="#f3f1e9")
        save_btn.place(x=472,y=250)
        
        save_btn=Button(Left_frame,text="Telegram",command=self.tele1,width=20, height=2,font=("times new roman",16,"bold"),bg="#9c332d",fg="#f3f1e9")
        save_btn.place(x=0,y=350)
        
        save_btn=Button(Left_frame,text="Instagram",width=20, height=2,font=("times new roman",16,"bold"),bg="#9c332d",fg="#f3f1e9")
        save_btn.place(x=472,y=350)
        
        #right frame
        right_frame=LabelFrame(self.root,bd=4,bg="#f9bf6a",fg="#141414",relief=RIDGE,text="الطالب معلومات",font=("times new roman",16,"bold"))
        right_frame.place(x=780,y=46,width=730,height=780)
        
        img2=Image.open(r"img\drmhmd.jpg") 
        img2=img2.resize((250,250),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        bg_img=Label(right_frame,image=self.photoimg2)
        bg_img.place(x=0,y=5,width=220,height=240)
        
        search_label=Label(right_frame,text="الاستاذ الدكتور محمد يوسف كامل \n بروفيسور معالجة الصور الرقمية في \nكلية العلوم الجامعة المستنصرية \nقسم الفيزياء \nرقم الهاتف: 07702575673",font=("lemonada",15,"bold"),anchor='center',bg="#9c332d",fg="#f3f1e9")
        search_label.place(x=221,y=5,width=500,height=240)
        
        save_btn=Button(right_frame,text="Email",command=self.gmail2,width=20, height=2,font=("times new roman",16,"bold"),bg="#9c332d",fg="#f3f1e9")
        save_btn.place(x=0,y=250)
        
        save_btn=Button(right_frame,text="Facebook",command=self.facebook2,width=20, height=2,font=("times new roman",16,"bold"),bg="#9c332d",fg="#f3f1e9")
        save_btn.place(x=472,y=250)
        
        save_btn=Button(right_frame,text="Telegram",command=self.tele2,width=20, height=2,font=("times new roman",16,"bold"),bg="#9c332d",fg="#f3f1e9")
        save_btn.place(x=0,y=350)
        
        save_btn=Button(right_frame,text="ResearchGate",command=self.RG,width=20, height=2,font=("times new roman",16,"bold"),bg="#9c332d",fg="#f3f1e9")
        save_btn.place(x=472,y=350)
        
        save_btn=Button(right_frame,text="Google Scholar",width=20, height=2,font=("times new roman",16,"bold"),bg="#9c332d",fg="#f3f1e9")
        save_btn.place(x=0,y=450)
        
        save_btn=Button(right_frame,text="Orcid",command=self.orcid,width=20, height=2,font=("times new roman",16,"bold"),bg="#9c332d",fg="#f3f1e9")
        save_btn.place(x=472,y=450)
        
        save_btn=Button(right_frame,text="Scopus",width=20, height=2,font=("times new roman",16,"bold"),bg="#9c332d",fg="#f3f1e9")
        save_btn.place(x=0,y=550)
        
        save_btn=Button(right_frame,text="Publons",width=20, height=2,font=("times new roman",16,"bold"),bg="#9c332d",fg="#f3f1e9")
        save_btn.place(x=472,y=550)
        
        save_btn=Button(right_frame,text="UOM profile",command=self.UOM,width=20, height=2,font=("times new roman",16,"bold"),bg="#9c332d",fg="#f3f1e9")
        save_btn.place(x=236,y=650)
        
    def facebook1(self):
        webbrowser.open_new_tab("https://www.facebook.com/A97S21/")
        
    def facebook2(self):
        webbrowser.open_new_tab("https://www.facebook.com/profile.php?id=100011465853182")
        
    def inst(self):
        webbrowser.open_new_tab("")
        
    def scopus(self):
        webbrowser.open_new_tab("")
    def publons(self):
        webbrowser.open_new_tab("")
        
    def UOM(self):
        webbrowser.open_new_tab("https://uomustansiriyah.edu.iq/e-learn/profile.php?id=820")
        
    def orcid(self):
        webbrowser.open_new_tab("https://orcid.org/0000-0001-5709-2549")
    def RG(self):
        webbrowser.open_new_tab("https://www.researchgate.net/profile/Mohammed-Y-Kamil")
    def tele1(self):
        webbrowser.open_new_tab("https://t.me/A97S21")
    def tele2(self):
        webbrowser.open_new_tab("https://t.me/m80y98")   
    def scholar(self):
        webbrowser.open_new_tab("")     
    def gmail1(self):
        webbrowser.open_new_tab("m80y98@uomustansiriyah.edu.iq")
    def gmail2(self):
        webbrowser.open_new_tab("ahd.sa.1997@gmail.com")

        
    

        
        

        
        
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()