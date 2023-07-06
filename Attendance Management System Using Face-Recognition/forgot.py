import mysql.connector
import os
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
import string
import random
import smtplib
from PIL import Image,ImageTk
import re

OTP_password=0
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def next():
    top.destroy()
    os.system('python C://Roadster//Major//reset.py')

def mouseClick(event):
  top.destroy()
  os.system('python C://Roadster//Major//drawv.py')

def clear():
    t1.delete(0,'end')

def clear1():
    t3.delete(0,'end')

def verify():
    gmail=t1.get()
    if gmail == "":
        messagebox.showwarning("Warning", "Please Insert Valid Gmail Id")

    elif re.search("[-+_!#$%^&*()<>?/\|}{~:]", gmail):
        messagebox.showwarning("Warning", "Please Insert Valid Gmail Id")
    else:
        clear()
        #print(gmail)
        validate(gmail)

def validate(gmail):
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="attendance")
        cursor = db.cursor()
        savequery = "SELECT * FROM teacherdb WHERE Email= '" + gmail +"'"
        #print(savequery)
        try:
            cursor.execute(savequery)
            rows = cursor.fetchall()
            numrows = int(cursor.rowcount)
            #print(numrows)
            if numrows == 1:
                sendmail(gmail)
            else:
                messagebox.showerror("Error", "Invalid Email id Please Retry!")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error",e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
    db.close()
def sendmail(gmail):
    try:
        simple_text = "your password is:"
        receiver_id = gmail
        s1 = string.ascii_uppercase
        s2 = string.ascii_lowercase
        s3 = string.digits
        plen = 6
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        global OTP_password
        OTP_password = ("".join(random.sample(s, plen)))
        FOTP_password= "Your OTP is " + OTP_password + " Please Do Not Share With It EveryOne!"
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("digitalchamp2016@gmail.com", "QAZWSXEDCRFV@109")

        try:
            s.sendmail("user_id", receiver_id, FOTP_password)
            messagebox.showinfo("Information", "OTP send successfully please verify your account!")
        except smtplib.SMTPException as e:
            messagebox.showerror("Error", e)
        s.quit()
    except smtplib.SMTPException as e:
        messagebox.showerror("Error", e)

def verifyotp():
    global OTP_password
    test=0
    #print(OTP_password)
    OOTP_password=t3.get()
    if t3.get() == "":
        messagebox.showwarning("Warning", "OTP Field Should Not Be Blank!")
    else:
        if OOTP_password == OTP_password:
            messagebox.showinfo("Information", "Account Verified Successfully!")
            clear1()
            next()
        else:
            messagebox.showerror("Error", "Invalid Please Enter Valid OTP! ")
            clear1()

top = Tk()
top.geometry("1490x750+10+10")
top.resizable(0, 0)
top.title("Reset Password")
p1 = PhotoImage(file = 'C://Roadster//Major//icont.png')
top.iconphoto(False, p1)
bg=ImageTk.PhotoImage(file="C://Roadster//Major//back.jpg")
bg_image=Label(top,image=bg).place(x=0,y=0,relwidth=1,relheight=1)

Frame_Login = Frame(top,bg=_from_rgb((33, 40, 62)))
Frame_Login.place(x=490,y=80,height=550,width=400)

logo=ImageTk.PhotoImage(file="C://Roadster//Major//logo.png")
logo_image=Label(Frame_Login,image=logo,bg=_from_rgb((33, 40, 62))).place(x=168,y=20)

previous=ImageTk.PhotoImage(file="C://Roadster//Major//previous.png")
previous_image=Label(Frame_Login,image=previous,bg=_from_rgb((33, 40, 62)))
previous_image.bind("<Button>", mouseClick)
previous_image.place(x=0,y=20)

l1=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg="white",text="VERIFY",font = "Verdana 15 bold").place(x=75,y=90)
l2=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg="white",text="YOUR ACCOUNT",font = "Verdana 15").place(x=165,y=90)
l3=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg="white",text="Recover your account",font = "Verdana 10").place(x=130,y=120)


t1=Entry(Frame_Login,bg=_from_rgb((33,40,62)),width=17, highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t1.place(height=30,x=96,y=180)
separator = ttk.Separator(Frame_Login,orient="horizontal")
separator.place(x=97,y=210, relwidth=0.6, relheight=-1)

username=ImageTk.PhotoImage(file="C://Roadster//Major//gmail (1).png")
username_icon=Label(Frame_Login,image=username,bg=_from_rgb((33, 40, 62))).place(x=55,y=180)

t3=Entry(Frame_Login,bg=_from_rgb((33,40,62)),width=17,highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t3.place(height=30,x=96,y=325)
separator = ttk.Separator(Frame_Login,orient="horizontal")
separator.place(x=97,y=355, relwidth=0.6, relheight=-1)

mail=ImageTk.PhotoImage(file="C://Roadster//Major//OTP.png")
mail_icon=Label(Frame_Login,image=mail,bg=_from_rgb((33, 40, 62))).place(x=55,y=323)

b1=Button(Frame_Login,bg=_from_rgb((48,130,184)),bd=0,width=22,text="Send OTP",font = "Verdana 10 bold",fg="white",command=verify)
b1.place(x=100,y=250,height=35)

b2=Button(Frame_Login,bg=_from_rgb((48,130,184)),bd=0,width=22,text="VERIFY",font = "Verdana 10 bold",fg="white",command=verifyotp)
b2.place(x=100,y=400,height=35)

top.mainloop()

