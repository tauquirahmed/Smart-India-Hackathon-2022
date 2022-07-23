from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
import cv2
import numpy as np
from tkinter import messagebox
import mysql.connector


class Face_Recognition_System:
    def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition System With AI Thermometer")

      #background Image
      img=Image.open(r"E:\SIH Project\Images\Background.jpg")
      img=img.resize((1530,790),Image.ANTIALIAS)
      self.photoimg=ImageTk.PhotoImage(img)

      bg_img=Label(self.root,image=self.photoimg)
      bg_img.place(x=0,y=0,width=1530,height=790)

      title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDACE SYSTEM WITH AI THERMOMETER", font=("Times New Roman", 30, "bold"), bg="white", fg="red")
      title_lbl.place(x=0, y=0, width=1530, height=50)

      #student button
      img1=Image.open(r"E:\SIH Project\Images\Student_details.jpg")
      img1=img1.resize((320,320),Image.ANTIALIAS)
      self.photoimg1=ImageTk.PhotoImage(img1)

      b1=Button(bg_img, image=self.photoimg1,command=self.student_details, cursor="hand2")
      b1.place(x=200, y=100, width=220, height=220)

      b1_1=Button(bg_img,text="Student Details",command=self.student_details,
      cursor="hand2", font=("Times New Roman",15,"bold"),bg="darkblue", fg="white")
      b1_1.place(x=200,y=300,width=220, height=40)

      #Detect Face
      img2=Image.open(r"E:\SIH Project\Images\Detect_Face.jpg")
      img2=img2.resize((220,220),Image.ANTIALIAS)
      self.photoimg2=ImageTk.PhotoImage(img2)

      b2=Button(bg_img, image=self.photoimg2, cursor="hand2")
      b2.place(x=500, y=100, width=220, height=220)

      b2_1=Button(bg_img,text="Detect Face", command=self.face_recog,cursor="hand2", font=("Times New Roman",15,"bold"),bg="darkblue", fg="white")
      b2_1.place(x=500,y=300,width=220, height=40)

      #Mark Attendance
      img3=Image.open(r"E:\SIH Project\Images\Mark_Attendance.png")
      img3=img3.resize((220,220),Image.ANTIALIAS)
      self.photoimg3=ImageTk.PhotoImage(img3)

      b3=Button(bg_img, image=self.photoimg3, cursor="hand2")
      b3.place(x=800, y=100, width=220, height=220)

      b3_1=Button(bg_img,text="Mark Attendance", cursor="hand2", font=("Times New Roman",15,"bold"),bg="darkblue", fg="white")
      b3_1.place(x=800,y=300,width=220, height=40)

      #Help
      img4=Image.open(r"E:\SIH Project\Images\Help.png")
      img4=img4.resize((220,220),Image.ANTIALIAS)
      self.photoimg4=ImageTk.PhotoImage(img4)

      b4=Button(bg_img, image=self.photoimg4, cursor="hand2")
      b4.place(x=1100, y=100, width=220, height=220)

      b4_1=Button(bg_img,text="Help", cursor="hand2", font=("Times New Roman",15,"bold"),bg="darkblue", fg="white")
      b4_1.place(x=1100,y=300,width=220, height=40)

      #Train Data
      img5=Image.open(r"E:\SIH Project\Images\Train.png")
      img5=img5.resize((220,220),Image.ANTIALIAS)
      self.photoimg5=ImageTk.PhotoImage(img5)

      b5=Button(bg_img, image=self.photoimg5, command=self.train_classifier,cursor="hand2")
      b5.place(x=200, y=400, width=220, height=220)

      b5_1=Button(bg_img,text="Train Data", command=self.train_classifier,cursor="hand2", font=("Times New Roman",15,"bold"),bg="darkblue", fg="white")
      b5_1.place(x=200,y=600,width=220, height=40)

      #Photos
      img6=Image.open(r"E:\SIH Project\Images\photos.jpg")
      img6=img6.resize((220,220),Image.ANTIALIAS)
      self.photoimg6=ImageTk.PhotoImage(img6)

      b6=Button(bg_img, image=self.photoimg6, command=self.open_img,cursor="hand2")
      b6.place(x=500, y=400, width=220, height=220)

      b6_1=Button(bg_img,text="Photos",command=self.open_img, cursor="hand2", font=("Times New Roman",15,"bold"),bg="darkblue", fg="white")
      b6_1.place(x=500,y=600,width=220, height=40)

      #Developer
      img7=Image.open(r"E:\SIH Project\Images\Developer.png")
      img7=img7.resize((220,220),Image.ANTIALIAS)
      self.photoimg7=ImageTk.PhotoImage(img7)

      b7=Button(bg_img, image=self.photoimg7, cursor="hand2")
      b7.place(x=800, y=400, width=220, height=220)

      b7_1=Button(bg_img,text="Developer", cursor="hand2", font=("Times New Roman",15,"bold"),bg="darkblue", fg="white")
      b7_1.place(x=800,y=600,width=220, height=40)

      #Exit
      img8=Image.open(r"E:\SIH Project\Images\Exit.png")
      img8=img8.resize((220,220),Image.ANTIALIAS)
      self.photoimg8=ImageTk.PhotoImage(img8)

      b8=Button(bg_img, image=self.photoimg8, cursor="hand2")
      b8.place(x=1100, y=400, width=220, height=220)

      b8_1=Button(bg_img,text="Exit", cursor="hand2", font=("Times New Roman",15,"bold"),bg="darkblue", fg="white")
      b8_1.place(x=1100,y=600,width=220, height=40)

    def open_img(self):
      os.startfile("data")

    # ============Function Buttons========
    def student_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Student(self.new_window)


    #========================Train Data===================
    def train_classifier(self):
      data_dir=("data")
      path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

      faces=[]
      ids=[]

      for image in path:
        img=Image.open(image).convert('L')
        imageNp=np.array(img,'uint8')
        id=int(os.path.split(image)[1].split('.')[1])

        faces.append(imageNp)
        ids.append(id)
        cv2.imshow("Training", imageNp)
        cv2.waitKey(1)==13
      ids=np.array(ids)

      # ================Train Classifier===============
      clf=cv2.face.LBPHFaceRecognizer_create()
      clf.train(faces, ids)
      clf.write("classifier.xml")
      cv2.destroyAllWindows()
      messagebox.showinfo("Result", "Training Datasets Completed")



    #==================================Face Recognition============================
    def face_recog(self):
      def draw_boundry(img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features=classifier.detectMultiScale(gray_image,scaleFactor, minNeighbors)

        coord=[]

        for (x,y,w,h) in features:
          cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
          id,predict=clf.predict(gray_image[y:y+h,x:x+w])
          confidence=int((100*(1-predict/300)))

          conn=mysql.connector.connect(host="localhost", username="root", password="9831035162@Sonu", database="SIH2022")
          my_cursor = conn.cursor()
          
          my_cursor.execute("select Student_Name from student where Student_ID="+str(id))
          n=my_cursor.fetchone()
          n="+".join(n)

          if confidence>77:
            cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
          else:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
            cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)

          coord[x,y,w,h]
          
        return coord

      def recognize(img, clf, faceCascade):
        coord=draw_boundry(img,faceCascade, 1.1, 10, (255,25,255), "Face", clf)
        return img
        
      faceCascade=cv2.CascadeClassifier("Haarcascade_frontalface_default.xml")
      clf=cv2.face.LBPHFaceRecognizer_create()
      clf.read("classifier.xml")

      video_cap=cv2.VideoCapture(0)

      while True:
        ret,img=video_cap.read()
        img=recognize(img,clf,faceCascade)
        cv2.imshow("Welcome To Face Recognition",img)

        if cv2.waitKey(1)==13:
          break
      video_cap.release()
      cv2.destroyAllWindows()

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

