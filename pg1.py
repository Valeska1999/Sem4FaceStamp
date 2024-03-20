# from tkinter import *
# from tkinter import ttk,messagebox
# from PIL import Image, ImageTk, ImageDraw
# from student import Student
# from Main import Page2
# from PIL import Image
# import mysql.connector


# class FaceRecognitionSystem:
#     def __init__(self, root):
#         conn=mysql.connector.connect(host="localhost", username="root", password="$Leaval10", database="sem4facestamp")
#         my_cursor = conn.cursor()
#         global e1
#         global e2
        

#         loginid=e1.get()
#         password=e2.get()
#         sql="select * from login where loginid=%s and password =%s"
       
#         self.root = root
#         self.root.geometry("1550x790+0+0")
#         self.root.title("FaceStamp")
        
#         # Load and display the first image
#         img1 = Image.open(r"C:\Users\Valeska\Desktop\Sem4MiniProject\ImagesForGUI\MainPage.jpeg")
#         img1 = img1.resize((1550, 790), Image.ADAPTIVE)
#         self.photoimg1 = ImageTk.PhotoImage(img1)
#         f_lbl1 = Label(self.root, image=self.photoimg1)
#         f_lbl1.place(x=0, y=0, width=1550, height=790)

#         # # Load the second image and apply circular mask
#         # img2 = Image.open(r"C:\Users\Valeska\Desktop\Sem4MiniProject\ImagesForGUI\img2.jpeg")
#         # img2 = img2.resize((650, 650), Image.ADAPTIVE)

#         # # Create a circular mask
#         # mask = Image.new("L", (650, 650), 0)
#         # draw = ImageDraw.Draw(mask)
#         # draw.ellipse((10, 10, 650, 650), fill=255)

#         # img2.putalpha(mask)
#         # self.photoimg2 = ImageTk.PhotoImage(img2)
#         # f_lb2 = Label(self.root, image=self.photoimg2)
#         # f_lb2.place(x=10, y=10, width=650, height=650)
#         #Title
#         title_lbl = Label(self.root, text="Face-Based Attendance System", font=("Helvetica", 24), fg="white", bg="grey")
#         title_lbl.place(x=790, y=65, width=600, height=30)
#         title_lbl.config(compound='center')
#         title_lbl = Label(self.root, text="Face Stamp", font=("Helvetica", 24), fg="white", bg="grey")
#         title_lbl.place(x=1190, y=100, width=200, height=30)
#         title_lbl.config(compound='center')
#         #LoginId
#         title_lb2 = Label(self.root, text="Login Id ", font=("Helvetica", 24), fg="white", bg="grey")
#         title_lb2.place(x=700, y=300, width=200, height=30)
#         password_entry =ttk.Entry(self.root, font=("Helvetica", 14))
#         password_entry.place(x=930, y=300, width=220, height=30)

#         title_lb3 = Label(self.root, text="Password", font=("Helvetica", 24), fg="white", bg="grey")
#         title_lb3.place(x=700, y=400, width=200, height=30)
#         password_entry = Entry(self.root, show="*", font=("Helvetica", 14))
#         password_entry.place(x=930, y=400, width=220, height=30)

#         b7_7 = Button(self.root, text="Login",command=self.student_details, cursor="hand2", font=("Helvetica", 14), fg="black", bg="white", relief=FLAT)
#         b7_7.place(x=1000, y=600, width=220, height=40)

#     def login(self):
#         if self.title_lb2.get()=="" or self.title_lb3.get()=="":

#             messagebox. showerror ("Error", "all field required")
#         elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
#             messagebox.showinfo("Success", "Welcome to codewithkiran channel please subscribe my channel")
#             self.new_window = Toplevel(self.root)
#             self.app = Page2(self.new_window)
#         else:
#             messagebox. showerror ("Invalid", "Invalid username&password")

#     def student_details(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Page2(self.new_window)
 

# if __name__ == "__main__":
#     root = Tk()
#     obj = FaceRecognitionSystem(root)
#     root.mainloop()


from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw
import mysql.connector
from student import Student
from Main import Page2


class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x790+0+0")
        self.root.title("FaceStamp")

        # Load and display the first image
        img1 = Image.open(r"C:\Users\Valeska\Desktop\Sem4MiniProject\ImagesForGUI\val.png")
        img1 = img1.resize((1550, 790), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=1550, height=790)
        
        # img2 = Image.open(r"C:\Users\Valeska\Desktop\Sem4MiniProject\ImagesForGUI\img2.jpeg")
        # img2 = img2.resize((650, 650), Image.ADAPTIVE)

        # # Create a circular mask
        # mask = Image.new("L", (650, 650), 0)
        # draw = ImageDraw.Draw(mask)
        # draw.ellipse((10, 10, 650, 650), fill=255)

        # img2.putalpha(mask)
        # self.photoimg2 = ImageTk.PhotoImage(img2)
        # f_lb2 = Label(self.root, image=self.photoimg2)
        # f_lb2.place(x=10, y=10, width=650, height=650)

        # Title
        title_lbl = Label(self.root, text="Face-Based Attendance System", font=("Helvetica", 24), fg="white", bg="grey")
        title_lbl.place(x=790, y=65, width=600, height=30)
        title_lbl.config(compound='center')
        title_lbl = Label(self.root, text="Face Stamp", font=("Helvetica", 24), fg="white", bg="grey")
        title_lbl.place(x=1190, y=100, width=200, height=30)
        title_lbl.config(compound='center')

        # LoginId
        title_lb2 = Label(self.root, text="Login Id ", font=("Helvetica", 24), fg="white", bg="grey")
        title_lb2.place(x=700, y=300, width=200, height=30)
        self.e1 = ttk.Entry(self.root, font=("Helvetica", 14))
        self.e1.place(x=930, y=300, width=220, height=30)

        title_lb3 = Label(self.root, text="Password", font=("Helvetica", 24), fg="white", bg="grey")
        title_lb3.place(x=700, y=400, width=200, height=30)
        self.e2 = Entry(self.root, show="*", font=("Helvetica", 14))
        self.e2.place(x=930, y=400, width=220, height=30)

        b7_7 = Button(self.root, text="Login", command=self.login, cursor="hand2", font=("Helvetica", 14), fg="black", bg="white", relief=FLAT)
        b7_7.place(x=1000, y=600, width=220, height=40)

    def login(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="$Leaval10", database="sem4facestamp")
        my_cursor = conn.cursor()

        loginid = self.e1.get()
        password = self.e2.get()
        sql = "SELECT * FROM login WHERE loginid = %s AND password = %s"
        my_cursor.execute(sql, (loginid, password))
        result = my_cursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Login Successful!")
            self.new_window = Toplevel(self.root)
            self.app = Page2(self.new_window)
        else:
            messagebox.showerror("Error", "Invalid login credentials")

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()

