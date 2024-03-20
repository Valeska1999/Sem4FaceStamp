from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from PIL import Image
from datetime import datetime
from time import strftime

class face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        img6 = Image.open(r"C:\Users\Valeska\Desktop\Sem4MiniProject\ImagesForGUI\page2.jpeg")
        img6 = img6.resize((1550, 790), Image.ADAPTIVE)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        f_lbl6 = Label(self.root, image=self.photoimg6)
        f_lbl6.place(x=0, y=0, width=1550, height=790)
        

        # f_lbl1=Label(self.root,image=self.photoimg6)
        # f_lbl1.place(x=0,y=0,width=50,height=130)
        # text_label = Label(self.root, text=" Attendence", font=("Helvetica", 50))
        # text_label.place(x=500, y=0, width=550, height=130)
        f_lbl1=Label(self.root,image=self.photoimg6)
        f_lbl1.place(x=0,y=0,width=500,height=130)
        text_label = Label(self.root, text="Take Attendence", font=("Helvetica", 50))
        text_label.place(x=500, y=0, width=550, height=130)
        # img=Image.open(r"C:\Users\Valeska\Desktop\Sem4MiniProject\ImagesForGUI\att.png")
        # img=img.resize((1500,300),Image.ADAPTIVE)
        # self.photoimg = ImageTk.PhotoImage(img)
        # f_lbl1=Label(self.root,image=self.photoimg)
        # f_lbl1.place(x=0,y=0,width=1500,height=300)
        

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
        fr = LabelFrame(root, bd=2, bg="black", relief=RIDGE, fg="white", font=("times new roman", 15, "bold"))
        fr.place(x=665, y=400, width=150, height=75)
        lbl = Label(fr, font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl.place(x=20, y=20, width=110, height=30)  # Adjust the coordinates to position the label properly
        time()
        b1_1 = Button(self.root, text="Take Attendence ",command=self.face_recog, cursor="hand2", font=("times new roman", 18, "bold"), bg="white", fg="black")
        b1_1.place(x=650, y=500, width=200, height=40)

    def  mark_attendace(self,i,r,n):
        with open("att.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) ):
                now=datetime.now()
                d1=now.strftime()
                dtString=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")



    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord=[]
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                
                conn = mysql.connector.connect(host="localhost", username="root", password="$Leaval10", database="sem4facestamp")
                my_cursor = conn.cursor()

                my_cursor.execute("select sname from student where spid=" + str(id))
                n = my_cursor.fetchone()
                n = str(n)

                my_cursor.execute("select rollno from student where spid=" + str(id))
                r = my_cursor.fetchone()
                r= str(r)

                # my_cursor.execute("select Dep from student where spid=" + str(id))
                # d = my_cursor.fetchone()
                # d="+".join(d)

                my_cursor.execute("select spid from student where spid=" + str(id))
                i = my_cursor.fetchone()
                i= str(i)


                # my_cursor.execute("select Dep from student where spid=" + str(id))
                # d = my_cursor.fetchone()
                # d = "+".join(d)
                if confidence > 77:
                    cv2.putText(img, f"Roll: {r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"spid: {i}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendace(i,r,n)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord=[x,y,w,y]
            return coord   
        def recognize(img, clf, faceCascade):
            img = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img 
        # faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        clf =cv2.face_LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            # print(type((img)))
            cv2.imshow("Welcome To Face Recognition",img)


            if cv2.waitKey(1) == 13:
                break
        
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = face_recognition(root)
    root.mainloop()
