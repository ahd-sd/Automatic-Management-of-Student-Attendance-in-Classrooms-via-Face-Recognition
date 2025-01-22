from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import re
import mysql.connector
import pyttsx3

class Register():
    def __init__(self,root):
        self.root=root
        self.root.title('Register Page')
        self.root.geometry('1600x790+0+0')
        
        # text-to-speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[1].id)
        
        #variable
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.contact_var=StringVar()
        self.gender_var=StringVar()
        self.country_var=StringVar()
        self.id_var=StringVar()
        self.id_no_var=StringVar()
        self.password=StringVar()
        self.confirm_pass=StringVar()
        self.check_var=IntVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
               
        self.bg=ImageTk.PhotoImage(file=r'img/1111.jpg')
        bg_lbl=Label(self.root,image=self.bg,bd=2,relief=RAISED)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        # Images
        self.bg=ImageTk.PhotoImage(file=r'img/1111.jpg')
        bg_lbl=Label(self.root,image=self.bg,bd=2,relief=RAISED)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        logo_img=Image.open(r'img/icon.jpg')
        logo_img=logo_img.resize((60,60),Image.Resampling.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(logo_img)
        
        # Title frame
        title_frame=Frame(self.root,bd=1,relief=RIDGE)
        title_frame.place(x=450,y=28,width=550,height=82)
        title_lbl=Label(title_frame,image=self.photo_logo,compound=LEFT,text='استمارة تسجيل المستخدم',font=('times new roman',25,'bold'),fg='darkblue',bg='white')
        title_lbl.place(x=10,y=10)
        
        # information frame
        main_frame=Frame(self.root,bd=1,relief=RIDGE)
        main_frame.place(x=450,y=110,width=550,height=670)
        
        user_name=Label(main_frame,text=':اسم المستخدم',font=('times new roman',16,'bold'))
        user_name.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        user_entry=ttk.Entry(main_frame,textvariable=self.name_var,font=('times new roman',15,'bold'),width=25)
        user_entry.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        
        # Callback and validation register
        validate_name=self.root.register(self.checkname)
        user_entry.config(validate='key',validatecommand=(validate_name,'%P'))
        
        # Email
        email_lbl=Label(main_frame,text=":البريد الالكتروني",font=('times new roman',16,'bold'))
        email_lbl.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        txt_email=ttk.Entry(main_frame,textvariable=self.email_var,font=("times new roman",15),width=25)
        txt_email.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        
        # Conatact
        contactNo=Label(main_frame,text=":رقم الهاتف",font=('times new roman',16,'bold'))
        contactNo.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        entry_contact=ttk.Entry(main_frame,textvariable=self.contact_var,font=("times new roman",15),width=25)
        entry_contact.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        
        # Callback and validation register
        validate_contact=self.root.register(self.checkcontact)
        entry_contact.config(validate='key',validatecommand=(validate_contact,'%P'))
        
        # Gender
        gender_lbl=Label(main_frame,text=":الجنس",font=('times new roman',16,'bold'))
        gender_lbl.grid(row=3,column=1,padx=10,pady=10,sticky=W)
        gender_frame=Frame(main_frame)
        gender_frame.place(x=25,y=160,width=250,height=35)

        radio_male=Radiobutton(gender_frame,variable=self.gender_var,value='ذكر',text='ذكر',font=("times new roman",15))
        radio_male.grid(row=0,column=0,padx=10,pady=0,sticky=W)
        self.gender_var.set('ذكر')

        radio_female=Radiobutton(gender_frame,variable=self.gender_var,value='انثى',text='انثى',font=("times new roman",15))
        radio_female.grid(row=0,column=1,padx=10,pady=0,sticky=W)
        
        # Country

        selct_country=Label(main_frame,text=":اختر البلد",font=('times new roman',16,'bold'))
        selct_country.grid(row=4,column=1,padx=10,pady=10,sticky=W)
        list =['العراق','المملكة المتحدة','المكسيك','افغانستان','باكستان'];
        droplist=OptionMenu(main_frame,self.country_var, *list)
        droplist.config(width=21,font=("times new roman",15),bg='white')
        self.country_var.set('اختر بلدك')
        # # droplist.place(x=240,y=420)
        droplist.grid(row=4,column=0,padx=10,pady=10,sticky=W)
        
        
        # Id Type
        id_type=Label(main_frame,text=":اختر نوع الهوية التعريفية",font=('times new roman',16,'bold'))
        id_type.grid(row=5,column=1,padx=10,pady=10,sticky=W)
        self.combo_id_type=ttk.Combobox(main_frame,textvariable=self.id_var,font=("times new roman",15),justify='center',state="readonly",width=23)
        self.combo_id_type["values"]=("اختر هويتك التعريفية","بطاقة اذور","جواز سفر","رخصة قيادة")
        self.combo_id_type.grid(row=5,column=0,padx=10,pady=10)
        self.combo_id_type.current(0)

        # Id Number
        id_no=Label(main_frame,text=":ادخل رقم الهوية التعريفية",font=('times new roman',16,'bold'))
        id_no.grid(row=6,column=1,padx=10,pady=10,sticky=W)
        entry_id_no=ttk.Entry(main_frame,textvariable=self.id_no_var,font=("times new roman",15),width=25)
        entry_id_no.grid(row=6,column=0,padx=10,pady=10,sticky=W)

        # Password
        s_password=Label(main_frame,text=":كلمة المرور",font=('times new roman',16,'bold'))
        s_password.grid(row=7,column=1,padx=10,pady=10,sticky=W)
        entry_pass=ttk.Entry(main_frame,textvariable=self.password,font=("times new roman",15),width=25)
        entry_pass.grid(row=7,column=0,padx=10,pady=10,sticky=W)

        # Confirm Pasword
        c_password=Label(main_frame,text=":تأكيد كلمة المرور",font=('times new roman',16,'bold'))
        c_password.grid(row=8,column=1,padx=10,pady=10,sticky=W)
        entry_confirm=ttk.Entry(main_frame,textvariable=self.confirm_pass,font=("times new roman",15),width=25)
        entry_confirm.grid(row=8,column=0,padx=10,pady=10,sticky=W)

        # secqurity Q&A
        security_Q=Label(main_frame,text=":اختر سؤال الحماية",font=("times new roman",16,"bold"))
        security_Q.grid(row=9,column=1)
        
        self.combo_security_Q=ttk.Combobox(main_frame,textvariable=self.var_securityQ,font=("times new roman",16,"bold"),state="readonly",justify='center',width=21)
        self.combo_security_Q["values"]=("اختر","مكان ولادتك","اسم حبيبتك","اسم حيوانك المفضل")
        self.combo_security_Q.grid(row=9,column=0,padx=10,pady=10,sticky=W)
        self.combo_security_Q.current(0)

        self.txt_security=ttk.Entry(main_frame,textvariable=self.var_securityA,font=("times new roman",15),width=25)
        self.txt_security.grid(row=10,column=0,padx=10,pady=10,sticky=W)
        
        security_A=Label(main_frame,text=":جواب سؤال الحماية",font=("times new roman",15,"bold"))
        security_A.grid(row=10,column=1,padx=10,pady=10,sticky=W)
        

        
        # Check_frame
        check_frame=Frame(main_frame)
        check_frame.place(x=130,y=550,width=400,height=70)
        check_btn=Checkbutton(check_frame,variable=self.check_var,text='يرجى تعليم المربع للموافقة على الشروط 🥱',font=("times new roman",16),onvalue=1,offvalue=0)
        check_btn.grid(row=0,column=0,padx=10,sticky=W)
        self.check_lbl=Label(check_frame,text='',font=("arial",16),fg='red')
        self.check_lbl.grid(row=1,column=0,padx=10,sticky=W)

        # Button Frame
        btn_frame=Frame(main_frame)
        btn_frame.place(x=30,y=625,width=480,height=70)
        save_data=Button(btn_frame,text='حفظ',command=self.validation,font=("times new roman",16,'bold'),width=12,cursor='hand2',bg='blue',fg='white')
        save_data.grid(row=0,column=0,padx=1,sticky=W)

        verify_data=Button(btn_frame,command=self.verify_data,text='التحقق من البيانات',font=("times new roman",16,'bold'),width=12,cursor='hand2',bg='blue',fg='white')
        verify_data.grid(row=0,column=1,padx=1,sticky=W)

        clear_data=Button(btn_frame,command=self.clear_data,text='محو البيانات',font=("times new roman",16,'bold'),width=12,cursor='hand2',bg='blue',fg='white')
        clear_data.grid(row=0,column=2,padx=1,sticky=W)
        
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
            messagebox.showerror("نعتذر على ازعاجك",'من فضلك ادخل ارقام فقط')
            return False
        
    def checkpassword(self,password):
        if len(password)<=21:
            if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",password):
                return True
            else:
                messagebox.showinfo('غير متاح','ادخل كلمة مرور قوية (مثل:Ahmad@123)')
                return False
        else:
            messagebox.showerror('غير متاح',"لقد تجاوزت الحد المسموح به من الرموز")
            return False
        
    def checkemail(self,email):
        if len(email)>7:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                return True
            else:
                self.engine.say('invalid email enter valid user email (example:codewithAhmad97@gmail.com)')
                self.engine.runAndWait()
                messagebox.showwarning('تحذير','البريد الالكتروني غير متوفر، رجاءا قم بادخال بريدك الالكتروني (مثلا:codewithAhmad97@gmail.com)')
                return False
        else:
            self.engine.say('Email lenght is too small')
            self.engine.runAndWait()
            messagebox.showinfo('غير متاح','البريد الالكتروني قصير جدا')
            
    # Valiaadations
    def validation(self):
        if self.name_var.get()=='':
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
                    conn=mysql.connector.connect(host="localhost",user="root",password="*********",database="*********")
                    my_cursur=conn.cursor()
                    my_cursur.execute('insert into new_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                            self.name_var.get(),
                                                                                            self.email_var.get(),
                                                                                            self.contact_var.get(),
                                                                                            self.gender_var.get(),
                                                                                            self.country_var.get(),
                                                                                            self.id_var.get(),
                                                                                            self.id_no_var.get(),
                                                                                            self.password.get(),
                                                                                            self.var_securityQ.get(),
                                                                                            self.var_securityA.get(),
                                                                                        ))
                    conn.commit()
                    conn.close
                    messagebox.showinfo('تمت بنجاح',f'تم تسجيلك بنجاح اسمك:{self.name_var.get()} و كلمة المرور:{self.password.get()}')
                except Exception as es:
                    messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
        
        
    def verify_data(self):
        data = f'الاسم:{self.name_var.get()}\nEmail:{self.email_var.get()}\nرقم الهاتف:{self.contact_var.get()}\nالجنس:{self.gender_var.get()}\nالبلد:{self.country_var.get()}\nالهوية التعريفية:{self.id_var.get()}\nرقم الهوية التعريفية:{self.id_no_var.get()}\nكلمة المرور:{self.password.get()}\nسؤال الحماية:{self.var_securityQ.get()}\nجواب سؤال الحماية:{self.var_securityA.get()}'
        messagebox.showinfo('Details',data)
        
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
        
        
        
        
if __name__=='__main__':
    root=Tk()
    obj=Register(root)
    root.mainloop()
    
