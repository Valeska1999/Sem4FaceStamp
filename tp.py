
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

        # Background Image
        img1 = Image.open(r"C:\Users\Valeska\Desktop\Sem4MiniProject\ImagesForGUI\val.png")
        img1 = img1.resize((1550, 790), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=1550, height=790)

        # Title
        title_lbl = Label(self.root, text="Face-Based Attendance System", font=("Helvetica", 28, "bold"), fg="white", bg="purple4")
        title_lbl.place(x=550, y=50, width=600, height=50)
        title_lbl.config(compound='center')

        title_lbl = Label(self.root, text="Face Stamp", font=("Helvetica", 24, "bold"), fg="white", bg="purple4")
        title_lbl.place(x=1150, y=100, width=200, height=30)
        title_lbl.config(compound='center')

        # LoginId
        title_lb2 = Label(self.root, text="Login Id", font=("Helvetica", 20, "bold"), fg="white", bg="purple4")
        title_lb2.place(x=700, y=200, width=200, height=30)
        self.e1 = ttk.Entry(self.root, font=("Helvetica", 16))
        self.e1.place(x=930, y=200, width=220, height=30)

        title_lb3 = Label(self.root, text="Password", font=("Helvetica", 20, "bold"), fg="white", bg="purple4")
        title_lb3.place(x=700, y=270, width=200, height=30)
        self.e2 = Entry(self.root, show="*", font=("Helvetica", 16))
        self.e2.place(x=930, y=270, width=220, height=30)

        b7_7 = Button(self.root, text="Login", command=self.login, cursor="hand2", font=("Helvetica", 18, "bold"), fg="black", bg="lime green", relief=FLAT)
        b7_7.place(x=1000, y=360, width=220, height=40)

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
