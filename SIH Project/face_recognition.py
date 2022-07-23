import imghdr
from readline import get_history_item
from tkinter import*
from tkinter import ttk
from turtle import update, width
from PIL import Image, ImageTk
from numpy import save
from tkinter import messagebox
import pyodbc
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition")
      
      b1=Button(self.root, text="Face Recognition",command=self.face_recog, cursor="hand2")
      b1.place(x=200, y=100, width=220, height=220)

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
        cv2.imshow("Welcome To Face Recognition", img)

        if cv2.waitKey(1)==13:
          break
      video_cap.release()
      cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
