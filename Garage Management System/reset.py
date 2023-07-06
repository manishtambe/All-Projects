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

def clear():
    t1.delete(0,'end')
    t2.delete(0,'end')
    t3.delete(0,'end')
def mouseClick(event):
  top.destroy()
  os.system('forgot.py')
def changepassword(userf,ffnew):
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", db="mmt_garages")
        cursor = db.cursor()
        savequery = "UPDATE logindb SET Password='" + ffnew + "'"+"WHERE Username= '"+userf+"'"
        print(savequery)
        try:
            cursor.execute(savequery)
            db.commit()
            # result = cursor.fetchone()
            # number_of_rows = result[0]
            #rows = cursor.fetchall()
            numrows = cursor.rowcount#int(cursor.rowcount)
            print(numrows)
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
        db = mysql.connector.connect(host="localhost", user="root", password="", db="mmt_garages")
        cursor = db.cursor()
        savequery = "SELECT * FROM logindb WHERE Username= '" + userf + "'"
        print(savequery)
        try:
            cursor.execute(savequery)
            # result = cursor.fetchone()
            # number_of_rows = result[0]
            rows = cursor.fetchall()
            numrows = int(cursor.rowcount)
            print(numrows)
            if numrows == 1:
                #messagebox.showinfo("Information","Login Successful! You Are About To Redirect On Dashboard Page!")
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
                    #messagebox.showinfo("Information","Login Successful!")
                    clear()
                    check(user,cnew)
                else:
                    messagebox.showerror("Error", "Password Mismatched Please Enter Same Password!")
                    clear()
top = Tk()
top.geometry("1362x700+-7+0")
top.resizable(0, 0)
top.title("Reset Password")

p1 = PhotoImage(file = 'tools.png')
top.iconphoto(False, p1)

bg=ImageTk.PhotoImage(file="Back.png")
bg_image=Label(top,image=bg).place(x=0,y=0,relwidth=1,relheight=1)

Frame_Login = Frame(top,bg=_from_rgb((23, 29, 66)))
Frame_Login.place(x=436,y=85,height=520,width=490)

logo=ImageTk.PhotoImage(file="logo11.png")
logo_image=Label(Frame_Login,image=logo,bg=_from_rgb((23, 29, 66))).place(x=200,y=0)

previous=ImageTk.PhotoImage(file="previous.png")
previous_image=Label(Frame_Login,image=previous,bg=_from_rgb((23, 29, 66)))
previous_image.bind("<Button>", mouseClick)
previous_image.place(x=0,y=20)

l1=Label(Frame_Login,bg=_from_rgb((23, 29, 66)),fg="white",text="RESET",font = "Verdana 15 bold").place(x=120,y=90)
l2=Label(Frame_Login,bg=_from_rgb((23, 29, 66)),fg="white",text="Account Password",font = "Verdana 15").place(x=200,y=90)
l3=Label(Frame_Login,bg=_from_rgb((23, 29, 66)),fg="white",text="Please Insert Valid Details",font = "Verdana 10").place(x=160,y=120)


t1=tk.Entry(Frame_Login,bg=_from_rgb((23, 29, 66)),width=15, highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t1.place(height=30,x=265,y=180)
separator = ttk.Separator(Frame_Login,orient="horizontal")
separator.place(x=265,y=210,width=215)

t2=tk.Entry(Frame_Login,bg=_from_rgb((23, 29, 66)),width=15,show='*',highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t2.place(height=30,x=265,y=250)
separator = ttk.Separator(Frame_Login,orient="horizontal")
separator.place(x=265,y=280,width=215)

t3=tk.Entry(Frame_Login,bg=_from_rgb((23, 29, 66)),width=15,show='*',highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t3.place(height=30,x=265,y=327)
separator = ttk.Separator(Frame_Login,orient="horizontal")
separator.place(x=265,y=357,width=215)

password_text=Label(Frame_Login,text="New Password:-",fg=_from_rgb((0,200,244)),font = "Verdana 17 bold",bg=_from_rgb((23, 29, 66))).place(x=0,y=247)
username_text=Label(Frame_Login,text="Username:-",fg=_from_rgb((0,200,244)),font = "Verdana 17 bold",bg=_from_rgb((23, 29, 66))).place(x=0,y=181)
mail_text=Label(Frame_Login,text="Confirm Password:-",fg=_from_rgb((0,200,244)),font = "Verdana 17 bold",bg=_from_rgb((23, 29, 66))).place(x=0,y=325)

b1=Button(Frame_Login,bg=_from_rgb((0,200,244)),bd=0,width=32,text="Reset",font = "Verdana 10 bold",fg="white",command=reset)
b1.place(x=105,y=390,height=35)

top.mainloop()

#t4=tk.Entry(Frame_Login,bg=_from_rgb((33,40,62)),width=18,highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
#t4.place(height=30,x=210,y=390)
#separator = ttk.Separator(Frame_Login,orient="horizontal")
#separator.place(x=212,y=420, relwidth=0.5, relheight=-1)

#t5=tk.Entry(Frame_Login,bg=_from_rgb((33,40,62)),width=18,highlightthickness=0,show="*",bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
#t5.place(height=30,x=210,y=460)
#separator = ttk.Separator(Frame_Login,orient="horizontal")
#separator.place(x=212,y=490, relwidth=0.5, relheight=-1)

#Username_text=Label(Frame_Login,text="Username:-",fg=_from_rgb((0,200,244)),font = "Verdana 15 bold",bg=_from_rgb((33, 40, 62))).place(x=55,y=394)
#Password_text=Label(Frame_Login,text="Password:-",fg=_from_rgb((0,200,244)),font = "Verdana 15 bold",bg=_from_rgb((33, 40, 62))).place(x=55,y=464)