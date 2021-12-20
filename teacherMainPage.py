from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from face_recognition import Face_Recognition
from teacherCheckStudentDetails import Student
from teacherCheckAttendance import Student_attendance


class teacherMainPage:
    def __init__(self, root, data=None):
        self.root = root
        self.root.geometry("1650x900+0+0")
        self.root.title("Face Recognition Attendance System")
        self.mydata = data
        # ---- Variables --- #

        # img1 = main background
        img1 = Image.open("Images/Harvey.jpeg")
        img1 = img1.resize((1650, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1650, height=900)

        # title
        title_lbl = Label(
            bg_img,
            text="TEACHER PORTAL",
            font=("times new roman", 30, "bold"),
            bg="black",
            fg="white",
        )
        title_lbl.place(x=200, y=100, width=1250, height=40)
        # title_lbl.place(x=100, y=100, width=1350, height=40)

        # Mark attendance frame
        markAttendance_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        markAttendance_frame.place(x=200, y=160, width=325, height=525)
        # markAttendance_frame.place(x=100, y=160, width=350, height=600)

        markAttendance_frame.config(highlightbackground="black", highlightcolor="black")

        # Edit attendance frame
        editAttendance_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        editAttendance_frame.place(x=662, y=160, width=325, height=525)
        # editAttendance_frame.place(x=600, y=160, width=350, height=600)

        editAttendance_frame.config(highlightbackground="black", highlightcolor="black")

        # details frame
        details_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        details_frame.place(x=1124, y=160, width=325, height=525)
        # details_frame.place(x=1100, y=160, width=350, height=600)

        details_frame.config(highlightbackground="black", highlightcolor="black")

        # img2 = markAttendance image
        img2 = Image.open("Images/face.png")
        img2 = img2.resize((290, 290), Image.ANTIALIAS) # (300, 300)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=220, y=183, width=290, height=290)
        # bg_img.place(x=125, y=183, width=300, height=300)

        # img3 = editAttendance image
        img4 = Image.open("Images/attendanceBoard.jpeg")
        img4 = img4.resize((290, 290), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=682, y=183, width=290, height=290)
        # bg_img.place(x=615, y=183, width=320, height=300)

        # img4 = Details image
        img3 = Image.open("Images/id.jpeg")
        img3 = img3.resize((290, 290), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=1144, y=183, width=290, height=290)
        # bg_img.place(x=1115, y=183, width=320, height=300)

        # markAttendance button
        markAttendance_btn = Button(
            markAttendance_frame,
            command=self.mark_attandance,
            relief='raised',
            width=15,
            height=3,
            # width=25,
            # height=6,
            text="Mark\nAttendance",
            font=("times new roman", 20, "bold"),
            bg="#D1E8E4",
            fg="black",
            highlightcolor = '#FF8243',
        )
        markAttendance_btn.place(x=31, y=351, anchor=NW) # x=15, y=400

        # details button
        details_btn = Button(
            details_frame,
            command=self.student_details,
            width=15,
            height=3,
            text="Check\nStudent Details",
            font=("times new roman", 20, "bold"),
            bg="#D1E8E4",
            fg="black",
            highlightcolor = '#FF8243'
        )
        details_btn.place(x=31, y=351, anchor=NW)

        # editAttendance button
        editAttendance_btn = Button(
            editAttendance_frame,
            command=self.attendance_details,
            # width=25,
            # height=6,
            width=15,
            height=3,
            text="Check / Edit\nAttendance",
            font=("times new roman", 20, "bold"),
            bg="#D1E8E4",
            fg="black",
            highlightcolor = '#FF8243'
        )
        editAttendance_btn.place(x=31, y=351, anchor=NW)

    # ==================function ============================================#

    # ====================mark attandance button ==============================#

    def mark_attandance(self):
        self.new_window = Toplevel(
            self.root
        )  # This asks where we want to open our window
        self.app = Face_Recognition(self.new_window, self.mydata)

    def student_details(self):
        self.new_window = Toplevel(
            self.root
        )  # This asks where we want to open our window
        self.app = Student(self.new_window, self.mydata)

    def attendance_details(self):
        self.new_window = Toplevel(
            self.root
        )  # This asks where we want to open our window
        self.app = Student_attendance(self.new_window, self.mydata)


if __name__ == "__main__":
    root = Tk()
    obj = teacherMainPage(root)
    root.mainloop()
