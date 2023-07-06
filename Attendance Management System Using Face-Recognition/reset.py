import mysql.connector
import os
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def redirect():
    top.destroy()
    os.system('python C://Roadster//Major//drawv.py')

def clear():
    t1.delete(0,'end')
    t2.delete(0,'end')
    t3.delete(0,'end')

def mouseClick(event):
  top.destroy()
  os.system('python C://Roadster//Major//forgot.py')

def changepassword(userf,ffnew):
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", db="attendance")
        cursor = db.cursor()
        savequery = "UPDATE teacherdb SET Password='" + ffnew + "'"+"WHERE Username= '"+userf+"'"
        #print(savequery)
        try:
            cursor.execute(savequery)
            db.commit()
            numrows = cursor.rowcount
            #print(numrows)
            if numrows == 1:
                messagebox.showinfo("Information","Password Reset Successful! You Are About To Redirect On Login Page!")
                redirect()
            else:
                messagebox.showerror("Error", "Invalid Username Please Retry!")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()

def check(user,cnew):
    userf=user
    ffnew=cnew
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", db="attendance")
        cursor = db.cursor()
        savequery = "SELECT * FROM teacherdb WHERE Username= '" + userf + "'"
        #print(savequery)
        try:
            cursor.execute(savequery)
            rows = cursor.fetchall()
            numrows = int(cursor.rowcount)
            #print(numrows)
            if numrows == 1:
                changepassword(userf,ffnew)
            else:
                messagebox.showerror("Error", "Invalid Username Please Retry!")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()
def reset():
    user=t1.get()
    new=t2.get()
    cnew=t3.get()
    if user == "":
        messagebox.showwarning("Warning", "Please Insert Username")
    else:
        if new == "":
            messagebox.showwarning("Warning", "Please Insert Password!")
        else:
            if cnew == "":
                messagebox.showwarning("Warning", "Please Confirm Password!")
            else:
                if new == cnew:
                    clear()
                    check(user,cnew)
                else:
                    messagebox.showerror("Error", "Password Mismatched Please Enter Same Password!")
                    clear()
top = Tk()
top.geometry("1490x750+10+10")
top.resizable(0, 0)
top.title("Reset Password")
p1 = PhotoImage(file = 'C://Roadster//Major//icont.png')
top.iconphoto(False, p1)
bg=ImageTk.PhotoImage(file="C://Roadster//Major//back.jpg")
bg_image=Label(top,image=bg).place(x=0,y=0,relwidth=1,relheight=1)

Frame_Login = Frame(top,bg=_from_rgb((33, 40, 62)))
Frame_Login.place(x=430,y=85,height=520,width=500)

logo=ImageTk.PhotoImage(file="C://Roadster//Major//logo.png")
logo_image=Label(Frame_Login,image=logo,bg=_from_rgb((33, 40, 62))).place(x=215,y=20)

previous=ImageTk.PhotoImage(file="C://Roadster//Major//previous.png")
previous_image=Label(Frame_Login,image=previous,bg=_from_rgb((33, 40, 62)))
previous_image.bind("<Button>", mouseClick)
previous_image.place(x=0,y=20)

l1=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg="white",text="RESET",font = "Verdana 15 bold").place(x=120,y=90)
l2=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg="white",text="Account Password",font = "Verdana 15").place(x=200,y=90)
l3=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg="white",text="Please Insert Valid Details",font = "Verdana 10").place(x=160,y=120)


t1=tk.Entry(Frame_Login,bg=_from_rgb((33,40,62)),width=15, highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t1.place(height=30,x=275,y=180)
separator = ttk.Separator(Frame_Login,orient="horizontal")
separator.place(x=280,y=210, relwidth=0.4, relheight=-1)

t2=tk.Entry(Frame_Login,bg=_from_rgb((33,40,62)),width=15,show='*',highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t2.place(height=30,x=275,y=250)
separator = ttk.Separator(Frame_Login,orient="horizontal")
separator.place(x=275,y=280, relwidth=0.4, relheight=-1)

t3=tk.Entry(Frame_Login,bg=_from_rgb((33,40,62)),width=15,show='*',highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t3.place(height=30,x=275,y=327)
separator = ttk.Separator(Frame_Login,orient="horizontal")
separator.place(x=240,y=357, relwidth=0.5, relheight=-1)

password_text=Label(Frame_Login,text="New Password:-",fg=_from_rgb((0,200,244)),font = "Verdana 17 bold",bg=_from_rgb((33, 40, 62))).place(x=10,y=247)
username_text=Label(Frame_Login,text="Username:-",fg=_from_rgb((0,200,244)),font = "Verdana 17 bold",bg=_from_rgb((33, 40, 62))).place(x=10,y=181)
mail_text=Label(Frame_Login,text="Confirm Password:-",fg=_from_rgb((0,200,244)),font = "Verdana 17 bold",bg=_from_rgb((33, 40, 62))).place(x=10,y=325)

b1=Button(Frame_Login,bg=_from_rgb((0,200,244)),bd=0,width=32,text="Reset",font = "Verdana 10 bold",fg="white",command=reset)
b1.place(x=105,y=390,height=35)

top.mainloop()
