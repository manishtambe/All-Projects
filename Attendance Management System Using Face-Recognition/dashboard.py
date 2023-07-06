import tkinter
import pandas.io.sql as sql
from pymysql import*
import pathlib
import mysql.connector
import os
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import webbrowser
import re

def clearall():
    t1.delete(0, 'end')
    classroom.delete(*classroom.get_children())
#-------------------------------------------------------tab3 Manage Student-----------------------------------------------------------------------------------
def reset():
    std_Roll_no_insert.delete(0, 'end')
    std_fname_insert.delete(0, 'end')
    std_lname_insert.delete(0, 'end')
    std_mobile_insert.delete(0, 'end')
    std_Email_Id_insert.delete(0, 'end')
    std_branch_insert.delete(0, 'end')
    std_Semester_insert.delete(0, 'end')

def updatestudentdetails(event):
    Roll_No=std_Roll_no_insert.get()
    First_Name=std_fname_insert.get()
    Last_Name=std_lname_insert.get()
    Mobile_No=std_mobile_insert.get()
    Email_Id=std_Email_Id_insert.get()
    classroom=std_branch_insert.get()
    Semester=std_Semester_insert.get()
    Folder=fol.get()
    Image_Name=img_name.get()
    if Roll_No == "":
        messagebox.showwarning("Warning", "Please Insert Roll No!")
    else:
        if First_Name == "":
            messagebox.showwarning("Warning", "Please Insert First Name!")
        else:
            if Last_Name == "":
                messagebox.showwarning("Warning", "Please Insert Last Name!")
            else:
                if Mobile_No == "":
                    messagebox.showwarning("Warning", "Please Insert Mobile_No!")
                else:
                    if Email_Id == "":
                        messagebox.showwarning("Warning", "Please Insert Email Id!")
                    elif re.search("[-+_!#$%^&*()<>?/\|}{~:]", Email_Id):
                        messagebox.showwarning("Warning", "Please Insert Valid Gmail Id")
                    else:
                        if classroom == "":
                            messagebox.showwarning("Warning", "Please Insert Branch!")
                        else:
                            if Semester == "":
                                messagebox.showwarning("Warning", "Please Insert Semester!")
                            else:
                                updatestudent(Roll_No,First_Name,Last_Name,Mobile_No,Email_Id,classroom,Semester,Folder,Image_Name)
def updatestudent(Roll_No,First_Name,Last_Name,Mobile_No,Email_Id,classroom,Semester,Folder,Image_Name):
    path = "C:/Roadster/Major/Attendance/" + Folder + "/"
    str = Image_Name
    path1 = path + str
    file = pathlib.Path(path1)

    str1 = Roll_No + "-" + First_Name + "-" + Last_Name + "-" + classroom + ".png"
    path2 = path + str1
    file1 = pathlib.Path(path2)
    if file.exists():
            try:
                db = mysql.connector.connect(host="localhost", user="root", password="", db="classroom")
                cursor = db.cursor()
                savequery = "UPDATE "+ classroom +" SET First_Name='"+First_Name+"'"+",Last_Name='"+Last_Name+"'"+",Mobile_No='"+Mobile_No+"'"+",Email_Id='"+Email_Id+"'"+",Classroom='"+classroom+"'"+",Semester='"+Semester+"'"+",Folder='"+Folder+"'"+",Image_Name='"+str1+"'"+" WHERE Roll_No="+Roll_No
                #print(savequery)
                try:
                    cursor.execute(savequery)
                    db.commit()
                    numrows = int(cursor.rowcount)  # int(cursor.rowcount)
                    #print(numrows)
                    if numrows == 1:
                        rename(file,file1)
                    else:
                        messagebox.showerror("Error", "Invalid Details Or Same Data Has Been Entered Please Retry!")
                        reset()
                        resetalltable()
                except mysql.connector.Error as e:
                    messagebox.showinfo("Error", e)
            except mysql.connector.Error as e:
                messagebox.showinfo("Error", e)
            db.close()
    else:
        messagebox.showwarning("warning","Image Not Found!")
def rename(file,file1):
    try:
        os.rename(file,file1)
        messagebox.showinfo("information","Student Details Successfully Changed")
        reset()
        resetalltable()
    except OSError as error:
        messagebox.showinfo("Error", error)
        reset()
        resetalltable()

def capturestudentdetails(event):
    Roll_No=std_Roll_no_insert.get()
    First_Name=std_fname_insert.get()
    Last_Name=std_lname_insert.get()
    Mobile_No=std_mobile_insert.get()
    Email_Id=std_Email_Id_insert.get()
    classroom=std_branch_insert.get()
    Semester=std_Semester_insert.get()
    Folder=fol.get()
    Image_Name=img_name.get()
    if Roll_No == "":
        messagebox.showwarning("Warning", "Please Insert Roll No!")
    else:
        if First_Name == "":
            messagebox.showwarning("Warning", "Please Insert First Name!")
        else:
            if Last_Name == "":
                messagebox.showwarning("Warning", "Please Insert Last Name!")
            else:
                if Mobile_No == "":
                    messagebox.showwarning("Warning", "Please Insert Mobile_No!")
                else:
                    if Email_Id == "":
                        messagebox.showwarning("Warning", "Please Insert Email Id!")
                    else:
                        if classroom == "":
                            messagebox.showwarning("Warning", "Please Insert Branch!")
                        else:
                            if Semester == "":
                                messagebox.showwarning("Warning", "Please Insert Semester!")
                            else:
                                delatestudent(Roll_No,First_Name,Last_Name,Mobile_No,Email_Id,classroom,Semester,Folder,Image_Name)

def delatestudent(Roll_No,First_Name,Last_Name,Mobile_No,Email_Id,classroom,Semester,Folder,Image_Name):
    path = "C:/Roadster/Major/Attendance/" + Folder + "/"
    #print(Roll_No,First_Name,Last_Name,Mobile_No,Email_Id,classroom,Semester,Folder,Image_Name)
    str = Image_Name
    path1 = path + str
    file = pathlib.Path(path1)
    if file.exists():
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", db="classroom")
            cursor = db.cursor()
            savequery = "DELETE FROM `"+classroom+"` WHERE Roll_No="+Roll_No+ " AND First_Name='" + First_Name + "'" + " AND Last_Name='" + Last_Name + "'" + " AND Mobile_No='" + Mobile_No + "'" + " AND Email_Id='" + Email_Id + "'" + " AND Classroom='" + classroom + "'" + " AND Semester='" + Semester + "'" + " AND Folder='" + Folder + "'" +" AND Image_Name='" + Image_Name + "'"
            #print(savequery)
            try:
                numrows=0
                cursor.execute(savequery)
                db.commit()
                numrows = int(cursor.rowcount)
                #print(numrows)
                if numrows == 1:
                    os.remove(path1)
                    messagebox.showinfo('information',"Entry Successfully Deleted")
                    reset()
                    resetalltable()
                else:
                    messagebox.showerror("Error", "Error Occur While Deleting Data please manually delete your data ")
                    reset()
            except mysql.connector.Error as e:
                messagebox.showinfo("Error", e)
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
        db.close()
    else:
        messagebox.showerror("Error", "The Image that you trying to delete is not present!")
def resetalltable():
    Studentdata.delete(*Studentdata.get_children())
def clearalltable():
    comb_st.set("Select From List")
    Studentdata.delete(*Studentdata.get_children())
def select():
    classr=comb_st.get()
    if classr == "Select From List":
        messagebox.showwarning("Warning", "Please Select Classroom From List!")
    else:
        fetch_student(classr)

def fetch_student(classr):
    clearalltable()
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="classroom")
        cursor = db.cursor()
        savequery = "select Roll_No, First_Name, Last_Name, Mobile_No, Email_Id, Classroom, Semester, Folder, Image_Name from "+classr
        #print(savequery)
        try:
            cursor.execute(savequery)
            rows = cursor.fetchall()
            update_student(rows)
        except mysql.connector.Error as e:
            messagebox.showinfo("Error",e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
    db.close()

def update_student(rows):
    for i in rows:
        Studentdata.insert('','end',values=i)

def combo_input3():
    db = mysql.connector.connect(host="localhost",user="root",password="",db="classroom")
    cursor = db.cursor()
    savequery = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='" + "classroom" + "'"
    cursor.execute(savequery)

    result = []

    for row in cursor.fetchall():
        result.append(row[0])

    return result

def OptionCallBack3(*args):
    variable3.get()

def getrow_studentdb(event):
    rowid = Studentdata.identify_row(event.y)
    item = Studentdata.item(Studentdata.focus())
    e6.set(item['values'][0])
    e7.set(item['values'][1])
    e8.set(item['values'][2])
    e9.set(item['values'][3])
    e10.set(item['values'][4])
    e11.set(item['values'][5])
    e12.set(item['values'][6])
    fol.set(item['values'][7])
    img_name.set(item['values'][8])
#-------------------------------------------------------tab4 Attendance---------------------------------------------------------------------------------------
def start():
    global classroom
    global teacher
    global folder
    global subject
    classroom=comb_class.get()
    teacher=comb_ter.get()
    folder=comb_folder.get()
    subject=Subject.get()
    if classroom == "":
        messagebox.showwarning("warning","Please Select The Classroom!")
    else:
        if teacher == "":
            messagebox.showwarning("warning","Please Select The Teacher Name!")
        else:
            if folder == "":
                messagebox.showwarning("warning","Please Select The Folder!")
            else:
                if subject == "":
                    messagebox.showwarning("warning","Please Insert The Subject")
                else:
                    storedata(classroom,teacher,folder,subject)
def storedata(classroom,teacher,folder,subject):
    try:
        database='data'
        db = mysql.connector.connect(host="localhost",user="root",password="",db="temp")
        cursor = db.cursor()
        savequery = "insert into "+database+"(Classroom,Teacher_Name,Folder_Name,Subject) values (%s,%s,%s,%s)"
        #print(savequery)
        try:
            cursor.execute(savequery,(classroom,teacher,folder,subject))
            db.commit()
            numrows = int(cursor.rowcount)
            if numrows == 1:
                messagebox.showinfo("Information","Entry Added Successfully Now You Are Redirected To The Attendance Window!")
                messagebox.showinfo("Information","Press 'Esc' To Exit From The Attendance Window !")
                reset_att()
                os.system("python C://Roadster//Major//AttendanceCapture.py")
            else:
                messagebox.showerror("Error","Error Occur While acquiring data")
                reset_att()
        except mysql.connector.Error as e:
            messagebox.showinfo("Error",e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
    db.close()

def reset_att():
    comb_class.set("Select From List")
    comb_ter.set("Select From List")
    comb_folder.set("Select From List")
    Subject.delete(0, 'end')
def input_teacher():
    db = mysql.connector.connect(host="localhost",user="root",password="",db="attendance")
    cursor = db.cursor()
    savequery = "SELECT CONCAT(Fname, ' ', Lname) AS Fname FROM teacherdb"
    cursor.execute(savequery)

    result = []

    for row in cursor.fetchall():
        result.append(row[0])

    return result

def OptionCallBack_ter(*args):
    variable_std.get()

def input_classroom():
    db = mysql.connector.connect(host="localhost",user="root",password="",db="classroom")
    cursor = db.cursor()
    savequery = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='" + "classroom" + "'"
    cursor.execute(savequery)

    result = []

    for row in cursor.fetchall():
        result.append(row[0])

    return result

def OptionCallBack_class(*args):
    variable_class.get()

def input_folder():
    directory = ''
    parent_dir = "C:/Roadster/Major/Attendance"
    path = os.path.join(parent_dir, directory)

    result1 = []
    my_list = os.listdir(parent_dir)

    for dirname in list(my_list):
        result1.append(dirname)
    return result1


def OptionCallBack_fol(*args):
    variable_fol.get()
#-------------------------------------------------------tab5 Generate Report Function-------------------------------------------------------------------------
def clearreport():
    comb.set("Select From List")
    t3.delete(0, 'end')

def combo_input():
    db = mysql.connector.connect(host="localhost",user="root",password="",db="attendance")
    cursor = db.cursor()
    savequery = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='" + "classroom" + "'"
    cursor.execute(savequery)

    result = []

    for row in cursor.fetchall():
        result.append(row[0])

    return result

def OptionCallBack(*args):
    variable.get()

def getdata():
    Branch = comb.get()
    name = t3.get()
    if Branch == "Select From List":
        messagebox.showwarning("Warning", "Please Select Classroom From List To Generate Report!")
    else:
        if name == "":
            messagebox.showwarning("Warning", "Please Enter The File Name To Store The File!")
        else:
            path1 = "C:/Roadster/Major/reports/"
            str1 = name + ".xlsx"
            path2 = path1 + str1
            file = pathlib.Path(path2)
            if file.exists():
                messagebox.showwarning("Warning", "File Name Already Exists Please Choose Different File Name!")
                clearreport()
            else:
                generate(Branch,path2)

def generate(Branch,path2):
    try:
        con=connect(user="root",password="",host="localhost",database="classroom")
        query="select Roll_No, First_Name, Last_Name, Mobile_No, Email_Id, Classroom, Semester, Subject, Teacher, Date, Attendance from "+Branch
        try:
            df = sql.read_sql(query, con)
            df.to_excel(path2)
            messagebox.showinfo("information","Report Successfully Generated")
            clearreport()
            updatetable(Branch)
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
def updatetable(Branch):
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", db="classroom")
        cursor = db.cursor()
        savequery = "update "+Branch+" SET Subject = Null,Teacher = Null,Date = Null,Attendance = 'Absent'"
        #print(savequery)
        try:
            cursor.execute(savequery)
            db.commit()
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()
#-------------------------------------------------------manage tecaher-----------------------------------------------------------------------------------
def fetch_teacher():
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="attendance")
        cursor = db.cursor()
        savequery = "SELECT id,Fname,Lname,Email FROM teacherdb"
        #print(savequery)
        try:
            cursor.execute(savequery)
            rows = cursor.fetchall()
            update_teacher(rows)
        except mysql.connector.Error as e:
            messagebox.showinfo("Error",e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
    db.close()

def update_teacher(rows):
    for i in rows:
        teacherdata.insert('','end',values=i)

def getrow_teacherdb(event):
    rowid = teacherdata.identify_row(event.y)
    item = teacherdata.item(teacherdata.focus())
    id.set(item['values'][0])
    e3.set(item['values'][1])
    e4.set(item['values'][2])
    e5.set(item['values'][3])
def mouseClickremove(event):
    teacherid=id.get()
    faname=fname_insert.get()
    lname=lname_insert.get()
    email=email_insert.get()
    if faname=="":
        messagebox.showwarning("Warning", "Please Enter First Name!")
    else:
        if lname=="":
             messagebox.showwarning("Warning", "Please Enter Last Name!")
        else:
            if email=="":
                messagebox.showwarning("Warning", "Please Enter Email Id!")
            else:
                removeteacher(teacherid,faname,lname,email)

def mouseClickadd(event):
    teacherid=id.get()
    faname=fname_insert.get()
    lname=lname_insert.get()
    email=email_insert.get()
    if faname=="":
        messagebox.showwarning("Warning", "Please Enter First Name!")
    else:
        if lname=="":
             messagebox.showwarning("Warning", "Please Enter Last Name!")
        else:
            if email=="":
                messagebox.showwarning("Warning", "Please Enter Email Id!")
            else:
                addteacher(teacherid,faname,lname,email)
def addteacher(teacherid,faname,lname,email):
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", db="attendance")
        cursor = db.cursor()
        savequery = "UPDATE teacherdb SET Fname='"+faname+"'"+",Lname='"+lname+"'"+",Email='"+email+"'"+" WHERE id="+str(teacherid)
        #print(savequery)
        try:
            cursor.execute(savequery)
            db.commit()
            numrows = int(cursor.rowcount)
            #print(numrows)
            if numrows == 1:
                messagebox.showinfo("Information","Details Updated Successfully!")
                clearteacher()
                fetch_teacher()
            else:
                messagebox.showerror("Error", "Invalid Details Or Same Data Has Been Entered Please Retry!")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()
    clearteacher()
    fetch_teacher()
def removeteacher(teacherid,faname,lname,email):
    #print(teacherid)
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="attendance")
        cursor = db.cursor()
        savequery="DELETE FROM `teacherdb` WHERE id= "+str(teacherid)+" AND Fname='"+faname+"'"+" AND Lname='"+lname+"'"+" AND Email='"+email+"'"
        try:
            cursor.execute(savequery)
            db.commit()
            numrows = int(cursor.rowcount)
            #print(numrows)
            if numrows == 1:
                messagebox.showinfo("Information","Entry Deleted Successful!")
                clearteacher()
                fetch_teacher()

            else:
                messagebox.showerror("Error", "Invalid Teacher Data Please Retry!")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()
    clearteacher()
    fetch_teacher()
def clearteacher():
    id.set("")
    fname_insert.delete(0, 'end')
    lname_insert.delete(0, 'end')
    email_insert.delete(0, 'end')
    teacherdata.delete(*teacherdata.get_children())

#-------------------------------------------------------folder functions------------------------------------------------------
def add1():
    filename = t2.get()
    directory = filename
    parent_dir = "C:/Roadster/Major/Attendance"
    path = os.path.join(parent_dir, directory)
    if(directory == ""):
        messagebox.showwarning("Warning", "Please Enter Folder Name To Add!")
    elif re.search("[@+_!#$%^&*()<>?/\|}{~:]", directory):
        messagebox.showwarning("Warning", "Name should not contain special chars except '-'")
    else:
        try:
            os.mkdir(path)
            messagebox.showinfo("Information", "Folder Successfully Created!")
        except OSError as error:
            messagebox.showinfo("Error", error)
    clearall1()
    update1(parent_dir)

def clearall1():
    t2.delete(0, 'end')
    filecontain.delete(*filecontain.get_children())

def delete_fol():
    filename = t2.get()
    directory = filename
    parent_dir = "C:/Roadster/Major/Attendance"
    path = os.path.join(parent_dir, directory)
    if (directory == ""):
        messagebox.showwarning("Warning", "Please Enter Folder Name To Delete!")
    else:
        try:
            os.rmdir(path)
            messagebox.showinfo("Information", "Folder Successfully Deleted!")
        except OSError as error:
            messagebox.showinfo("Error", error)
    clearall1()
    update1(parent_dir)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def add():
    classname = t1.get()
    #print(classname)
    if (classname == ""):
        messagebox.showwarning("Warning", "Please Enter Classroom Name To Add!")
    elif re.search("[-@+_!#$%^&*()<>?/\|}{~:]", classname):
        messagebox.showwarning("Warning", "Name should not contain special characters")
    else:
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", db="classroom")
            cursor = db.cursor()
            savequery = "SHOW TABLES LIKE '" + classname + "'"
            #print(savequery)
            try:
                cursor.execute(savequery)
                rows = cursor.fetchall()
                numrows = int(cursor.rowcount)
                #print(numrows)
                if numrows == 1:
                    messagebox.showerror("Error", "Classroom already exists!")
                else:
                    addall(classname)
            except mysql.connector.Error as e:
                messagebox.showinfo("Error", e)
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
        db.close()

def addall(classname):
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", db="classroom")
        cursor = db.cursor()
        savequery = "CREATE TABLE "+classname+"(Roll_No int PRIMARY KEY,First_Name varchar(20) NOT Null,Last_Name varchar(20) NOT Null,Mobile_No varchar(10) UNIQUE NOT Null,Email_Id varchar(30) UNIQUE NOT Null,Classroom varchar(10) NOT Null,Semester varchar(10) NOT Null,Subject varchar(20) Null,Teacher varchar(20) Null, Date date Null,Attendance varchar(10) Null,Folder varchar(10) Null,Image_Name varchar(50))";
        #print(savequery)
        try:
            cursor.execute(savequery)
            messagebox.showinfo("Information", "Classroom Successfully Created!")
            clearall()
            fetch()
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()

def delete():
    classname = t1.get()
    #print(classname)
    if(classname==""):
        messagebox.showwarning("Warning", "Please Enter Classroom Name To Delete!")
    else:
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", db="classroom")
            cursor = db.cursor()
            savequery = "SHOW TABLES LIKE '"+classname+"'"
            #print(savequery)
            try:
                cursor.execute(savequery)
                rows = cursor.fetchall()
                numrows = int(cursor.rowcount)
                #print(numrows)
                if numrows == 1:
                    remove(classname)
                else:
                    messagebox.showerror("Error", "Invalid Classroom Name Please Retry!")
            except mysql.connector.Error as e:
                messagebox.showinfo("Error", e)
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
        db.close()

def remove(classname):
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", db="classroom")
        cursor = db.cursor()
        savequery = "drop table if exists "+classname
        #print(savequery)
        try:
            cursor.execute(savequery)
            messagebox.showinfo("Information", "Classroom Successfully Deleted!")
            clearall()
            fetch()
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()

def update(rows):
    for i in rows:
        classroom.insert('','end',values=i)

def fetch():
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="classroom")
        cursor = db.cursor()
        savequery = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='" + "classroom" + "'"
        #print(savequery)
        try:
            cursor.execute(savequery)
            rows = cursor.fetchall()
            update(rows)
        except mysql.connector.Error as e:
            messagebox.showinfo("Error",e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
    db.close()

def update1(dirname):
    my_list = os.listdir(dirname)
    for dirname in list(my_list):
        filecontain.insert('','end',values=dirname)

def mouseClick(event):
  messagebox.showwarning("Warning", "Do You Want To Logout?")
  #cap.release()
  top.destroy()
  os.system('python C://Roadster//Major//drawv.py')

def getrow_fol(event):
    rowid = filecontain.identify_row(event.y)
    item = filecontain.item(filecontain.focus())
    e2.set(item['values'][0])

def getrow(event):
    rowid = classroom.identify_row(event.y)
    item = classroom.item(classroom.focus())
    e1.set(item['values'][0])

def Home():
    tabControl.select(0)
def Classroom():
    tabControl.select(1)
def Addstudent():
    messagebox.showinfo("Information", "You Are Redirected To The Another Page Please Wait For A Sec..!")
    top.destroy()
    os.system('python C://Roadster//Major//Student.py')
def managestudent():
    tabControl.select(2)
def Attendance():
    tabControl.select(3)
def Generatereport():
    tabControl.select(4)
def teacher():
    tabControl.select(5)
def about():
    tabControl.select(6)

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def urlopen():
    url = 'https://mmt-roadster-systems.netlify.app/'
    webbrowser.open(url)

top = Tk()
top.geometry("1362x700+50+50")
top.resizable(0, 0)
top.title("Dashboard")
p1 = PhotoImage(file = 'C://Roadster//Major//icont.png')
top.iconphoto(False, p1)
e1 = StringVar()
e2 = StringVar()
e3 = StringVar()
e4 = StringVar()
e5 = StringVar()
id = StringVar()

style = ttk.Style()
style.theme_use("clam")
style.layout('TNotebook.Tab', [])
style.configure("Treeview.Heading", background="black",fieldbackground="black",foreground="white")

variable = StringVar(top)
variable.set("Select From List")
variable.trace('w', OptionCallBack)

directory = ''
parent_dir = "C:/Roadster/Major/Attendance"
path = os.path.join(parent_dir, directory)

variable_std = StringVar(top)
variable_std.set("Select From List")
variable_std.trace('w', OptionCallBack_ter)

variable_class = StringVar(top)
variable_class.set("Select From List")
variable_class.trace('w', OptionCallBack_class)

variable_fol = StringVar(top)
variable_fol.set("Select From List")
variable_fol.trace('w', OptionCallBack_fol)

variable3 = StringVar(top)
variable3.set("Select From List")
variable3.trace('w', OptionCallBack3)

e6 = StringVar()
e7 = StringVar()
e8 = StringVar()
e9 = StringVar()
e10 = StringVar()
e11 = StringVar()
e12 = StringVar()
fol = StringVar()
img_name = StringVar()

bg=ImageTk.PhotoImage(file="C://Roadster//Major//back.jpg")
bg_image=Label(top,image=bg).place(x=0,y=0,relwidth=1,relheight=1)

Frame_Login = Frame(top,bg=_from_rgb((33, 40, 62)))
Frame_Login.place(x=0,y=0,height=695,width=230)

Frame_Login1 = Frame(top,bg=_from_rgb((255, 255, 255)))
Frame_Login1.place(x=230,y=0,height=80,width=1132) #height=80

user_logo=ImageTk.PhotoImage(file="C://Roadster//Major//user.png")
user_label=Label(Frame_Login1,image=user_logo,bg=_from_rgb((255, 255, 255)))
user_label.place(x=-325,y=-5,relwidth=1,relheight=1)

logout_logo=ImageTk.PhotoImage(file="C://Roadster//Major//logout.png")
logout_logo1=Label(Frame_Login1,image=logout_logo,bg=_from_rgb((255, 255, 255)))
logout_logo1.bind("<Button>", mouseClick)
logout_logo1.place(x=1090,y=40)

logout_label=Label(Frame_Login1,text="Logout",bg=_from_rgb((255, 255, 255)),font="Verdana 10 bold")
logout_label.bind("<Button>", mouseClick)
logout_label.place(x=1030,y=43)

Title=Label(Frame_Login1,text="Attendance Management System",bg='white',font="Verdana 25 bold")
Title.place(x=280,y=10)

separator = ttk.Separator(Frame_Login1,orient="horizontal")
separator.place(x=8,y=70,width=1110 )

#------------------------------------------------------------Tab Section-----------------------------------------------------------
tabControl = ttk.Notebook(top)

tab1 = Frame(tabControl, background=_from_rgb((33, 40, 62)))
tab2 = Frame(tabControl, background=_from_rgb((33, 40, 62)))
tab3 = Frame(tabControl, background=_from_rgb((33, 40, 62)))
tab4 = Frame(tabControl, background=_from_rgb((33, 40, 62)))
tab5 = Frame(tabControl, background=_from_rgb((33, 40, 62)))
tab6 = Frame(tabControl, background=_from_rgb((33, 40, 62)))
tab7 = Frame(tabControl, background=_from_rgb((33, 40, 62)))

tabControl.add(tab1, text ='Tab 1')
tabControl.add(tab2, text ='Tab 2')
tabControl.add(tab3, text ='Tab 3')
tabControl.add(tab4, text ='Tab 4')
tabControl.add(tab5, text ='Tab 5')
tabControl.add(tab6, text ='Tab 6')
tabControl.add(tab7, text ='Tab 7')
tabControl.place(x=230,y=80,height=615,width=1132)
#---------------------------------------------------Side Menu---------------------------------------------------------------------
menu_logo=ImageTk.PhotoImage(file="C://Roadster//Major//menu.png")
menu = Label(Frame_Login,image=menu_logo,bg=_from_rgb((33, 40, 62)))
menu.place(x=0,y=50)

logo=ImageTk.PhotoImage(file="C://Roadster//Major//logo.png")
logo_label=Label(Frame_Login,image=logo,bg=_from_rgb((33, 40, 62)))
logo_label.place(x=80,y=0)

b1=Button(Frame_Login,bg=_from_rgb((0,200,244)),bd=0,width=25,text="Home",font = "Verdana 10 bold",fg="white",command=Home)
b1.place(x=0,y=83,height=35)

b2=Button(Frame_Login,bg=_from_rgb((0,200,244)),bd=0,width=25,text="Classrooms",font = "Verdana 10 bold",fg="white",command=Classroom)
b2.place(x=0,y=162,height=35)

b3=Button(Frame_Login,bg=_from_rgb((0,200,244)),bd=0,width=25,text="Add Student",font = "Verdana 10 bold",fg="white",command=Addstudent)
b3.place(x=0,y=244,height=35)

b3=Button(Frame_Login,bg=_from_rgb((0,200,244)),bd=0,width=25,text="Manage Student",font = "Verdana 10 bold",fg="white",command=managestudent)
b3.place(x=0,y=326,height=35)

b4=Button(Frame_Login,bg=_from_rgb((0,200,244)),bd=0,width=25,text="Attendance",font = "Verdana 10 bold",fg="white",command=Attendance)
b4.place(x=0,y=406,height=35)

b5=Button(Frame_Login,bg=_from_rgb((0,200,244)),bd=0,width=25,text="Generate Report",font = "Verdana 10 bold",fg="white",command=Generatereport)
b5.place(x=0,y=492,height=35)

b6=Button(Frame_Login,bg=_from_rgb((0,200,244)),bd=0,width=25,text="Manage Teacher",font = "Verdana 10 bold",fg="white",command=teacher)
b6.place(x=0,y=576,height=35)

b7=Button(Frame_Login,bg=_from_rgb((0,200,244)),bd=0,width=25,text="About",font = "Verdana 10 bold",fg="white",command=urlopen)
b7.place(x=0,y=657,height=35)


#----------------------------------------------------------Classroom Section-----------------------------------------------------
heading = Label(tab2,bg=_from_rgb((33, 40, 62)),bd=0,width=25,text="Manage Classrooms",font = "Verdana 15 bold",fg=_from_rgb((0,200,244)))
heading.place(x=85,y=17)

classroom = ttk.Treeview(tab2,columns=(1),show="headings",height="12")
classroom.bind('<Double 1>',getrow)
classroom.place(x=110,y=70,width="300")
classroom.heading(1,text="Classrooms")
classroom.column(1, anchor=tkinter.N)
fetch()


class_label=Label(tab2,bg=_from_rgb((33, 40, 62)),bd=0,width=25,text="Classroom: -",font = "Verdana 12 bold",fg=_from_rgb((0,200,244)))
class_label.place(x=25,y=355)

t1=Entry(tab2,bg=_from_rgb((33,40,62)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold",textvariable=e1)
t1.place(height=30,x=223,y=350)
separator = ttk.Separator(tab2,orient="horizontal")
separator.place(x=225,y=380,width=182 )

b8=Button(tab2,bg=_from_rgb((0,200,244)),bd=0,width=13,text="Add",font = "Verdana 10 bold",fg="white",command=add)
b8.place(x=110,y=400,height=35)

b9=Button(tab2,bg=_from_rgb((0,200,244)),bd=0,width=13,text="Delete",font = "Verdana 10 bold",fg="white",command=delete)
b9.place(x=284,y=400,height=35)

#--------------------------------------------Vertical Separator between two section-----------------------------------------------
separator = ttk.Separator(tab2, orient='vertical')
separator.place(relx=0.47, rely=0, relwidth=0, relheight=1)

#---------------------------------------------Folder Section----------------------------------------------------------------------
filecontain = ttk.Treeview(tab2,columns=(1),show="headings",height="12")
filecontain.bind('<Double 1>',getrow_fol)
filecontain.place(x=680,y=70,width="300")
filecontain.heading(1,text="Folders")
filecontain.column(1, anchor=tkinter.N)
update1(parent_dir)

heading_fol = Label(tab2,bg=_from_rgb((33, 40, 62)),bd=0,width=25,text="Manage Folders",font = "Verdana 15 bold",fg=_from_rgb((0,200,244)))
heading_fol.place(x=660,y=17)

t2=Entry(tab2,bg=_from_rgb((33,40,62)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold",textvariable=e2)
t2.place(height=30,x=793,y=350)
separator = ttk.Separator(tab2,orient="horizontal")
separator.place(x=795,y=380,width=182)

b10=Button(tab2,bg=_from_rgb((0,200,244)),bd=0,width=13,text="Add",font = "Verdana 10 bold",fg="white",command=add1)
b10.place(x=680,y=400,height=35)

b11=Button(tab2,bg=_from_rgb((0,200,244)),bd=0,width=13,text="Delete",font = "Verdana 10 bold",fg="white",command=delete_fol)
b11.place(x=860,y=400,height=35)

folder_label=Label(tab2,bg=_from_rgb((33, 40, 62)),bd=0,width=0,text="Folder: -",font = "Verdana 12 bold",fg=_from_rgb((0,200,244)))
folder_label.place(x=695,y=355)

#------------------------------------------------------tab1---------------------------------------------------------------------
bg_tab1=ImageTk.PhotoImage(file="C://Roadster//Major//tab.jpg")
bg_tab2=Label(tab1,image=bg_tab1)
bg_tab2.place(x=0,y=0,relwidth=1,relheight=1)
#------------------------------------------------------tab6----------------------------------------------------------------------

separator = ttk.Separator(tab6, orient='vertical')
separator.place(relx=0.49, rely=0, relwidth=0, relheight=1)

teacher_label=Label(tab6,bg=_from_rgb((33, 40, 62)),bd=0,width=0,text="Teachers Details",font = "Verdana 15 bold",fg=_from_rgb((0,200,244)))
teacher_label.place(x=200,y=17)


teacherdata = ttk.Treeview(tab6,columns=(1,2,3,4),show="headings",height="12")
teacherdata.bind('<Double 1>',getrow_teacherdb)
teacherdata.place(x=0,y=70,width="550")
teacherdata.heading(1,text="Id")
teacherdata.heading(2,text="First Name")
teacherdata.heading(3,text="Last Name")
teacherdata.heading(4,text="Email Id")
teacherdata.column(1, anchor=tkinter.N,minwidth=0, width=50, stretch=NO)
teacherdata.column(2, anchor=tkinter.N,minwidth=0, width=165, stretch=NO)
teacherdata.column(3, anchor=tkinter.N,minwidth=0, width=165, stretch=NO)
teacherdata.column(4, anchor=tkinter.N,minwidth=0, width=165, stretch=NO)
fetch_teacher()

Frame_Login = Frame(tab6,bg=_from_rgb((0,200,244)))
Frame_Login.place(x=630,y=70,height=280,width=430)

edit_logo=ImageTk.PhotoImage(file="C://Roadster//Major//edit.png")
edit_image=Label(tab6,image=edit_logo,bg=_from_rgb((0,200,244)))
edit_image.bind("<Button>",mouseClickadd)
edit_image.place(x=632,y=72)


save_logo=ImageTk.PhotoImage(file="C://Roadster//Major//shield.png")
save_image=Label(tab6,image=save_logo,bg=_from_rgb((0,200,244)))
save_image.bind("<Button>", mouseClickremove)
save_image.place(x=1022,y=72)

save_details=Label(tab6,text="Edit Teacher Details",bg=_from_rgb((0,200,244)),font = "Verdana 15 bold").place(x=732,y=72)

id_details=Label(tab6,text="Teacher Id: -",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Verdana 15 bold").place(x=670,y=144)
fname_details=Label(tab6,text="First Name: -",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Verdana 15 bold").place(x=671,y=200)
lname_details=Label(tab6,text="Last Name: -",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Verdana 15 bold").place(x=674,y=256)
email_details=Label(tab6,text="Email Id: -",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold").place(x=698,y=310)

id_insert_label=Label(tab6,bg=_from_rgb((0,200,244)),text="Auto Generated",width=13, highlightthickness=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 10 bold")
id_insert_label.place(height=30,x=825,y=148)

fname_insert=Entry(tab6,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e3)
fname_insert.place(height=30,x=825,y=200)
separator = ttk.Separator(tab6,orient="horizontal")
separator.place(x=826,y=230,width=182 )

lname_insert=Entry(tab6,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e4)
lname_insert.place(height=30,x=825,y=256)
separator = ttk.Separator(tab6,orient="horizontal")
separator.place(x=826,y=285,width=182 )

email_insert=Entry(tab6,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e5)
email_insert.place(height=30,x=825,y=310)
separator = ttk.Separator(tab6,orient="horizontal")
separator.place(x=826,y=340,width=182 )
#------------------------------------------------------------------------------tab 5 Report Generation------------------------------------------------------------------------------
Generate_Report=Label(tab5,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Generate Report",font = "Verdana 25 bold underline").place(x=420,y=10)
Classroom_Label=Label(tab5,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Classroom: -",font = "Verdana 15 bold").place(x=380,y=100)

Filename=Label(tab5,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="File Name: -",font = "Verdana 15 bold").place(x=388,y=180)

Note=Label(tab5,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="(Note: - Please Update Name Of Report & Delete Report Manually Located at D:\Reports)",font = "Verdana 10 bold").place(x=265,y=300)

comb = ttk.Combobox(tab5,width=36,background=_from_rgb((0,200,244)),textvariable=variable)
comb.place(x=540,y=100,height=30)
comb['value'] = combo_input()

t3=Entry(tab5,bg=_from_rgb((33,40,62)),width=17, highlightthickness=0,bd=0,justify=CENTER,fg="white",font = "Verdana 15 bold")
t3.place(height=30,x=540,y=180)
separator = ttk.Separator(tab5,orient="horizontal")
separator.place(x=540,y=210,width=243 )

b12=Button(tab5,bg=_from_rgb((0,200,244)),bd=0,width=13,text="Save Report",font = "Verdana 10 bold",fg="white",command=getdata)
b12.place(x=538,y=260,height=35)
#-----------------------------------------------------------------------tab-4 Attendace------------------------------------------------------------------------------
Attendance_Label=Label(tab4,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Take Attendance",font = "Verdana 25 bold underline").place(x=420,y=10)
classroom_Label=Label(tab4,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Classroom: -",font = "Verdana 15 bold").place(x=380,y=115)
Subject_Label=Label(tab4,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Teacher Name: -",font = "Verdana 15 bold").place(x=335,y=180)
Teacher_Label=Label(tab4,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Subject: -",font = "Verdana 15 bold").place(x=410,y=310)
Folder_Label=Label(tab4,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Folder Name: -",font = "Verdana 15 bold").place(x=352,y=245)

comb_class = ttk.Combobox(tab4,width=36,background=_from_rgb((0,200,244)),textvariable=variable_class)
comb_class.place(x=530,y=120,height=30)
comb_class['value'] = input_classroom()

comb_ter = ttk.Combobox(tab4,width=36,background=_from_rgb((0,200,244)),textvariable=variable_std)
comb_ter.place(x=530,y=180,height=30)
comb_ter['value'] = input_teacher()

comb_folder = ttk.Combobox(tab4,width=36,background=_from_rgb((0,200,244)),textvariable=variable_fol)
comb_folder.place(x=530,y=245,height=30)
comb_folder ['value'] = input_folder()


Subject=Entry(tab4,bg=_from_rgb((33, 40, 62)),width=17, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((0,200,244)),font = "Verdana 15 bold")
Subject.place(height=30,x=530,y=310)
separator = ttk.Separator(tab4,orient="horizontal")
separator.place(x=530,y=340,width=242 )

start=Button(tab4,bg=_from_rgb((0,200,244)),bd=0,width=13,text="Start",font = "Verdana 10 bold",fg="white",command=start)
start.place(x=530,y=400,height=35)

#----------------------------------------------------------------------------------------tab3 Manage Student------------------------------------------------------
separator3 = ttk.Separator(tab3, orient='vertical')
separator3.place(relx=0.49, rely=0, relwidth=0, relheight=1)

Student_label=Label(tab3,bg=_from_rgb((33, 40, 62)),bd=0,width=0,text="Students Details",font = "Verdana 15 bold",fg=_from_rgb((0,200,244)))
Student_label.place(x=200,y=17)

Studentdata = ttk.Treeview(tab3,columns=(1,2,3,4,5,6,7,8,9),show="headings",height="12")
Studentdata.bind('<Double 1>',getrow_studentdb)
Studentdata.place(x=0,y=70,width="555")
Studentdata.heading(1,text="Roll No")
Studentdata.heading(2,text="First Name")
Studentdata.heading(3,text="Last Name")
Studentdata.heading(4,text="Mobile No")
Studentdata.heading(5,text="Email Id")
Studentdata.heading(6,text="Branch")
Studentdata.heading(7,text="Semester")
Studentdata.heading(8,text="Folder")
Studentdata.heading(9,text="ImageName")
Studentdata.column(1, anchor=tkinter.N,minwidth=0, width=50, stretch=NO)
Studentdata.column(2, anchor=tkinter.N,minwidth=0, width=120, stretch=NO)
Studentdata.column(3, anchor=tkinter.N,minwidth=0, width=120, stretch=NO)
Studentdata.column(4, anchor=tkinter.N,minwidth=0, width=120, stretch=NO)
Studentdata.column(5, anchor=tkinter.N,minwidth=0, width=141, stretch=NO)
Studentdata.column(6, anchor=tkinter.N,minwidth=0, width=141, stretch=NO)
Studentdata.column(7, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
Studentdata.column(8, anchor=tkinter.N,minwidth=0, width=141, stretch=NO)
Studentdata.column(9, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)

Select_Classroom=Label(tab3,bg=_from_rgb((33,40,62)),fg=_from_rgb((0,200,244)),text="Select Classroom: -",font = "Verdana 15 bold")
Select_Classroom.place(x=40,y=380)

comb_st = ttk.Combobox(tab3,width=36,background=_from_rgb((0,200,244)),textvariable=variable3)
comb_st.place(x=280,y=383,height=30)
comb_st['value'] = combo_input3()

b13=Button(tab3,bg=_from_rgb((0,200,244)),bd=0,width=13,text="Select",font = "Verdana 10 bold",fg="white",command=select)
b13.place(x=225,y=445,height=35)

Frame_insert = Frame(tab3,bg=_from_rgb((0,200,244)))
Frame_insert.place(x=630,y=70,height=440,width=430)

edit_logo_student=ImageTk.PhotoImage(file="C://Roadster//Major//edit.png")
edit_image_student=Label(tab3,image=edit_logo_student,bg=_from_rgb((0,200,244)))
edit_image_student.bind("<Button>",updatestudentdetails)
edit_image_student.place(x=632,y=72)

save_student_details=Label(tab3,text="Edit Student Details",bg=_from_rgb((0,200,244)),font = "Verdana 15 bold")
save_student_details.place(x=732,y=72)

save_logo_student=ImageTk.PhotoImage(file="C://Roadster//Major//shield.png")
save_image_student=Label(tab3,image=save_logo_student,bg=_from_rgb((0,200,244)))
save_image_student.bind("<Button>", capturestudentdetails)
save_image_student.place(x=1022,y=72)

std_Roll_no=Label(tab3,text="Roll No: -",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Verdana 15 bold").place(x=710,y=144)
std_First_Name=Label(tab3,text="First Name: -",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Verdana 15 bold").place(x=671,y=200)
std_Last_Name=Label(tab3,text="Last Name: -",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Verdana 15 bold").place(x=674,y=256)
std_Mobile_no=Label(tab3,text="Mobile No: -",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold").place(x=680,y=310)
std_Email_Id=Label(tab3,text="Email Id: -",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold").place(x=700,y=364)
std_branch=Label(tab3,text="Classroom: -",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold").place(x=680,y=418)
std_Semester=Label(tab3,text="Semester: -",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold").place(x=690,y=472)


std_Roll_no_insert=Entry(tab3,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e6)
std_Roll_no_insert.place(height=30,x=825,y=145)
separator = ttk.Separator(tab3,orient="horizontal")
separator.place(x=826,y=175,width=182 )

std_fname_insert=Entry(tab3,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e7)
std_fname_insert.place(height=30,x=825,y=200)
separator = ttk.Separator(tab3,orient="horizontal")
separator.place(x=826,y=230,width=182 )

std_lname_insert=Entry(tab3,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e8)
std_lname_insert.place(height=30,x=825,y=256)
separator = ttk.Separator(tab3,orient="horizontal")
separator.place(x=826,y=285,width=182 )

std_mobile_insert=Entry(tab3,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e9)
std_mobile_insert.place(height=30,x=825,y=310)
separator = ttk.Separator(tab3,orient="horizontal")
separator.place(x=826,y=340,width=182 )

std_Email_Id_insert=Entry(tab3,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e10)
std_Email_Id_insert.place(height=30,x=826,y=364)
separator = ttk.Separator(tab3,orient="horizontal")
separator.place(x=826,y=394,width=182 )

std_branch_insert=Entry(tab3,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e11)
std_branch_insert.place(height=30,x=826,y=418)
separator = ttk.Separator(tab3,orient="horizontal")
separator.place(x=826,y=448,width=182 )

std_Semester_insert=Entry(tab3,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e12)
std_Semester_insert.place(height=30,x=828,y=472)
separator = ttk.Separator(tab3,orient="horizontal")
separator.place(x=829,y=500,width=182 )

note=Label(tab3,text="(Note: To Change Classroom & Roll_No please Delete & Re-enter your details)",bg=_from_rgb((33, 40, 62)),fg=_from_rgb((0,200,244)),font = "Verdana 10 bold")
note.place(x=560,y=572)

about_logo_student=ImageTk.PhotoImage(file="C://Roadster//Major//edit.png")
about_image=Label(tab7,image=about_logo_student)
about_image.place(x=0,y=0)

top.mainloop()










