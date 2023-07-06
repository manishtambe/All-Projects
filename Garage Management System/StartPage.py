import os
import tkinter
import tkinter as tk
from tkinter import*
#from PIL import ImageTk
root = tk.Tk()
root.title("Welcome")
root.geometry("1362x700+-7+0")
root.resizable(0,0)

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def dash():
    root.destroy()
    os.system("Login.py")

p1 = PhotoImage(file = 'tools.png')
root.iconphoto(False, p1)


SideBar = tkinter.Frame(root,bg=_from_rgb((33, 40, 62)),width=1362)
SideBar.place(x=0,y=0,height=700)

user_logo=PhotoImage(file="Start.png")
user_label=Label(SideBar,image=user_logo)
user_label.place(x=0,y=-10)

b1=Button(SideBar,bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),bd=0,width=32,text="Explore",font = "Verdana 10 bold",command=dash)
b1.place(x=525,y=360,height=40)

root.mainloop()