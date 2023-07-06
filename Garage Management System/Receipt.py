import os
#import pywintypes
import pythoncom # Uncomment this if some other DLL load will fail
import win32gui
from PIL import ImageGrab
from tkinter import simpledialog

#from pyscreenshot import grab
import tkinter
import tkinter as tk
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
# dictionary of colors:
import mysql.connector
from PIL import ImageTk
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def getcarcode(event):
    code=t8.get()
    if code=="":
        messagebox.showwarning("Warning","Please Enter Car Code To Make Receipt!")
    else:
        fetch_car(code)
def fetch_car(code):
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery = "select Car_Code,Car_Name,Registration_Number,Owner_Name,Owner_CNIC_Number from detail"+" WHERE Car_Code="+code
        print(savequery)
        try:
            cursor.execute(savequery)
            rows = cursor.fetchall()
            print("-",rows)
            if rows==[]:
                messagebox.showwarning("Warning", "Please Insert Valid Car Code!")
            else:
                update_car(rows)
        except mysql.connector.Error as e:
            messagebox.showwarning("Warning","Please Insert Valid Car Code!")
            messagebox.showinfo("Error",e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
    db.close()

def update_car(rows):
    y=rows[0]
    x=list(y)
    carcode=x[0]
    carname=x[1]
    carragistrationno=x[2]
    customername=x[3]
    customercode=x[4]
    print(carcode,carname,carragistrationno,customername,customercode)
    s1.set(carcode)
    s2.set(customercode)
    s3.set(carname)
    s4.set(customername)
    s5.set(carragistrationno)
    fetch_cardata(carcode)

def fetch_cardata(carcode):
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery = " select Sr_No,Name,Price from recept"+" WHERE Car_Code="+str(carcode)
        print(savequery)
        try:
            cursor.execute(savequery)
            rows = cursor.fetchall()
            reset_carexit()
            update_carexitdata(rows)
            labourcharges(carcode)
        except mysql.connector.Error as e:
            messagebox.showinfo("Error",e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
    db.close()

def update_carexitdata(rows):
    for i in rows:
        Cartdata.insert('','end',values=i)

def reset_carexit():
    Cartdata.delete(*Cartdata.get_children())

def labourcharges(carcode):
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery = " select Machine_fee from recept"+" WHERE Car_Code="+str(carcode)
        print(savequery)
        try:
            cursor.execute(savequery)
            rows = cursor.fetchall()
            t6.delete(0, 'end')
            if rows==[]:
                messagebox.showwarning("Warning","Receipt not generated for the current Car Code Please Try Again!")
            else:
                labourdata(rows)
                calculate()
        except mysql.connector.Error as e:
            messagebox.showinfo("Error",e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
    db.close()

def labourdata(rows):
    y = rows[0]
    x = list(y)
    charges = x[0]
    s6.set(charges)

def calculate():
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", db="mmt_garages")
        cursor = db.cursor()
        savequery = "select sum(Price),Machine_Fee from recept"
        print(savequery)
        try:
            cursor.execute(savequery)
            rows = cursor.fetchall()
            t7.delete(0, 'end')
            calculatedata(rows)
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()

def calculatedata(rows):
    y = rows[0]
    x = list(y)
    Lcharges = x[0]
    Tcharges = x[1]
    total=int(Lcharges)+int(Tcharges)
    s7.set(str(total))

def reset_allcarexit():
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", db="mmt_garages")
        cursor = db.cursor()
        savequery = "truncate table recept"
        try:
            cursor.execute(savequery)
            db.commit()
            # result = cursor.fetchone()
            # number_of_rows = result[0]
            # rows = cursor.fetchall()
            # numrows = int(cursor.rowcount)
            # numrows = cursor.fetchall()
            messagebox.showinfo("Information", "Receipt Generated Successfully!")
            Cartdata.delete(*Cartdata.get_children())
            top.destroy()
            os.system('dashboard.py')
        except mysql.connector.Error as e:
            messagebox.showerror("Error", "Operation Failed Please Retry!")
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)

def save_img(event):
    #im = grab(bbox=(360, 10, 980, 660))
    #im.show()
    hwnd = win32gui.FindWindow(None, r'Receipt')
    win32gui.SetForegroundWindow(hwnd)
    dimensions = win32gui.GetWindowRect(hwnd)
    image = ImageGrab.grab(dimensions)
    #image.show()
    USER_INP = simpledialog.askstring(title="Test",prompt="Enter Image Name!")
    print(str(USER_INP))
    if str(USER_INP)!="None":
        path="C:/Users/Admin/Desktop/"+str(USER_INP)+".png"
        try:
            image.save(path)
        except:
            messagebox.showerror("Error","Error While Saving The Image! Please Retry!")
        reset_allcarexit()

def reset_allcarexit1(event):
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", db="mmt_garages")
        cursor = db.cursor()
        savequery = "truncate table recept"
        try:
            cursor.execute(savequery)
            db.commit()
            # result = cursor.fetchone()
            # number_of_rows = result[0]
            # rows = cursor.fetchall()
            # numrows = int(cursor.rowcount)
            # numrows = cursor.fetchall()
            messagebox.showinfo("Information", "Redirecting To The Dashboard!")
            Cartdata.delete(*Cartdata.get_children())
            top.destroy()
            os.system('dashboard.py')
        except mysql.connector.Error as e:
            messagebox.showerror("Error", "Operation Failed Please Retry!")
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
top = Tk()
#top.geometry("620x700+-7+0")
top.geometry("620x700+360+10")
top.resizable(0, 0)
top.overrideredirect(True)
top.title("Receipt")

p1 = PhotoImage(file = 'tools.png')
top.iconphoto(False, p1)

s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
s4 = StringVar()
s5 = StringVar()
s6 = StringVar()
s7 = StringVar()
s8 = StringVar()
s9 = StringVar()
s10 = StringVar()

back=Frame(top,bg=_from_rgb((33,40,62)),width=620)
back.place(x=0,y=0,height=650)

header = Frame(back,bg=_from_rgb((33,40,62)),width=620)
header.place(x=0,y=0,height=90)

h1=Label(header,text="MMT Garage Management System",bg=_from_rgb((33,40,62)),font="Tahoma 24 bold",fg=_from_rgb((0,200,244)))
h1.place(x=30,y=20)

l1=Label(back,text="Receipt No",bg=_from_rgb((33,40,62)),font="Tahoma 14 bold",fg=_from_rgb((0,200,244)))
l1.place(x=10,y=100)

t1=Entry(back,bg="white",width=3, highlightthickness=0,bd=1,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 8 bold",textvariable=s1)
t1.place(height=30,x=125,y=100)

l2=Label(back,text="Customer Code",bg=_from_rgb((33,40,62)),font="Tahoma 14 bold",fg=_from_rgb((0,200,244)))
l2.place(x=10,y=160)

t2=Entry(back,bg="white",width=14, highlightthickness=0,bd=1,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 8 bold",textvariable=s2)
t2.place(height=28,x=174,y=160)

l3=Label(back,text="Car Name",bg=_from_rgb((33,40,62)),font="Tahoma 14 bold",fg=_from_rgb((0,200,244)))
l3.place(x=320,y=160)

t3=Entry(back,bg="white",width=12, highlightthickness=0,bd=1,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 8 bold",textvariable=s3)
t3.place(height=28,x=510,y=160)

l4=Label(back,text="Customer Name",bg=_from_rgb((33,40,62)),font="Tahoma 14 bold",fg=_from_rgb((0,200,244)))
l4.place(x=10,y=200)

t4=Entry(back,bg="white",width=14, highlightthickness=0,bd=1,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 8 bold",textvariable=s4)
t4.place(height=30,x=174,y=200)

l5=Label(back,text="Car Registration #",bg=_from_rgb((33,40,62)),font="Tahoma 14 bold",fg=_from_rgb((0,200,244)))
l5.place(x=320,y=200)

t5=Entry(back,bg="white",width=12, highlightthickness=0,bd=1,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 8 bold",textvariable=s5)
t5.place(height=28,x=510,y=200)

style8 = ttk.Style()
style8.theme_use("clam")
style8.layout('TNotebook.Tab', [])
style8.configure("Treeview.Heading", background=_from_rgb((33, 40, 62)),fieldbackground=_from_rgb((33, 40, 62)),foreground=_from_rgb((0,200,244)))

Cartdata = ttk.Treeview(back,columns=(1,2,3),show="headings",height="11")
#Stockdata.bind('<Double 1>',getrow_Stockdb)
Cartdata.place(x=0,y=250,width="620")
Cartdata.heading(1,text="Sr_No")
Cartdata.heading(2,text="Name")
Cartdata.heading(3,text="Price")
Cartdata.column(1, anchor=tkinter.N,minwidth=0, width=205, stretch=NO)
Cartdata.column(2, anchor=tkinter.N,minwidth=0, width=205, stretch=NO)
Cartdata.column(3, anchor=tkinter.N,minwidth=0, width=205, stretch=NO)

separator1 = ttk.Separator(back,orient='vertical',style="tab10.TSeparator")
separator1.place(x=410,y=250,width=3, height=250)

separator2 = ttk.Separator(back,orient='vertical',style="tab10.TSeparator")
separator2.place(x=206,y=250,width=3, height=250)

separator = ttk.Separator(back,orient="horizontal",style="tab8.TSeparator")
separator.place(x=0,y=500,width=620)

l6=Label(back,text="Labour Charges:-",bg=_from_rgb((33,40,62)),font="Tahoma 14 bold",fg=_from_rgb((0,200,244)))
l6.place(x=210,y=520)

t6=Entry(back,bg="white",width=16, highlightthickness=0,bd=1,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 8 bold",textvariable=s6)
t6.place(height=28,x=380,y=520)

l7=Label(back,text="Total:-",bg=_from_rgb((33,40,62)),font="Tahoma 14 bold",fg=_from_rgb((0,200,244)))
l7.place(x=310,y=565)

t7=Entry(back,bg="white",width=16, highlightthickness=0,bd=1,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 8 bold",textvariable=s7)
t7.place(height=28,x=380,y=565)

l8=Label(back,text="Signature:-",bg=_from_rgb((33,40,62)),font="Tahoma 14 bold",fg=_from_rgb((0,200,244)))
l8.place(x=268,y=610)

separator = ttk.Separator(back,orient="horizontal",style="tab8.TSeparator")
separator.place(x=380,y=640,width=220)

l8=Label(back,text="MMT Garages Signature:-",bg=_from_rgb((33,40,62)),font="Tahoma 11 bold",fg=_from_rgb((0,200,244)))
l8.place(x=0,y=615)


l9=Label(back,text="Thank You! Visit Us Again",bg=_from_rgb((33,40,62)),font="Tahoma 11 bold",fg=_from_rgb((0,200,244)))
l9.place(x=50,y=570)

l10=Label(top,text="Enter Car Code: -",font="Tahoma 11 bold",fg=_from_rgb((0,200,244)),bg=_from_rgb((33,40,62)))
l10.place(x=5,y=665)

t8=Entry(top,bg="white",width=3, highlightthickness=0,bd=1,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 8 bold")
t8.place(height=25,x=140,y=665)

l12=Label(top,text="Show Receipt",font="Tahoma 11 bold",fg=_from_rgb((0,200,244)),bg=_from_rgb((33,40,62)),width=12)
l12.bind("<Button>", getcarcode)
l12.place(x=210,y=665)

l11=Label(top,text="Print",font="Tahoma 11 bold",fg=_from_rgb((0,200,244)),bg=_from_rgb((33,40,62)),width=10)
l11.bind("<Button>", save_img)
l11.place(x=365,y=665)

l12=Label(top,text="Exit",font="Tahoma 11 bold",fg=_from_rgb((0,200,244)),bg=_from_rgb((33,40,62)),width=10)
l12.bind("<Button>",reset_allcarexit1)
l12.place(x=500,y=665)

separator = ttk.Separator(back,orient="horizontal",style="tab8.TSeparator")
separator.place(x=200,y=632,width=70)

top.mainloop()













