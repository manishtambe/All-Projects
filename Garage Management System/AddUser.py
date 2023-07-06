import sys
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
    os.system('Login.py')

def mouseClick(event):
  top.destroy()
  os.system('Login.py')

def clear():
    t1.delete(0, 'end')
    t2.delete(0, 'end')
    t3.delete(0, 'end')
    t4.delete(0, 'end')
    t5.delete(0, 'end')

def login():
    fname=t1.get()
    lname=t2.get()
    email=t3.get()
    user=t4.get()
    passd=t5.get()
    if fname=="":
        messagebox.showwarning("Warning","First Name Should Not Be Empty")
    else:
        if lname=="":
            messagebox.showwarning("Warning","Last Name Should Not Be Empty")
        else:
            if email=="":
                messagebox.showwarning("Warning", "Mail Field Should Not Be Empty")
            else:
                if user=="":
                    messagebox.showwarning("Warning", "Username Field Should Not Be Empty")
                else:
                    if passd=="":
                        messagebox.showwarning("Warning", "Password Field Should Not Be Empty")
                    else:
                        #print(fname, lname, email, user, passd)
                        clear()
                        logintodb(fname, lname, email, user, passd)

def logintodb(fname, lname, email, user, passwd ):
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery = "insert into logindb (Fname,Lname,Email,Username,Password) values (%s,%s,%s,%s,%s)"
        try:
            cursor.execute(savequery,(fname,lname,email,user,passwd))
            db.commit()
            messagebox.showinfo("Information","Entry Added Successfully! You Are About To Redirect On Login Page!")
            redirect()
        except mysql.connector.Error as e:
            messagebox.showinfo("Error",e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
    db.close()

top = Tk()
top.geometry("1362x700+-7+0")
top.resizable(0, 0)
top.title("Add User")

p1 = PhotoImage(file = 'tools.png')
top.iconphoto(False, p1)

bg=ImageTk.PhotoImage(file="Back.png")
bg_image=Label(top,image=bg).place(x=0,y=0,relwidth=1,relheight=1)

Frame_Login = Frame(top,bg=_from_rgb((33, 40, 62)))
Frame_Login.place(x=436,y=55,height=590,width=490)

logo=ImageTk.PhotoImage(file="logo11.png")
logo_image=Label(Frame_Login,image=logo,bg=_from_rgb((33, 40, 62))).place(x=205,y=-2)

previous=ImageTk.PhotoImage(file="previous.png")
previous_image=Label(Frame_Login,image=previous,bg=_from_rgb((33, 40, 62)))
previous_image.bind("<Button>", mouseClick)
previous_image.place(x=0,y=20)

l1=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg="white",text="Add New",font = "Verdana 15 bold").place(x=100,y=90)
l2=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg="white",text="User Account",font = "Verdana 15 bold").place(x=212,y=90)
l3=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg="white",text="Please Insert Valid Details",font = "Verdana 10").place(x=160,y=120)


t1=tk.Entry(Frame_Login,bg=_from_rgb((33,40,62)),width=18, highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t1.place(height=30,x=210,y=180)
separator = ttk.Separator(Frame_Login,orient="horizontal")
separator.place(x=212,y=210, relwidth=0.5, relheight=-1)

t2=tk.Entry(Frame_Login,bg=_from_rgb((33,40,62)),width=18,highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t2.place(height=30,x=210,y=250)
separator = ttk.Separator(Frame_Login,orient="horizontal")
separator.place(x=212,y=280, relwidth=0.5, relheight=-1)

t3=tk.Entry(Frame_Login,bg=_from_rgb((33,40,62)),width=18,highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t3.place(height=30,x=210,y=320)
separator = ttk.Separator(Frame_Login,orient="horizontal")
separator.place(x=212,y=350, relwidth=0.5, relheight=-1)

t4=tk.Entry(Frame_Login,bg=_from_rgb((33,40,62)),width=18,highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t4.place(height=30,x=210,y=390)
separator = ttk.Separator(Frame_Login,orient="horizontal")
separator.place(x=212,y=420, relwidth=0.5, relheight=-1)

t5=tk.Entry(Frame_Login,bg=_from_rgb((33,40,62)),width=18,highlightthickness=0,show="*",bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t5.place(height=30,x=210,y=460)
separator = ttk.Separator(Frame_Login,orient="horizontal")
separator.place(x=212,y=490, relwidth=0.5, relheight=-1)


password_text=Label(Frame_Login,text="Last Name:-",fg=_from_rgb((0,200,244)),font = "Verdana 15 bold",bg=_from_rgb((33, 40, 62))).place(x=55,y=247)
username_text=Label(Frame_Login,text="First Name:-",fg=_from_rgb((0,200,244)),font = "Verdana 15 bold",bg=_from_rgb((33, 40, 62))).place(x=55,y=181)
mail_text=Label(Frame_Login,text="Gmail Id:-",fg=_from_rgb((0,200,244)),font = "Verdana 15 bold",bg=_from_rgb((33, 40, 62))).place(x=55,y=325)
Username_text=Label(Frame_Login,text="Username:-",fg=_from_rgb((0,200,244)),font = "Verdana 15 bold",bg=_from_rgb((33, 40, 62))).place(x=55,y=394)
Password_text=Label(Frame_Login,text="Password:-",fg=_from_rgb((0,200,244)),font = "Verdana 15 bold",bg=_from_rgb((33, 40, 62))).place(x=55,y=464)

b1=Button(Frame_Login,bg=_from_rgb((0,200,244)),bd=0,width=32,text="Login",font = "Verdana 10 bold",fg="white",command=login).place(x=105,y=530,height=35)

top.mainloop()