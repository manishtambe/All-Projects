from tkinter import *
import os
from PIL import ImageTk

def Explore():
    root4.destroy()
    os.system('python C://Roadster//Major//drawv.py')

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

root4 = Tk()
root4.geometry("1280x800+150+20")
bg = ImageTk.PhotoImage(file="C://Roadster//Major//startup.jpg")
bg_image1 = Label(root4,image=bg).place(x=0, y=0, relwidth=1, relheight=1)
root4.overrideredirect(True)
root4.after(3000,Explore)
root4.mainloop()


















