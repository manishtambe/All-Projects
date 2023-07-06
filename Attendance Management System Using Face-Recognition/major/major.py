
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
import os
import tkinter as tk
from PIL import Image,ImageTk

def Explore():
    root4.destroy()
    os.system('python drawv.py')

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

"""top = Tk()
top.geometry("1362x700+-7+0")
top.resizable(0, 0)
top.title("Explore")

#bg=ImageTk.PhotoImage(file="Start.jpg")
#bg_image=Label(top,image=bg).place(x=0,y=0,relwidth=1,relheight=1)

Frame_Login = Frame(top,bg=_from_rgb((33, 40, 62)),width=1362)
Frame_Login.place(x=0,y=0,height=700)

logo=ImageTk.PhotoImage(file="logo.png")
logo_image=Label(Frame_Login,image=logo,bg=_from_rgb((33, 40, 62))).place(x=630,y=100)

l1=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Attendance Management System Using Face Recognition",font = "Verdana 29 bold").place(x=61,y=190)
l2=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Attend Today And Achive Tomorrow.....",font = "Verdana 15 bold").place(x=450,y=280)
l3=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Copyright © MMT & Roadster Systems 2021. All Rights Reserved",font = "Verdana 15 bold").place(x=300,y=650)

b1=Button(top,bg=_from_rgb((0,200,244)),fg="white",bd=0,width=32,text="Explore",font = "Verdana 10 bold",command=Explore)
b1.place(x=525,y=360,height=40)

top.mainloop()"""
root4 = Tk()
root4.geometry("1280x800+150+20")
bg = ImageTk.PhotoImage(file="icons\\startup.jpg")
bg_image1 = Label(root4,image=bg).place(x=0, y=0, relwidth=1, relheight=1)
root4.overrideredirect(True)
root4.after(3000,Explore)
root4.mainloop()


















