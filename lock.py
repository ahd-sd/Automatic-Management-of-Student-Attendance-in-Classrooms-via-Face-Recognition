from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from student import Student     
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
import tkinter
import re
import pyttsx3


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window():
    def __init__(self,root):
        self.root=root
        self.root.title("تسجيل دخول للمنظومة")
        self.root.geometry("1550x800+0+0")
        self.root.iconbitmap(r"img/login.ico")
        
        self.bg=ImageTk.PhotoImage(file=r"img\lock.tif")
        lbl_bg=Label(self.root,bg='#62339D',image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="#121114")
        frame.place(x=950,y=240,width=600,height=600)
        
        img1=Image.open(r"img\images.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoImage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoImage1,bg="#121114",borderwidth=0)
        lblimg1.place(x=1220,y=230,width=100,height=100)
        
        get_str=Label(frame,text="اذا كنت احد المسؤولين، يرجى تسجيل الدخول",font=("lemonada",15,"bold"),fg="#F9F7F7",bg="#121114")
        get_str.place(x=25,y=100)
        
        
        #label
        
        username=lbl=Label(frame,text="اسم المستخدم",font=("lemonada",15,"bold"),fg="#F9F7F7",bg="#121114")
        username.place(x=380,y=160)
        
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=287,y=200,width=270,height=30)
        
        password=lbl=Label(frame,text="كلمة المرور",font=("lemonada",15,"bold"),fg="#F9F7F7",bg="#121114")
        password.place(x=410,y=235)
        
        self.txtpass=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
        self.txtpass.place(x=287,y=280,width=270,height=30)
        
        
        
        
        #======icon images===========
        img2=Image.open(r"img\user.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoImage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoImage2,bg="#121114",borderwidth=0)
        lblimg1.place(x=1300,y=410,width=25,height=25)
        
        
        img3=Image.open(r"img\images.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoImage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoImage3,bg="#121114",borderwidth=0)
        lblimg1.place(x=1325,y=490,width=25,height=25)
        
        #loginbutton
        loginbtn=Button(frame,text="تسجيل الدخول",command=self.login,font=("lemonada",15,"bold"),bd=3,relief=RIDGE,fg="#F9F7F7",bg="#FDDD0D",activeforeground="#f7d944",activebackground="#202223")
        loginbtn.place(x=350,y=330,width=200,height=55)
        
        
        #regiserationbutton
        registerbtn=Button(frame,text="مستخدم جديد",command=self.register_window,borderwidth=0,font=("lemonada",12,"bold"),fg="#F9F7F7",bg="#FDDD0D",activeforeground="#a8b0c1",activebackground="#fef23d")
        registerbtn.place(x=350,y=420,width=200,height=55)
        
        #forgetpassbtn
        registerbtn=Button(frame,text="هل نسيت كلمة السر؟",command=self.forgot_password_window,borderwidth=0,font=("lemonada",12,"bold"),fg="#F9F7F7",bg="#FDDD0D",activeforeground="#a8b0c1",activebackground="#fef23d")
        registerbtn.place(x=335,y=500,width=215,height=55)
        
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("خطا","كل الحقول مطلوبة")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("تم","اهلا بكم يم احمد")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="******",database="********")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from new_table where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                
                                                                           ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("خطأ","اسم المستخدم او كلمة المرور ليست صحيحة")
            else:
                open_main=messagebox.askyesno("نعم او لا","الدخول للمسؤول فقط")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    def reset_pass(self):

        if self.combo_security_Q.get()=="اختر":
            messagebox.showerror("خطأ","من فضلك، اختر سؤال الحماية",parent=self.root2)

        elif self.txt_security.get()=="":
            messagebox.showerror("خطأ","رجاءا ادخل الاجابة على سؤال الحماية",parent=self.root2)

        elif self.txt_newpass.get()=="":
            messagebox.showerror("خطأ","من فضلك، ادخل كلمة السر الجديدة",parent=self.root2)

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="******",database="*******")
            my_cursor=conn.cursor()
            qury=("select * from new_table where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("خطأ","من فضلك، ادخل الاجابة الصحيحة",parent=self.root2)
            else:
                query=("update new_table set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("تم","تم تغيير كلمة المرور، قم بتسجيل الدخول باستخدام كلمة المرور الجديدة من فضلك",parent=self.root2)
                self.root2.destroy()


    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("خطأ","ادخل عنوان البريد الالكتروني لاعادة ضبط كلمة المرور")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="********",database="*********")
            my_cursor=conn.cursor()
            query=("select * from new_table where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("خطأ","رجاءا ادخل البريد الالكتروني بصورة صحيحة")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("نسيان كلمة المرور")
                self.root2.geometry("340x450+440+340")
                l=Label(self.root2,text="اعادة ضبط كلمة المرور",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="اختر سؤال الحماية",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=170,y=50)
                
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),justify='center',state="readonly")
                self.combo_security_Q["values"]=("اختر","مكان ولادتك","فريقك الرياضي المفضل","لغتك البرمجية المفضلة","اسم الشخص الاقرب لقلبك","اسم حيوانك المفضل")
                self.combo_security_Q.place(x=50,y=80,width=250)
                self.combo_security_Q.current(0)
                
                security_A=Label(self.root2,text="جواب سؤال الحماية",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=170,y=120)
                
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=150,width=250)

                new_password=Label(self.root2,text="كلمة المرور الجديدة",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=170,y=190)
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=220,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="White",bg="green")
                btn.place(x=190, y=400)

         
            
            
            
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('Register Page')
        self.root.geometry('1600x790+0+0')
        root.configure(bg='#893376')
        self.root.iconbitmap(r"img/login.ico")
        
        # text-to-speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[1].id)
        
        #variable
        self.name_var=StringVar()
        self.contact_var=StringVar()
        self.gender_var=StringVar()
        self.country_var=StringVar()
        self.id_var=StringVar()
        self.id_no_var=StringVar()
        self.email_var=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.password=StringVar()
        self.confirm_pass=StringVar()
        self.check_var=IntVar()
        self.var_admin=StringVar()
        
               

        # Images

        logo_img=Image.open(r'img/icon.png')
        logo_img=logo_img.resize((60,60),Image.Resampling.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(logo_img)
        
        # Title frame
        title_frame=Frame(self.root,bg='#fcf6df',bd=1,relief=RIDGE)
        title_frame.place(x=450,y=5,width=650,height=82)
        title_lbl=Label(title_frame,image=self.photo_logo,compound=LEFT,text='استمارة تسجيل المستخدم',font=('times new roman',25,'bold'),fg='#fbc24f',bg='#fcf6df')
        title_lbl.place(x=120,y=10)
        
        # information frame
        main_frame=Frame(self.root,bg='#0b0307',bd=1,relief=RIDGE)
        main_frame.place(x=450,y=87,width=650,height=720)
        
        user_name=Label(main_frame,text=':اسم المستخدم',font=('times new roman',16,'bold'),bg='#0b0307',fg='#d8df5a')
        user_name.place(x=400,y=5)
        user_entry=ttk.Entry(main_frame,textvariable=self.name_var,font=('times new roman',15,'bold'),width=25)
        user_entry.place(x=115,y=5)
        
        # Callback and validation register
        validate_name=self.root.register(self.checkname)
        user_entry.config(validate='key',validatecommand=(validate_name,'%P'))
        
        # Email
        email_lbl=Label(main_frame,text=":البريد الالكتروني",font=('times new roman',16,'bold'),bg='#0b0307',fg='#d8df5a')
        email_lbl.place(x=400,y=55)
        txt_email=ttk.Entry(main_frame,textvariable=self.email_var,font=("times new roman",15),width=25)
        txt_email.place(x=115,y=55)
        
        # Conatact
        contactNo=Label(main_frame,text=":رقم الهاتف",font=('times new roman',16,'bold'),bg='#0b0307',fg='#d8df5a')
        contactNo.place(x=400,y=105)
        entry_contact=ttk.Entry(main_frame,textvariable=self.contact_var,font=("times new roman",15),width=25)
        entry_contact.place(x=115,y=105)
        
        # Callback and validation register
        validate_contact=self.root.register(self.checkcontact)
        entry_contact.config(validate='key',validatecommand=(validate_contact,'%P'))
        
        # Gender
        gender_lbl=Label(main_frame,text=":الجنس",font=('times new roman',16,'bold'),bg='#0b0307',fg='#d8df5a')
        gender_lbl.place(x=400,y=155)
        gender_frame=Frame(main_frame,bg='#0b0307')
        gender_frame.place(x=115,y=155,width=250,height=35)

        radio_male=Radiobutton(gender_frame,variable=self.gender_var,value='ذكر',text='ذكر',font=("times new roman",15),bg='#0b0307',fg='#d8df5a')
        radio_male.grid(row=0,column=0,padx=20,pady=0,sticky=W)
        self.gender_var.set('ذكر')

        radio_female=Radiobutton(gender_frame,variable=self.gender_var,value='انثى',text='انثى',font=("times new roman",15),bg='#0b0307',fg='#d8df5a')
        radio_female.grid(row=0,column=1,padx=20,pady=0,sticky=W)
        
        # Country

        selct_country=Label(main_frame,text=":اختر البلد",font=('times new roman',16,'bold'),bg='#0b0307',fg='#d8df5a')
        selct_country.place(x=400,y=190)
        list =['العراق','المملكة المتحدة','المكسيك','افغانستان','باكستان'];
        droplist=OptionMenu(main_frame,self.country_var, *list)
        droplist.config(width=21,font=("times new roman",15),bg='#0b0307',fg='#d8df5a')
        self.country_var.set('اختر بلدك')
        droplist.place(x=115,y=190)
        
        
        # Id Type
        id_type=Label(main_frame,text=":اختر نوع الهوية التعريفية",font=('times new roman',16,'bold'),bg='#0b0307',fg='#d8df5a')
        id_type.place(x=400,y=240)
        self.combo_id_type=ttk.Combobox(main_frame,textvariable=self.id_var,font=("times new roman",15),justify='center',state="readonly",width=23)
        self.combo_id_type["values"]=("اختر هويتك التعريفية","بطاقة الاحوال المدنية","جواز سفر","رخصة قيادة","البطاقة الوطنية")
        self.combo_id_type.place(x=115,y=240)
        self.combo_id_type.current(0)

        # Id Number
        id_no=Label(main_frame,text=":ادخل رقم الهوية التعريفية",font=('times new roman',16,'bold'),bg='#0b0307',fg='#d8df5a')
        id_no.place(x=400,y=290)
        entry_id_no=ttk.Entry(main_frame,textvariable=self.id_no_var,font=("times new roman",15),width=25)
        entry_id_no.place(x=115,y=290)

        # Password
        s_password=Label(main_frame,text=":كلمة المرور",font=('times new roman',16,'bold'),bg='#0b0307',fg='#d8df5a')
        s_password.place(x=400,y=340)
        entry_pass=ttk.Entry(main_frame,show="*",textvariable=self.password,font=("times new roman",15),width=25)
        entry_pass.place(x=115,y=340)

        # Confirm Pasword
        c_password=Label(main_frame,text=":تأكيد كلمة المرور",font=('times new roman',16,'bold'),bg='#0b0307',fg='#d8df5a')
        c_password.place(x=400,y=390)
        entry_confirm=ttk.Entry(main_frame,show="*",textvariable=self.confirm_pass,font=("times new roman",15),width=25)
        entry_confirm.place(x=115,y=390)

        # secqurity Q&A
        security_Q=Label(main_frame,text=":اختر سؤال الحماية",font=("times new roman",16,"bold"),bg='#0b0307',fg='#d8df5a')
        security_Q.place(x=400,y=440)
        
        self.combo_security_Q=ttk.Combobox(main_frame,textvariable=self.var_securityQ,font=("times new roman",16,"bold"),state="readonly",justify='center',width=21)
        self.combo_security_Q["values"]=("اختر","مكان ولادتك","فريقك الرياضي المفضل","لغتك البرمجية المفضلة","اسم الشخص الاقرب لقلبك","اسم حيوانك المفضل")
        self.combo_security_Q.place(x=115,y=440)
        self.combo_security_Q.current(0)

        self.txt_security=ttk.Entry(main_frame,textvariable=self.var_securityA,font=("times new roman",15),width=25)
        self.txt_security.place(x=115,y=490)
        
        security_A=Label(main_frame,text=":جواب سؤال الحماية",font=("times new roman",15,"bold"),bg='#0b0307',fg='#d8df5a')
        security_A.place(x=400,y=490)

        self.abc_admin=ttk.Entry(main_frame,textvariable=self.var_admin,font=("times new roman",15),width=25)
        self.abc_admin.place(x=115,y=540)
        
        admin=Label(main_frame,text=":كلمة المرور لمسؤول التسجيل",font=("times new roman",15,"bold"),bg='#0b0307',fg='#d8df5a')
        admin.place(x=400,y=540)
        

        
        # Check_frame
        check_frame=Frame(main_frame,bg='#0b0307')
        check_frame.place(x=130,y=590,width=400,height=70)
        check_btn=Checkbutton(check_frame,variable=self.check_var,text='يرجى تعليم المربع للموافقة على الشروط',font=("times new roman",16),bg='#0b0307',fg='#d8df5a',onvalue=1,offvalue=0)
        check_btn.grid(row=0,column=0,padx=10,sticky=W)
        self.check_lbl=Label(check_frame,text='',font=("arial",16),bg='#0b0307',fg='red')
        self.check_lbl.grid(row=1,column=0,padx=10,sticky=W)

        # Button Frame
        btn_frame=Frame(main_frame)
        btn_frame.place(x=0,y=675,width=650,height=70)
        save_data=Button(btn_frame,text='حفظ',command=self.validation,font=("times new roman",16,'bold'),width=11,cursor='hand2',bg='#fcf6df',fg='#fbc24f')
        save_data.grid(row=0,column=0,padx=1,sticky=W)

        verify_data=Button(btn_frame,command=self.verify_data,text='التحقق من البيانات',font=("times new roman",16,'bold'),width=11,cursor='hand2',bg='#fcf6df',fg='#fbc24f')
        verify_data.grid(row=0,column=1,padx=1,sticky=W)

        clear_data=Button(btn_frame,command=self.clear_data,text='محو البيانات',font=("times new roman",16,'bold'),width=11,cursor='hand2',bg='#fcf6df',fg='#fbc24f')
        clear_data.grid(row=0,column=2,padx=1,sticky=W)

        back_2login=Button(btn_frame,command=self.return_login,text='العودة الى صفحة تسجيل الدخول',font=("times new roman",15,'bold'),width=17,cursor='hand2',bg='#fcf6df',fg='#fbc24f')
        back_2login.grid(row=0,column=3,padx=1,sticky=W)
        
        # Call back Function
    def checkname(self,name):
        if name.isalnum():
            return True
        if name=='':
            return True
        else:
            messagebox.showerror('غير متاح','غير مسموح'+name[-1])       
    # checkcontact
    def checkcontact(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return True
        else:
            messagebox.showerror("نعتذر على ازعاجك",'من فضلك، ادخل رقم هاتف صالح')
            return False
        
    def checkpassword(self,password):
        if len(password)<=21:
            if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",password):
                return True
            else:
                messagebox.showinfo('نعتذر على ازعاجك','ادخل كلمة مرور قوية (مثل:Ahmad@123)')
                return False
        else:
            messagebox.showerror('نعتذر على ازعاجك',"لقد تجاوزت الحد المسموح به من الرموز")
            return False
        
    def checkemail(self,email):
        if len(email)>7:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                return True
            else:
                self.engine.say('invalid email enter valid user email (example:codewithAhmad97@gmail.com)')
                self.engine.runAndWait()
                messagebox.showwarning('تحذير','البريد الالكتروني غير متوفر، رجاءا قم بادخال بريدك الالكتروني (مثلا:codewithAhmad@gmail.com)')
                return False
        else:
            self.engine.say('Email lenght is too small')
            self.engine.runAndWait()
            messagebox.showinfo('غير متاح','البريد الالكتروني قصير جدا')
            
    # Valiaadations
    def validation(self):
        if self.var_admin.get()=='':
            self.engine.say('if you are the adminstrator, please enter the password of the admins')
            self.engine.runAndWait()
            messagebox.showerror('نعتذر على ازعاجك','ادخل كلمة المرور من فضلك',parent=self.root)
        elif self.name_var.get()=='':
            self.engine.say('Please enter your name')
            self.engine.runAndWait()
            messagebox.showerror('حطا','رجاءا قم بادخال اسمك',parent=self.root)
        elif self.email_var.get()=='': 
            self.engine.say('Please enter your email id')
            self.engine.runAndWait()
            messagebox.showerror('خطا','رجاءا قم بادخال بريدك الالكتروني',parent=self.root)
            
        elif self.contact_var.get()=='' or len(self.contact_var.get())!=11:
            self.engine.say('Please enter your Valid Contact')
            self.engine.runAndWait()
            messagebox.showerror('خطأ','رجاءا قم بادخال رقم هاتف صالح',parent=self.root)
        elif self.gender_var.get()=='':
            self.engine.say('Please select your gender')
            self.engine.runAndWait()
            messagebox.showerror('خطأ','قم باختيار جنسك من فضلك',parent=self.root)
        elif self.country_var.get()=='' or self.country_var.get()=='اختر بلدك':
            self.engine.say('Please select your country')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please select your county',parent=self.root)
        elif self.id_var.get()=='اختر هويتك التعريفية':
            self.engine.say('Please selct your id Type')
            self.engine.runAndWait()
            messagebox.showerror('خطأ','من فضلك، اختر نوع هويتك التعريفية',parent=self.root)
        elif self.id_no_var.get()=='':
            self.engine.say('Please enter your id number')
            self.engine.runAndWait()
            messagebox.showerror('خطأ','رجاءا قم بادخال رقم هويتك التعريفية',parent=self.root)
        elif len(self.id_no_var.get())!=14:
            messagebox.showerror('خطأ','رجاءا قم بادخال 14 رقم',parent=self.root)
        elif self.password.get()=='':
            self.engine.say('Please enter your Password')
            self.engine.runAndWait()
            messagebox.showerror('خطأ','رجاءا، ادخل كلمة مرورك',parent=self.root)
        elif self.confirm_pass.get()=='':
            messagebox.showerror('خطأ','رجاءا اكد كلمة مرورك',parent=self.root)
        elif self.password.get()!= self.confirm_pass.get():
            self.engine.say('Password & Confirm password must be same')
            self.engine.runAndWait()
            messagebox.showerror('خطأ','كلمة المرور يجب ان تكون نفس كلمة التأكيد',parent=self.root)
        elif self.var_securityQ.get()=='اختر':
            self.engine.say('Please selct your security question Type')
            self.engine.runAndWait()
            messagebox.showerror('خطأ','من فضلك، اختر نوع سؤال الحماية الخاص بك',parent=self.root)
        elif self.var_securityA.get()=='':
            self.engine.say('Please enter your security answer')
            self.engine.runAndWait()
            messagebox.showerror('خطأ','رجاءا قم بادخال جوابك على سؤال الحماية',parent=self.root)
        elif self.var_admin.get()!='******':
            self.engine.say('you do not have the permission to register a new aminstrators')
            self.engine.runAndWait()
            messagebox.showerror('نعتذر على ازعاجك','😔على ما يبدو انك لا تمتلك صلاحية اضافة مشرفين جدد',parent=self.root)
        
        
        elif self.email_var.get()!=None and self.password.get()!=None:
            X=self.checkemail(self.email_var.get())
            Y=self.checkpassword(self.password.get())
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="*********",database="******")
            my_cursor=conn.cursor()
            query=("select * from new_table where email=%s")
            value=(self.email_var.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("خطأ","المستخدم موجود")

        if (X == True) and (Y == True):
            if self.check_var.get()==0:
                self.engine.say('Please Agree Our terms & Conditions')
                self.engine.runAndWait()
                self.check_lbl.config(text='وافق على شروطنا',fg='red')
            else:
                self.check_lbl.config(text='تمت الموافقة',fg='green')
                
                try:
                    conn=mysql.connector.connect(host="localhost",user="root",password="*****",database="*******")
                    my_cursur=conn.cursor()
                    my_cursur.execute('insert into new_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                            self.name_var.get(),
                                                                                            self.contact_var.get(),
                                                                                            self.gender_var.get(),
                                                                                            self.country_var.get(),
                                                                                            self.id_var.get(),
                                                                                            self.id_no_var.get(),
                                                                                            self.email_var.get(),
                                                                                            self.var_securityQ.get(),
                                                                                            self.var_securityA.get(),
                                                                                            self.password.get(),
                                                                                            
                                                                                        ))
                    conn.commit()
                    conn.close
                    messagebox.showinfo('تمت بنجاح',f'تم تسجيلك بنجاح اسمك:{self.name_var.get()} و كلمة المرور:{self.password.get()}',parent=self.root)
                except Exception as es:
                    messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
        
        
    def verify_data(self):
        data = f'الاسم:{self.name_var.get()}\nEmail:{self.email_var.get()}\nرقم الهاتف:{self.contact_var.get()}\nالجنس:{self.gender_var.get()}\nالبلد:{self.country_var.get()}\nالهوية التعريفية:{self.id_var.get()}\nرقم الهوية التعريفية:{self.id_no_var.get()}\nكلمة المرور:{self.password.get()}\nسؤال الحماية:{self.var_securityQ.get()}\nجواب سؤال الحماية:{self.var_securityA.get()}'
        messagebox.showinfo('Details',data,parent=self.root)
        
    def clear_data(self):
        
       self.name_var.set('')
       self.email_var.set('')
       self.contact_var.set('')
       self.gender_var.set('ذكر')
       self.country_var.set('بلدك')
       self.id_var.set('اختر هويتك التعريفية')
       self.id_no_var.set('')
       self.password.set('')
       self.confirm_pass.set('')
       self.check_var.set(0)
       self.var_securityQ.set('اختر')
       self.var_securityA.set('')
       self.var_admin.set('')


    def return_login(self):
        self.root.destroy()

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
            
            
            
                    
                
        
        
if __name__=="__main__":
    main()


    
    
