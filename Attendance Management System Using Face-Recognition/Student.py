import pathlib
import cv2 as cv
import mysql.connector
import os
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import re

def reset():
    t3.delete(0, 'end')
    t4.delete(0, 'end')
    t5.delete(0, 'end')
    t6.delete(0, 'end')
    t7.delete(0, 'end')
    comb.set("Select From List")
    t8.delete(0, 'end')
    comb1.set("Select From List")
def mouseclick(event):
    messagebox.showinfo("Information", "You Are Redirected To The Dashboard Please Wait....!")
    cap.release()
    top.destroy()
    os.system('python C://Roadster//Major//dashboard.py')

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb
#--------------------------------------------------------------Button Click Function--------------------------------------------------------
def takeinput():
    roll_no=t3.get()
    First_Name=t4.get()
    Last_Name=t5.get()
    Mobile_No=t6.get()
    Email_Id=t7.get()
    Classroom=comb.get()
    Semester=t8.get()
    Folder=comb1.get()
    if roll_no=="":
        messagebox.showwarning("Warning", "Please Insert Roll-No!")
    else:
        if First_Name == "":
            messagebox.showwarning("Warning", "Please Insert First Name!")
        else:
            if Last_Name == "":
                messagebox.showwarning("Warning", "Please Insert Last Name!")
            else:
                if Mobile_No == "":
                    messagebox.showwarning("Warning", "Please Insert Mobile No!")
                else:
                    if Email_Id == "":
                        messagebox.showwarning("Warning", "Please Insert Email Id!")
                    else:
                        if Classroom == "Select From List":
                            messagebox.showwarning("Warning", "Please Select Classroom From List!")
                        else:
                            if Semester == "":
                                messagebox.showwarning("Warning", "Please Insert Semester!")
                            else:
                                if Folder == "Select From List":
                                    messagebox.showwarning("Warning", "Please Select Folder From List!")
                                else:
                                    if roll_no.isdigit() != True:
                                        messagebox.showwarning("Warning", "Enter Proper Roll No!")
                                    elif First_Name.isalpha() != True:
                                        messagebox.showwarning("Warning", "Name must contain only alphabets!")
                                    elif Last_Name.isalpha() != True:
                                        messagebox.showwarning("Warning", "Name must contain only alphabets!")
                                    elif Mobile_No.isdigit() != True or len(Mobile_No) < 10 or len(Mobile_No) > 10:
                                        messagebox.showwarning("Warning", "Enter Proper Mobile No!")
                                    elif not re.search("@", Email_Id):
                                        messagebox.showwarning("Warning", "Enter Proper Email!")
                                    else:
                                        getInput(roll_no,First_Name,Last_Name,Mobile_No,Email_Id,Classroom,Semester,Folder)

def getInput(roll_no,First_Name,Last_Name,Mobile_No,Email_Id,Classroom,Semester,Folder):
    path = "C:/Roadster/Major/Attendance/" + Folder + "/"
    str = roll_no + "-" + First_Name + "-" + Last_Name + "-" + Classroom + ".png"
    path1 = path + str
    try:
        global attendance
        attendance="Absent"
        db = mysql.connector.connect(host="localhost",user="root",password="",db="classroom")
        cursor = db.cursor()
        savequery = "insert into "+Classroom+"(roll_no,First_Name,Last_Name,Mobile_No,Email_Id,Classroom,Semester,Attendance,Folder,Image_Name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #(savequery)
        try:
            cursor.execute(savequery,(roll_no,First_Name,Last_Name,Mobile_No,Email_Id,Classroom,Semester,attendance,Folder,str))
            db.commit()
            numrows = int(cursor.rowcount)
            if numrows == 1:
                messagebox.showinfo("Information","Entry Added Successfully!")
                messagebox.showinfo("Information", "Please Look Into Camera To Capture Image !")
                capture(roll_no,First_Name,Last_Name,Classroom,Folder,path1)
            else:
                messagebox.showerror("Error","Error Occur While Storing Data")
                reset()
        except mysql.connector.Error as e:
            messagebox.showinfo("Error",e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
    db.close()

def capture(roll_no,First_Name,Last_Name,Classroom,Folder,path1):
    imag = Image.fromarray(cv2image)
    file = pathlib.Path(path1)
    if file.exists():
        messagebox.showerror("Error", "Image already Exists Please Try Again!")
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", db="classroom")
            cursor = db.cursor()
            savequery = "delete from " + Classroom + " where Roll_No="+roll_no
            #print(savequery)
            try:
                numrows=0
                cursor.execute(savequery)
                db.commit()
                numrows = int(cursor.rowcount)
                #print(numrows)
                if numrows == 1:
                    messagebox.showerror("Error", "Please Add Student Data And Image Again !!")
                    os.remove(path1)
                    reset()
                else:
                    messagebox.showerror("Error", "Error Occur While Storing Data please manually delete your data ")
                    reset()
            except mysql.connector.Error as e:
                messagebox.showinfo("Error", e)
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
        db.close()
    else:
        imag.save(path1)
        messagebox.showinfo("Information", "Image Successfully  Added !")
        reset()
#--------------------------------------------------------Classroom Combo-Box Methods--------------------------------------------------------
def combo_input():
    db = mysql.connector.connect(host="localhost",user="root",password="",db="classroom")
    cursor = db.cursor()
    savequery = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='" + "classroom" + "'"
    cursor.execute(savequery)

    result = []

    for row in cursor.fetchall():
        result.append(row[0])

    return result

def OptionCallBack(*args):
   variable.get()

#------------------------------------------------------------Folder Combo-Box Methods-------------------------------------------------------------------
def combo_input1():
    directory = ''
    parent_dir = "C:/Roadster/Major/Attendance"
    path = os.path.join(parent_dir, directory)

    result1 = []
    my_list = os.listdir(parent_dir)

    for dirname in list(my_list):
        result1.append(dirname)
    return result1

def OptionCallBack1(*args):
    variable1.get()
#-------------------------------------------------------------------------------------------------------------------------------------------------------
top = Tk()
top.geometry("1132x615+110+60")
top.resizable(0, 0)
top.title("New Student")
p1 = PhotoImage(file = 'C://Roadster//Major//icont.png')
top.iconphoto(False, p1)
top.overrideredirect(True)


Frame_Login = Frame(top,bg=_from_rgb((33, 40, 62)))
Frame_Login.place(x=0,y=0,height=615,width=1132)

variable = StringVar(top)
variable.set("Select From List")
variable.trace('w', OptionCallBack)

variable1 = StringVar(top)
variable1.set("Select From List")
variable1.trace('w', OptionCallBack1)

directory = ''
parent_dir = "C:/Roadster/Major/Attendance"
path = os.path.join(parent_dir, directory)

cap = cv.VideoCapture(1)

previous=ImageTk.PhotoImage(file="C://Roadster//Major//previous.png")
previous_image=Label(Frame_Login,image=previous,bg=_from_rgb((33, 40, 62)))
previous_image.bind("<Button>", mouseclick)
previous_image.place(x=0,y=20)

l1=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Roll No:-",font = "Verdana 15 bold").place(x=61,y=60)
l2=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="First Name: -",font = "Verdana 15 bold").place(x=21,y=120)
l3=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Last Name: -",font = "Verdana 15 bold").place(x=25,y=180)
l4=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Mobile No: -",font = "Verdana 15 bold").place(x=30,y=240)
l5=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Email Id: -",font = "Verdana 15 bold").place(x=50,y=300)
l6=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Classroom: -",font = "Verdana 15 bold").place(x=28,y=360)
l7=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Semester: -",font = "Verdana 15 bold").place(x=40,y=420)
l8=Label(Frame_Login,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Folder: -",font = "Verdana 15 bold").place(x=76,y=480)

t3=Entry(Frame_Login,bg=_from_rgb((0,200,244)),width=17, highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t3.place(height=30,x=181,y=60)

t4=Entry(Frame_Login,bg=_from_rgb((0,200,244)),width=17, highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t4.place(height=30,x=181,y=120)

t5=Entry(Frame_Login,bg=_from_rgb((0,200,244)),width=17, highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t5.place(height=30,x=181,y=180)

t6=Entry(Frame_Login,bg=_from_rgb((0,200,244)),width=17, highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t6.place(height=30,x=181,y=240)

t7=Entry(Frame_Login,bg=_from_rgb((0,200,244)),width=17, highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t7.place(height=30,x=181,y=300)

comb = ttk.Combobox(Frame_Login,width=36,background=_from_rgb((0,200,244)),textvariable=variable)
comb.place(x=181,y=360,height=30)
comb['value'] = combo_input()

t8=Entry(Frame_Login,bg=_from_rgb((0,200,244)),width=17, highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t8.place(height=30,x=181,y=420)

comb1 = ttk.Combobox(Frame_Login,width=36,background=_from_rgb((0,200,244)),textvariable=variable1)
comb1.place(x=181,y=480,height=30)
comb1['value'] = combo_input1()

b12=Button(Frame_Login,bg=_from_rgb((0,200,244)),bd=0,width=32,text="Save & Capture",font = "Verdana 10 bold",fg="white",command=takeinput)
b12.place(x=391,y=540,height=35)

f1=LabelFrame(top,bg=_from_rgb((0,200,244)),width=560,height=450)
f1.place(x=500,y=58)

l9=Label(f1,bg=_from_rgb((0,200,244)),width=551,height=442)
l9.place(x=0,y=0)

def show_frame():
    global img
    global cv2image
    global frame
    _, frame = cap.read()
    frame = cv.flip(frame, 1)
    cv2image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    l9.imgtk = imgtk
    l9.configure(image=imgtk)
    l9.after(10, show_frame)
show_frame()
top.mainloop()













