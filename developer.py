from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("منظومة تمييز الاوجه")
        self.root.iconbitmap(r"C:/Users/ahmad/OneDrive/Desktop/thesis/attendance project/img/icons/contact_us.ico")
        img1=Image.open(r"img\guide.jpg") 
        img1=img1.resize((1530,790),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
    
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=1530,height=790)

        
        
        

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()