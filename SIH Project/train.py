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

class Train:
    def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Train Data")
      
      b1=Button(self.root, text="Train Data",command=self.train_classifier, cursor="hand2")
      b1.place(x=200, y=100, width=220, height=220)

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




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
