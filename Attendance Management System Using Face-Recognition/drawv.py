import mysql.connector
import os
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from PIL import ImageTk


def dashboard():
    top.destroy()
    os.system('python C://Roadster//Major//dashboard.py')


def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


def mouseClick(event):
    top.destroy()
    os.system('python C://Roadster//Major//forgot.py')


def mouseClick1(event):
    top.destroy()
    os.system('python C://Roadster//Major//AddUser.py')


def clear():
    t1.delete(0, 'end')
    t2.delete(0, 'end')
    t3.delete(0, 'end')


def login():
    userid = t1.get()
    passid = t2.get()
    emailid = t3.get()
    if userid == "":
        messagebox.showwarning("Warning", "Username Field Should Not Be Empty")
    else:
        if passid == "":
            messagebox.showwarning("Warning", "Password Field Should Not Be Empty")
        else:
            if emailid == "":
                messagebox.showwarning("Warning", "Email Field Should Not Be Empty")
            else:
                #print(userid, passid, emailid)
                clear()
                confirm(userid, passid, emailid)


def confirm(userid, passid, emailid):
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", db="attendance")
        cursor = db.cursor()
        savequery = "SELECT * FROM teacherdb WHERE Username= '" + userid + "' AND Password = '" + passid + "' AND Email = '" + emailid + "'"
        #print(savequery)
        try:
            cursor.execute(savequery)
            rows = cursor.fetchall()
            numrows = int(cursor.rowcount)
            #print(numrows)
            if numrows == 1:
                messagebox.showinfo("Information", "Login Successful! You Are About To Redirect On Dashboard Page!")
                dashboard()
            else:
                messagebox.showerror("Error", "Invalid Username Or Password Or Email id Please Retry!")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()


top = Tk()
top.geometry("1490x750+10+10")
top.resizable(0, 0)
top.title("Login")
p1 = PhotoImage(file = 'C://Roadster//Major//icont.png')
top.iconphoto(False, p1)
bg = ImageTk.PhotoImage(file="C://Roadster//Major//back.jpg")
bg_image = Label(top, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

Frame_Login = Frame(top, bg=_from_rgb((33, 40, 62)))
Frame_Login.place(x=520, y=120, height=550, width=400)

logo = ImageTk.PhotoImage(file="C://Roadster//Major//logo.png")
logo_image = Label(Frame_Login, image=logo, bg=_from_rgb((33, 40, 62))).place(x=162, y=20)
text2 = Label(top, text="WELCOME TO  ATTENDANCE SYSTEM", font=("Impact", 55), fg="#00ffff", bg="#202020").place(x=250,
                                                                                                                y=20)
l1 = Label(Frame_Login, bg=_from_rgb((33, 40, 62)), fg="white", text="LOGIN TO", font="Verdana 15 bold").place(x=50,
                                                                                                               y=90)
l2 = Label(Frame_Login, bg=_from_rgb((33, 40, 62)), fg="white", text="YOUR ACCOUNT", font="Verdana 15").place(x=170,
                                                                                                              y=90)
l3 = Label(Frame_Login, bg=_from_rgb((33, 40, 62)), fg="white", text="Get Access To Attendance",
           font="Verdana 10").place(x=100, y=120)

t1 = Entry(Frame_Login, bg=_from_rgb((33, 40, 62)), width=17, highlightthickness=0, bd=0, justify=CENTER, fg="white",
           font="Verdana 15 bold")
t1.place(height=30, x=96, y=180)
separator = ttk.Separator(Frame_Login, orient="horizontal")
separator.place(x=97, y=210, relwidth=0.6, relheight=-1)

t2 = Entry(Frame_Login, bg=_from_rgb((33, 40, 62)), width=17, show="*", highlightthickness=0, bd=0, justify=CENTER,
           fg="white", font="Verdana 15 bold")
t2.place(height=30, x=96, y=250)
separator = ttk.Separator(Frame_Login, orient="horizontal")
separator.place(x=97, y=280, relwidth=0.6, relheight=-1)

t3 = Entry(Frame_Login, bg=_from_rgb((33, 40, 62)), width=17, highlightthickness=0, bd=0, justify=CENTER, fg="white",
           font="Verdana 15 bold")
t3.place(height=30, x=96, y=320)
separator = ttk.Separator(Frame_Login, orient="horizontal")
separator.place(x=97, y=350, relwidth=0.6, relheight=-1)

password = ImageTk.PhotoImage(file="C://Roadster//Major//password.png")
password_icon = Label(Frame_Login, image=password, bg=_from_rgb((33, 40, 62))).place(x=55, y=247)

username = ImageTk.PhotoImage(file="C://Roadster//Major//Username.png")
username_icon = Label(Frame_Login, image=username, bg=_from_rgb((33, 40, 62))).place(x=55, y=181)

mail = ImageTk.PhotoImage(file="C://Roadster//Major//mail.png")
mail_icon = Label(Frame_Login, image=mail, bg=_from_rgb((33, 40, 62))).place(x=55, y=325)

b1 = Button(Frame_Login, bg=_from_rgb((48, 130, 184)), bd=0, width=32, text="Login", font="Verdana 10 bold", fg="white",
            command=login).place(x=55, y=390, height=35)

l3 = Label(Frame_Login, bg=_from_rgb((33, 40, 62)), fg="white", text="Forgot my password :(",
           font="Verdana 10")  # .place(x=120,y=460)
l3.bind("<Button>", mouseClick)
l3.place(x=120, y=460)

l4 = Label(Frame_Login, bg=_from_rgb((33, 40, 62)), fg="white", text="I don't have an account", font="Verdana 10")
l4.bind("<Button>", mouseClick1)
l4.place(x=117, y=480)
top.mainloop()
