from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import shutil


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        root.configure(background = '#fcd775')
        self.root.title("منظومة تمييز الاوجه")
        self.root.iconbitmap(r"C:/Users/ahmad/OneDrive/Desktop/thesis/attendance project/img/icons/scheduling.ico")

        
        
        
        
        #=====variables===========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        
        
        
        #image
        img1=Image.open(r"img\students data.jpg") 
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
        title_lbl=Label(bg_img,text="الطلبة بيانات ادارة منظومة",font=("times new roman",30,"bold","italic"),bg="#fcd775",fg="#0c1934",anchor='center')
        title_lbl.place(x=0,y=0,width=1530,height=50)
        
        main_frame=Frame(bg_img,bd=2,bg="#fcd775")
        main_frame.place(x=0,y=50,width=1530,height=740)
        
        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="#fcd775",fg="#0c1934",relief=RIDGE,text="الطالب معلومات",font=("times new roman",16,"bold"))
        Left_frame.place(x=10,y=0,width=730,height=600)
        
        
        img_left=Image.open(r"img\clg.jpg") 
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
    
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="#e2ac65",fg="#0c1934",relief=RIDGE,text="الحالي الكورس معلومات",font=("times new roman",16,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=115)
        
        
        #department
        dep_label=Label(current_course_frame,text=" : القسم",font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775',anchor='center')
        dep_label.grid(row=0,column=1,padx=10,sticky=W)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=20,state="read only",justify=RIGHT)
        dep_combo["values"]=("القسم","الفيزياء","الكيمياء","الاحياء","الرياضيات","علوم الجو","الحاسوب")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=0,padx=2,pady=10,sticky=W)
        
        
        #course
        course_label=Label(current_course_frame,text=": الدراسية المادة",font=("times new roman",13,"bold"),bg="#986b60",fg='#fcd775',anchor='center')
        course_label.grid(row=0,column=3,padx=0,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=20,state="read only",justify=RIGHT)
        course_combo["values"]=("المادة","معالجة الصور الرقمية","نانوتكنولوجي","بلازما","ثرموداينمك","كهربائية","بصريات","ليزر","علم مواد","فيزياء نووية","اطياف وجزيئية","ميكانيك","صلبة","كهرومغناطيسية","فيزياء رياضية")
        course_combo.current(0)
        course_combo.grid(row=0,column=2,padx=30,pady=10,sticky=W)
        
        
        #year
        year_label=Label(current_course_frame,text=": الدراسية السنة",font=("times new roman",13,"bold"),bg="#986b60",fg='#fcd775',anchor='center')
        year_label.grid(row=1,column=1,padx=10,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=20,state="read only",justify=RIGHT)
        year_combo["values"]=("الدراسية السنة اختر","23-2022","24-2023","25-2024","26-2025")
        year_combo.current(0)
        year_combo.grid(row=1,column=0,padx=2,pady=10,sticky=W)
        
        
        
        #semester
        semester_label=Label(current_course_frame,text=": الدراسي الفصل",font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775',anchor='center')
        semester_label.grid(row=1,column=3,padx=0,sticky=W)
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=20,state="read only",justify=RIGHT)
        semester_combo["values"]=("الدراسي الفصل اختر","الاول","الثاني")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=2,padx=30,pady=10,sticky=W)
        
        
        
        
        #class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="#e2ac65",fg="#0c1934",relief=RIDGE,text="الطالب معلومات",font=("times new roman",16,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=325)
        
        #studentID
        studentId_label=Label(class_student_frame,text=": للطالب التعريفية الهوية (ID)",font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775',anchor='center')
        studentId_label.grid(row=0,column=1,padx=10,sticky=W)
        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.va_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=0,padx=10,sticky=W)
        
        
        #student name
        studentName_label=Label(class_student_frame,text=": الطالب اسم",font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775',anchor='center')
        studentName_label.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        
        
        
        #class division
        class_div_label=Label(class_student_frame,text=" : الشعبة",font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775',anchor='center')
        class_div_label.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="read only",justify=RIGHT)
        div_combo["values"]=("الشعبة اختر","A","B","C","D","E")
        div_combo.current(0)
        div_combo.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        
        #Roll No
        roll_no_label=Label(class_student_frame,text=" : التسجيل  رقم",font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775',anchor='center')
        roll_no_label.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        roll_no_label_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_label_entry.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        
        #gender
        gender_label=Label(class_student_frame,text=" : الجنس",font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775',anchor='center')
        gender_label.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="read only",justify=RIGHT)
        gender_combo["values"]=("ذكر","انثى")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        
        #DOB
        dob_label=Label(class_student_frame,text=" : الميلاد تأريخ",font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775',anchor='center')
        dob_label.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        dob_label_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_label_entry.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        
        #Email
        email_label=Label(class_student_frame,text=" : الالكتروني البريد",font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775',anchor='center')
        email_label.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        email_label_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_label_entry.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        
        #phone no
        phone_label=Label(class_student_frame,text=" : الهاتف رقم",font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775',anchor='center')
        phone_label.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        phone_label_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_label_entry.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        
        #Adress
        adress_label=Label(class_student_frame,text=" :العنوان",font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775',anchor='center')
        adress_label.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        adress_label_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        adress_label_entry.grid(row=4,column=0,padx=10,pady=5,sticky=W) 
        
        
        #Doctor name
        teacher_label=Label(class_student_frame,text=" : الأُستاذ إسم",font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775',anchor='center')
        teacher_label.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        teacher_label_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_label_entry.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        
        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="اخذ نماذج من الصور",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="بدون الصور",value="No")
        radiobtn2.grid(row=6,column=1)
        
        #buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="#e2ac65")
        btn_frame.place(x=0,y=230,width=715,height=35)
        
        save_btn=Button(btn_frame,text="حفظ",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775')
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="تعديل",command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775')
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="حذف",command=self.delete_data,width=19,font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775')
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="ضبط إعادة",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775')
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="#986b60")
        btn_frame1.place(x=0,y=265,width=715,height=35)
        
        take_photo_btn=Button(btn_frame1,text="صور خذ",command=self.generate_dataset,width=39,font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775')
        take_photo_btn.grid(row=1,column=0)
        
        update_photo_btn=Button(btn_frame1,text="الصور حدث",command=self.generate_dataset,width=39,font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775')
        update_photo_btn.grid(row=1,column=1)
        
        
        
        
        
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="#fcd775",fg="#0c1934",relief=RIDGE,text="الطالب معلومات",font=("times new roman",16,"bold"))
        Right_frame.place(x=770,y=0,width=720,height=600)
        
        
        img_right=Image.open(r"img\100.png") 
        img_right=img_right.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
    
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        #======search system=================
        Search_frame=LabelFrame(Right_frame,bd=2,bg="#e2ac65",fg="#0c1934",relief=RIDGE,text="النظام في البحث",font=("times new roman",16,"bold"))
        Search_frame.place(x=5,y=135,width=710,height=70)
        
        search_label=Label(Search_frame,text=" : بواسطة البحث",font=("times new roman",15,"bold"),bg="#986b60",fg='#fcd775')
        search_label.grid(row=0,column=4,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=15,justify=RIGHT,state="read only")
        search_combo["values"]=("اختر","رقم التسجيل","رقم الهاتف")
        search_combo.current(0)
        search_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        search_btn=Button(Search_frame,text="بحث",width=12,font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775')
        search_btn.grid(row=0,column=1,padx=4)
        
        showAll_btn=Button(Search_frame,text="الكل اظهار",width=12,font=("times new roman",12,"bold"),bg="#986b60",fg='#fcd775')
        showAll_btn.grid(row=0,column=0,padx=4)
        #=======table frame=========
        table_frame=Frame(Right_frame,bd=2,bg="#fba342",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","ID","name","div","roll","gender","DOB","mail","phone","adress","teacher","image"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("dep",text="القسم")
        self.student_table.heading("course",text="المقرر الدراسي")
        self.student_table.heading("year",text="السنة")
        self.student_table.heading("sem",text="الفصل الدراسي")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("name",text="الاسم")
        self.student_table.heading("div",text="الشعبة")
        self.student_table.heading("DOB",text="تأريخ الميلاد")
        self.student_table.heading("mail",text="البريد الالكتروني")
        self.student_table.heading("phone",text="رقم الهاتف")
        self.student_table.heading("teacher",text="اسم الاستاذ")
        self.student_table.heading("image",text="الصورة")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("mail",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("adress",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("image",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    #=========function decration=======
      
    def add_data(self):
        if self.var_dep.get()=="القسم اختر" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
              messagebox.showerror("هناك خطأ ما          ","ربما تكون قد نسيت احد الحقول فارغاً",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="******",database="***********")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                               self.var_dep.get(),
                                                                                                               self.var_course.get(),
                                                                                                               self.var_year.get(),
                                                                                                               self.var_semester.get(),
                                                                                                               self.va_std_id.get(),
                                                                                                               self.var_std_name.get(),
                                                                                                               self.var_div.get(),
                                                                                                               self.var_roll.get(),
                                                                                                               self.var_gender.get(),
                                                                                                               self.var_dob.get(),
                                                                                                               self.var_email.get(),
                                                                                                               self.var_phone.get(),
                                                                                                               self.var_address.get(),
                                                                                                               self.var_teacher.get(),
                                                                                                               self.var_radio1.get(),
                                                                                                               
                                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("تمت العملية بنجاح","معلومات الطالب قد تم اضافتها بصورة صحيحة",parent=self.root)
            except Exception as es:
                messagebox.showerror("خطأ",f"Due To:{str(es)}",parent=self.root)
                
                
                
                
                
                
    #==========fetch data=============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="*********",database="*****")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
        
        #==========get cursor=============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
            
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),
            
    #======update function======
    def update_data(self):
        if self.var_dep.get()=="القسم اختر" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
              messagebox.showerror("هناك خطأ ما          ","ربما تكون قد نسيت احد الحقول فارغاً",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("تحديث","هل ترغب بتعديل بيانات هذا الطالب",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="**********",database="******")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                            self.var_radio1.get(),  
                                                                                                                                                                                            self.va_std_id.get(),
                                                                                                                                                                                       ))
                    
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("تمت العملية بنجاح","معلومات الطالب قد تم تحديثها بصورة صحيحة",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("خطا",f"Due To:{str(es)}",parent=self.root)
            
    #=========delete function
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("error","يجب ذكر الهوية التعريفية للطالب",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("حذف بيانات الطالب","هل ترغب بحذف بيانات هذا الطالب؟",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="**********",database="********")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                    shutil.rmtree(r'F:/attendance project/data/people\%s'%val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("حذف","تم حذف بيانات الطالب بنجاح",parent=self.root)
                    
            except Exception as es:
                messagebox.showerror("خطا",f"Due To:{str(es)}",parent=self.root)
                
    #reset
    def reset_data(self):
        self.var_dep.set("القسم")
        self.var_course.set("امادة")
        self.var_year.set("الدراسية السنة اختر")
        self.var_semester.set("الدراسي الفصل اختر")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("الشعبة اختر")
        self.var_roll.set("")
        self.var_gender.set("ذكر")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    
    #=============generate dataset=============
    def generate_dataset(self):
        if self.var_dep.get()=="القسم" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
              messagebox.showerror("هناك خطأ ما          ","ربما تكون قد نسيت احد الحقول فارغاً",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="********",database="*********")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                    if os.path.isdir(rf'data/people/{str(id)}')==False:
                        os.mkdir(rf'data/people/{str(id)}')
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                            self.var_radio1.get(),  
                                                                                                                                                                                            self.va_std_id.get()==id+1
                                                                                                                                                                                       ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #=====load predifiend data on face frontals from opencv====                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    my_frame = cv2.resize(my_frame, (1920,1080))
                    if not ret:
                        print("failed to grab frame")
                        break
                    cv2.imshow(u"الصور اخذ يتم",my_frame)
                    k = cv2.waitKey(1)
                    
                    if k%256 ==27:     #esc
                        print("Escape hit, closing the app")
                        break
                    
                    elif k%256 ==32:
                        file_name_path=(rf'data/people/{str(id)}/user.'+str(id)+"."+str(img_id)+".jpg")
                        cv2.imwrite(file_name_path,my_frame)
                        print("screenshot taken")
                        img_id+=1

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("النتيجة","تم انشاء قاعدة البيانات")
            except Exception as es:
                messagebox.showerror("خطا",f"Due To:{str(es)}",parent=self.root)
            
                
        
    
    
    
    
    
    
    
    
    
    
        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
