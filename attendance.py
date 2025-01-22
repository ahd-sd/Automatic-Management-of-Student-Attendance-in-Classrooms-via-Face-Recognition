from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("منظومة تمييز الاوجه")
        self.root.iconbitmap(r"img/icons/attendant_list.ico")

        
        
        #=======variables==========
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        self.var_atten_subject=StringVar()

        
        
        
        #image
        img1=Image.open(r"C:\Users\ahmad\Desktop\Desktop\designs\atten.jpg") 
        img1=img1.resize((1600,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
    
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=1600,height=200)

        #big image
        img3=Image.open(r"img\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg") 
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)
        
        
        #the label
        title_lbl=Label(bg_img,text="ادارة حضور الطلبة",font=("Calibri",30,'bold'),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=55)
        
        main_frame=Frame(bg_img,bd=2,bg="#00FFFF")
        main_frame.place(x=0,y=50,width=1530,height=740)
        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="تفاصيل الطلبة الحاضرين",font=("Calibri",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)
        img_left=Image.open(r"img\clg.jpg") 
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
    
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)
        
        #Labelland entry
        #student id
        attendanceId_label=Label(left_inside_frame,text=": رقم التسجيل",font=("Amiri",13,'bold'),bg="white")
        attendanceId_label.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        attendanceId_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        attendanceId_entry.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        # roll
        roolLabel=Label(left_inside_frame,text=": الاسم",font=("Amiri",13,'bold'),bg="white")
        roolLabel.grid(row=0,column=3,padx=4,pady=8,sticky=W)
        atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        atten_roll.grid(row=0,column=2,padx=8,sticky=W)
        
        #name
        nameLabel=Label(left_inside_frame,text=": القسم",font=("Amiri",13,'bold'),bg="white")
        nameLabel.grid(row=1,column=1)
        atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        atten_name.grid(row=1,column=0,pady=8)
        
        #Dep
        depLabel=Label(left_inside_frame,text=": الوقت",font=("Amiri",13,'bold'),bg="white")
        depLabel.grid(row=1,column=3)
        atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        atten_dep.grid(row=1,column=2,pady=8)
        
        #time
        timeLabel=Label(left_inside_frame,text=": التاريخ",font=("Amiri",13,'bold'),bg="white")
        timeLabel.grid(row=2,column=1)
        atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        atten_time.grid(row=2,column=0,pady=8)
        
        #Date
        dateLabel=Label(left_inside_frame,text=": حالة الحضور",font=("Amiri",13,'bold'),bg="white")
        dateLabel.grid(row=2,column=3)
        self.atten_status=ttk.Combobox(left_inside_frame,text="Attendance Status",width=22,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),justify='right')
        self.atten_status["values"]=("الحالة","حاضر","غائب")
        self.atten_status.grid(row=2,column=2,pady=8)
        self.atten_status.current(0)
        
        
        #attendance
        attendanceLabel=Label(left_inside_frame,text=": المادة",font=("Amiri",13,'bold'),bg="white")
        attendanceLabel.grid(row=3,column=1)
        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_subject,font=("times new roman",13,"bold"))
        atten_date.grid(row=3,column=0,pady=8)
        
        
        
        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)
        
        save_btn=Button(btn_frame,text="csv استيراد",command=self.importCsv,width=19,font=("Calibri",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="csv تصدير",command=self.exportCsv,width=19,font=("Calibri",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="تحديث",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="اعادة ضبط",width=19,command=self.reset_data,font=("Calibri",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        
        
        
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="جدول بتفاصيل الحاضرين",font=("Calibri",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)
        
        
        img_right=Image.open(r"img\100.png") 
        img_right=img_right.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)
        
        #==============scroll bar table======
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("roll","name","department","time","date","attendance","subject"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("roll",text="رقم التسجيل")
        self.AttendanceReportTable.heading("name",text="الاسم")
        self.AttendanceReportTable.heading("department",text="القسم")
        self.AttendanceReportTable.heading("time",text="الوقت")
        self.AttendanceReportTable.heading("date",text="التاريخ")
        self.AttendanceReportTable.heading("attendance",text="حالة الحضور")
        self.AttendanceReportTable.heading("subject",text="المادة")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        self.AttendanceReportTable.column("subject",width=100)

        
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    #==========fetch data==========
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #import csv        
    def importCsv(self):
        global mydata
        mydata.clear()    #to clear the data when we do importing
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln,encoding="utf8") as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to " +os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("خطأ",f"Due To:{str(es)}",parent=self.root)
                
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_roll.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_dep.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_attendance.set(rows[5])
        self.var_atten_subject.set(rows[6])
        
        
    def reset_data(self):
        self.var_atten_subject.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
        
            
        
            
        
        
        
        
        














if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
