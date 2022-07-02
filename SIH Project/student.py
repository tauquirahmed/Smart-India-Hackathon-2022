from logging import root
from multiprocessing import parent_process
from multiprocessing.context import set_spawning_popen
from os import stat
import statistics
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image, ImageTk
from numpy import save
from tkinter import messagebox
import pyodbc


class Student:
    def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Student Management System")

      # ============variables================
      self.var_studentname=StringVar()
      self.var_studentID=StringVar()
      self.var_gender=StringVar()
      self.var_Course=StringVar()
      self.var_Dept=StringVar()
      self.var_Year=StringVar()
      self.var_semester=StringVar()
      self.var_mob=StringVar()
      self.var_email=StringVar()


      #background Image
      img=Image.open(r"E:\SIH Project\Images\Background.jpg")
      img=img.resize((1530,790),Image.ANTIALIAS)
      self.photoimg=ImageTk.PhotoImage(img)

      bg_img=Label(self.root,image=self.photoimg)
      bg_img.place(x=0,y=0,width=1530,height=790)

      title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("Times New Roman", 30, "bold"), bg="darkblue", fg="white")
      title_lbl.place(x=0, y=0, width=1530, height=50)

      main_frame=Frame(bg_img, bd=2,bg="white")
      main_frame.place(x=10, y=55, width=1500, height=720)

      #Left Frame
      Left_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Student Details", font=("Times New Roman",15, "bold"))
      Left_frame.place(x=15, y=10, width=720, height=680)

      #Right Frame
      Right_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Student Details", font=("Times New Roman",15, "bold"))
      Right_frame.place(x=755, y=10, width=720, height=680)

      #Current Course Frame
      Currrent_Course_frame=LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE, text="Current Course Details", font=("Times New Roman",15, "bold"))
      Currrent_Course_frame.place(x=5, y=10, width=705, height=150)
      #department
      dep_label=Label(Currrent_Course_frame, text="Department", font=("Times New Roman",15, "bold"))
      dep_label.grid(row=0, column=0, padx=10, sticky=W)

      dep_combo=ttk.Combobox(Currrent_Course_frame,textvariable=self.var_Dept, font=("Times New Roman",15, "bold"), width=17, state="readonly")
      dep_combo["values"]=("Select Department", "CSBS", "IT", "ECE", "CSE")
      dep_combo.current(0)
      dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
      #course
      course_label=Label(Currrent_Course_frame,text="Course", font=("Times New Roman",15, "bold"))
      course_label.grid(row=0, column=2, padx=10)

      course_combo=ttk.Combobox(Currrent_Course_frame,textvariable=self.var_Course, font=("Times New Roman",15, "bold"), width=17, state="readonly")
      course_combo["values"]=("Select Course", "B.Tech", "B.Sc", "M.Tech", "M.Sc")
      course_combo.current(0)
      course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

      #department
      year_label=Label(Currrent_Course_frame, text="Year", font=("Times New Roman",15, "bold"))
      year_label.grid(row=1, column=0, padx=10, sticky=W)

      year_combo=ttk.Combobox(Currrent_Course_frame,textvariable=self.var_Year, font=("Times New Roman",15, "bold"), width=17, state="readonly")
      year_combo["values"]=("Select Year", "1st", "2nd", "3rd", "4th")
      year_combo.current(0)
      year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)
      #course
      semester_label=Label(Currrent_Course_frame, text="Semester", font=("Times New Roman",15, "bold"))
      semester_label.grid(row=1, column=2, padx=10)

      semester_combo=ttk.Combobox(Currrent_Course_frame, textvariable=self.var_semester,font=("Times New Roman",15, "bold"), width=17, state="readonly")
      semester_combo["values"]=("Select Semester", "1", "2", "3", "4", "5","6","7","8")
      semester_combo.current(0)
      semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

      #Student Information
      Student_Information_frame=LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE, text="Student Information", font=("Times New Roman",15, "bold"))
      Student_Information_frame.place(x=5, y=165, width=705, height=460)

      StudentId_label=Label(Student_Information_frame, text="Student Id", font=("Times New Roman",15, "bold"))
      StudentId_label.grid(row=0, column=0, padx=10,pady=10, sticky=W)

      StudentId_entry=ttk.Entry(Student_Information_frame,textvariable=self.var_studentID, width=50, font=("times new roman", 15, "bold"))
      StudentId_entry.grid(row=0, column=1, padx=10,pady=10, sticky=W)

      StudentName_label=Label(Student_Information_frame, text="Student Name", font=("Times New Roman",15, "bold"))
      StudentName_label.grid(row=1, column=0, padx=10,pady=10, sticky=W)

      StudentName_entry=ttk.Entry(Student_Information_frame, textvariable=self.var_studentname,width=50, font=("times new roman", 15, "bold"))
      StudentName_entry.grid(row=1, column=1, padx=10,pady=10, sticky=W)

      Gender_label=Label(Student_Information_frame, text="Gender", font=("Times New Roman",15, "bold"))
      Gender_label.grid(row=3, column=0, padx=10,pady=10, sticky=W)

      Gender_combo=ttk.Combobox(Student_Information_frame,textvariable=self.var_gender ,width=50, font=("times new roman", 15, "bold"), state="readonly")
      Gender_combo["values"]=("Select Gender", "Male", "Female", "Others")
      Gender_combo.grid(row=3, column=1, padx=10,pady=10, sticky=W)

      Contact_label=Label(Student_Information_frame, text="Contact Number", font=("Times New Roman",15, "bold"))
      Contact_label.grid(row=4, column=0, padx=10,pady=10, sticky=W)

      Contact_entry=ttk.Entry(Student_Information_frame,textvariable=self.var_mob ,width=50, font=("times new roman", 15, "bold"))
      Contact_entry.grid(row=4, column=1, padx=10,pady=10, sticky=W)

      Email_label=Label(Student_Information_frame, text="Email Id", font=("Times New Roman",15, "bold"))
      Email_label.grid(row=5, column=0, padx=10,pady=10, sticky=W)

      Email_entry=ttk.Entry(Student_Information_frame, textvariable=self.var_email,width=50, font=("times new roman", 15, "bold"))
      Email_entry.grid(row=5, column=1, padx=10,pady=10, sticky=W)

      #radiobuttons
      self.var_radiobtn1=StringVar()
      radiobtn1=ttk.Radiobutton(Student_Information_frame,variable=self.var_radiobtn1, text="Take Photo Sample)", value="Yes")
      radiobtn1.grid(row=6, column=0)

      radiobtn2=ttk.Radiobutton(Student_Information_frame,variable=self.var_radiobtn1, text="No Photo Sample)", value="No")
      radiobtn2.grid(row=6, column=1)

      #buttons Frame
      btn_frame=Frame(Student_Information_frame, bd=2, relief=RIDGE, bg="white")
      btn_frame.place(x=5, y=300, width=690, height=150)

      save_btn=Button(btn_frame,text="Save",command=self.add_data, width=29,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
      save_btn.grid(row=0, column=0)

      update_btn=Button(btn_frame,text="Update", width=29,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
      update_btn.grid(row=0, column=1)

      Delete_btn=Button(btn_frame,text="Delete", width=29,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
      Delete_btn.grid(row=1, column=0)

      Reset_btn=Button(btn_frame,text="Reset", width=29,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
      Reset_btn.grid(row=1, column=1)

      Take_Photo_Sample_btn=Button(btn_frame,text="Take Photo Sammple", width=29,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
      Take_Photo_Sample_btn.grid(row=2, column=0)

      Update_Photo_Sample_btn=Button(btn_frame,text="Update Photo Sample", width=29,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
      Update_Photo_Sample_btn.grid(row=2, column=1)

      #=============Search System================
      Search_frame=LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("Times New Roman", 15, "bold"))
      Search_frame.place(x=10, y=5, width=700, height=100)

      Search_label=Label(Search_frame, text="Search by", font=("Times New Roman",15, "bold"), bg="red", fg="white")
      Search_label.grid(row=0, column=0,padx=2, pady=10, sticky=W)

      search_combo=ttk.Combobox(Search_frame, font=("Times New Roman",15, "bold"), width=12, state="readonly")
      search_combo["values"]=("Select", "Name", "Student Id", "Mobile No.")
      search_combo.current(0)
      search_combo.grid(row=0, column=1,padx=2, pady=10, sticky=W)

      SearchEntry=ttk.Entry(Search_frame, width=18, font=("Times New Roman",15, "bold"))
      SearchEntry.grid(row=0, column=2,padx=2, pady=10, sticky=W)

      search_btn=Button(Search_frame,text="Search", width=12,font=("Times New Roman", 12, "bold"), bg="blue", fg="white")
      search_btn.grid(row=0, column=3, padx=2, pady=10)

      Showall_btn=Button(Search_frame,text="Show All", width=12,font=("Times New Roman", 12, "bold"), bg="blue", fg="white")
      Showall_btn.grid(row=0, column=4, padx=2, pady=10)

      #=============Table Frame==============
      Table_frame=Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
      Table_frame.place(x=10, y=110, width=700, height=500)

      scroll_x=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(Table_frame, orient=VERTICAL)

      self.student_table=ttk.Treeview(Table_frame,column=("StudentName", "StudentId","Gender", "Course", "Department", "Year", "Semester", "Mobile", "Email"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
      scroll_x.pack(side=BOTTOM, fill=X)
      scroll_y.pack(side=RIGHT, fill=Y)
      scroll_x.config(command=self.student_table.xview)
      scroll_y.config(command=self.student_table.yview)

      self.student_table.heading("StudentName", text="Student Name")
      self.student_table.heading("StudentId", text="Student Id")
      self.student_table.heading("Gender", text="Gender")
      self.student_table.heading("Course", text="Course")
      self.student_table.heading("Department", text="Department")
      self.student_table.heading("Year", text="Year")
      self.student_table.heading("Semester", text="Semester")
      self.student_table.heading("Mobile", text="Mobile No.")
      self.student_table.heading("Email", text="Email Id")

      self.student_table["show"]="headings"
      # self.student_table.column("StudentName", width=100)

      self.student_table.pack(fill=BOTH, expand=1)
      self.fetch_data()

    # =================Function================
    def add_data(self):
      if self.var_studentname.get()=="" or self.var_studentID.get()=="" or self.var_Dept.get()=="Select Department":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
      else:
        try: 
          conn=pyodbc.connect('Driver={SQL Server};' 'Server=LAPTOP-GK81QE41\SQLEXPRESS;' 'Database=SIH2022;' 'Trusted_Connection=yes;' )
          cursor = conn.cursor()
          cursor.execute("insert into student values(?,?,?,?,?,?,?,?,?)", (
            self.var_studentname.get(),
            self.var_studentID.get(),
            self.var_gender.get(),
            self.var_Course.get(),
            self.var_Dept.get(),
            self.var_Year.get(),
            self.var_semester.get(),
            self.var_mob.get(),
            self.var_email.get()
          ))
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Success", "Added Succesfully", parent=self.root)
        except Exception as es:
          messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    # ==============Fetch Data========================
    def fetch_data(self):
      conn=pyodbc.connect('Driver={SQL Server};' 'Server=LAPTOP-GK81QE41\SQLEXPRESS;' 'Database=SIH2022;' 'Trusted_Connection=yes;' )
      cursor = conn.cursor()
      cursor.execute("select * from student")
      data=cursor.fetchall()

      if len(data)!=0:
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
          self.student_table.insert('',END, values=i)
        conn.commit()
      conn.close()





if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
