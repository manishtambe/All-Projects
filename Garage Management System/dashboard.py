import os
from datetime import date
from datetime import datetime
from tkinter import PhotoImage
from tkinter.ttk import Treeview
import tkinter
import tkinter as tk
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
# dictionary of colors:
import mysql.connector
from PIL import ImageTk

color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def custvisible():
    l1.place(x=4, y=165)
    l2.place(x=4, y=210)

def stockvisible():
    l3.place(x=4, y=295)
    l4.place(x=4, y=340)

def employeevisible():
    l5.place(x=4, y=425)
    l6.place(x=4, y=470)

def carvisible():
    l7.place(x=4, y=555)
    l8.place(x=4, y=595)
    l9.place(x=4, y=650)
def off():
    l1.pack_forget()
    l2.pack_forget()
    l3.pack_forget()
    l4.pack_forget()
    l5.pack_forget()
    l6.pack_forget()
    l7.pack_forget()
    l8.pack_forget()
    l9.pack_forget()
# setting root window:
root = tk.Tk()
root.title("Dashboard")
root.geometry("1362x700+-7+0")
root.resizable(0,0)

p1 = PhotoImage(file = 'tools.png')
root.iconphoto(False, p1)

SideBar = Frame(root,bg="white",width=1362)
SideBar.place(x=0,y=0,height=700)


# setting switch state:
btnState = False

# loading Navbar icon image:
navIcon = PhotoImage(file="menu.png")
closeIcon = PhotoImage(file="close.png")
logo = PhotoImage(file="Logo1.png")
customer=PhotoImage(file="customer.png")
# setting switch function:
def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            #topFrame.update()

        # turning button OFF:
        btnState = False
    else:
        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            #topFrame.update()
        # turing button ON:
        btnState = True
def viewtab2(event):
    tabControl.select(1)
def addtab3(event):
    tabControl.select(2)
def viewtab4(event):
    tabControl.select(3)
def addtab5(event):
    tabControl.select(4)
def viewtab6(event):
    tabControl.select(5)
def addtab7(event):
    tabControl.select(6)
def viewtab8(event):
    tabControl.select(7)
def cartab9(event):
    tabControl.select(8)
def cartab10(event):
    tabControl.select(9)
def tababout(event):
    tabControl.select(10)
def tablogout(event):
    #tabControl.select(11)
    messagebox.showwarning("Warning", "Do You Want To Logout From System!")
    root.destroy()
    os.system('Login.py')
def hometab(event):
    tabControl.select(0)
#---------------------------------------------------------------------Add Customer----------------------------------------------------
def clearaddcustomer():
    tab3t2.delete(0, 'end')
    tab3t3.delete(0, 'end')
    tab3t4.delete(0, 'end')
    tab3t5.delete(0, 'end')
    tab3t6.delete(0, 'end')
    tab3t7.delete(0, 'end')
    tab3t8.delete(0, 'end')
    tab3t9.delete(0, 'end')
    tab3t10.delete(0, 'end')
    tab3t11.delete(0, 'end')
def addcustomer():
    t2 = tab3t2.get()
    t3 = tab3t3.get()
    t4 = tab3t4.get()
    t5 = tab3t5.get()
    t6 = tab3t6.get()
    t7 = tab3t7.get()
    t8 = tab3t8.get()
    t9 = tab3t9.get()
    t10 = tab3t10.get()
    t11 = tab3t11.get()
    if t2=="":
        messagebox.showwarning("Warning", "Please Enter Customer Name!")
    else:
            if t3=="":
                messagebox.showwarning("Warning", "Please Enter CNIC Number!")
            else:
                if t4=="":
                    messagebox.showwarning("Warning", "Please Enter Date of Birth!")
                else:
                    if t5=="":
                        messagebox.showwarning("Warning", "Please Enter Gender!")
                    else:
                        if t6=="":
                            messagebox.showwarning("Warning", "Please Enter Mobile No!")
                        else:
                            if t7=="":
                                messagebox.showwarning("Warning", "Please Enter Email Address!")
                            else:
                                if t8=="":
                                    messagebox.showwarning("Warning", "Please Enter Car Name!")
                                else:
                                    if t9=="":
                                        messagebox.showwarning("Warning", "Please Enter Car Model!")
                                    else:
                                        if t10=="":
                                            messagebox.showwarning("Warning", "Please Enter Car Registration Number!")
                                        else:
                                            if t11=="":
                                                messagebox.showwarning("Warning","Please Enter Address Of Customer!")
                                            else:
                                                insertCustomer(t2,t3,t4,t5,t6,t7,t8,t9,t10,t11)
def insertCustomer(t2,t3,t4,t5,t6,t7,t8,t9,t10,t11):
    try:
        database="customer"
        db = mysql.connector.connect(host="localhost", user="root", password="", db="mmt_garages")
        cursor = db.cursor()
        #String query="INSERT INTO customer(Customer_Name,CNIC_Number,Date_of_Birth,Gender,Phone_Number,Email_Address,Car_Name,Car_Model,Car_Registration_Number,Address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)";
        savequery = "insert into " + database + "(Customer_Name,CNIC_Number,Date_of_Birth,Gender,Phone_Number,Email_Address,Car_Name,Car_Model,Car_Registration_Number,Address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(savequery, (t2,t3,t4,t5,t6,t7,t8,t9,t10,t11))
            db.commit()
            numrows = int(cursor.rowcount)
            if numrows == 1:
                messagebox.showinfo("Information","Entry Added Successfully !")
                clearaddcustomer()
                resetal_customer()
            else:
                messagebox.showerror("Error","Error Occur While inserting data")
                clearaddcustomer()
        except mysql.connector.Error as e:
            messagebox.showinfo("Error",e)
            clearaddcustomer()
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
        clearaddcustomer()
    db.close()


#-------------------------------------------------------------------------Add Stock-----------------------------------------------------------------------------------
def clearaddstock():
    tab5t2.delete(0, 'end')
    tab5t3.set('Door and Windows')
    tab5t4.delete(0,"end")
    tab5t4.insert(0,0)
    tab5t5.delete(0, 'end')
    tab5t6.delete(0, 'end')
    tab5t7.delete(0, 'end')
    tab5t10.delete(0, 'end')

def addstock():
    t2 = tab5t2.get()
    t3 = tab5t3.get()
    t4 = tab5t4.get()
    t5 = tab5t5.get()
    t6 = tab5t6.get()
    t7 = tab5t7.get()
    now = datetime.now()
    t8 = now.strftime("%H:%M:%S")
    t9 = date.today()
    t10 = tab5t10.get()
    if t2=="":
        messagebox.showwarning("Warning", "Please Enter Item Name!")
    else:
            if t4=="0":
                messagebox.showwarning("Warning", "Please Select Quantity!")
            else:
                if t5=="":
                    messagebox.showwarning("Warning", "Please Enter Buying Price!")
                else:
                    if t6=="":
                        messagebox.showwarning("Warning", "Please Enter Selling Price!")
                    else:
                        if t7=="":
                            messagebox.showwarning("Warning", "Please Enter Car Name!")
                        else:
                            insertStock(t2,t3,t4,t5,t6,t7,t8,t9,t10)

def insertStock(t2,t3,t4,t5,t6,t7,t8,t9,t10):
    try:
        database="stock"
        db = mysql.connector.connect(host="localhost", user="root", password="", db="mmt_garages")
        cursor = db.cursor()
        #String query="INSERT INTO stock(Item_Name,Category,Quantity,Buying_Price,Selling_Price,Car_Name,Time_Of_Entry,Date_Of_Entry,Warranty) VALUES (?,?,?,?,?,?,?,?,?)";
        savequery = "insert into " + database + "(Item_Name,Category,Quantity,Buying_Price,Selling_Price,Car_Name,Time_Of_Entry,Date_Of_Entry,Warranty) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(savequery, (t2,t3,t4,t5,t6,t7,t8,t9,t10))
            db.commit()
            numrows = int(cursor.rowcount)
            if numrows == 1:
                messagebox.showinfo("Information","Entry Added Successfully !")
                clearaddstock()
                reset_Stock()
                reset_car_exit()
            else:
                messagebox.showerror("Error","Error Occur While inserting data")
                clearaddstock()
        except mysql.connector.Error as e:
            messagebox.showinfo("Error",e)
            clearaddstock()
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
        clearaddstock()
    db.close()
#--------------------------------------------------------------------#tab7 Add Employee-------------------------------------------------------------------------------------------------
def clearaddemployee():
    tab7t2.delete(0, 'end')
    tab7t3.delete(0, 'end')
    tab7t4.delete(0, 'end')
    tab7t5.delete(0, 'end')
    tab7t6.delete(0, 'end')
    tab7t7.delete(0, 'end')
    tab7t8.delete(0, 'end')
    tab7t9.delete(0, 'end')
    tab7t10.delete(0, 'end')
    tab7t11.delete(0, 'end')
def addemployee():
    t2 = tab7t2.get()
    t3 = tab7t3.get()
    t4 = tab7t4.get()
    t5 = tab7t5.get()
    t6 = tab7t6.get()
    t7 = tab7t7.get()
    t8 = tab7t8.get()
    t9 = tab7t9.get()
    t10 = tab7t10.get()
    t11 = tab7t11.get()
    if t2=="":
        messagebox.showwarning("Warning", "Please Enter Employee Name!")
    else:
            if t3=="":
                messagebox.showwarning("Warning", "Please Enter Employee CNIC Number!")
            else:
                if t4=="":
                    messagebox.showwarning("Warning", "Please Enter Designation Of Employee!")
                else:
                    if t5=="":
                        messagebox.showwarning("Warning", "Please Enter Date Of Birth Of Employee!")
                    else:
                        if t6=="":
                            messagebox.showwarning("Warning", "Please Enter Gender Of Employee!")
                        else:
                            if t7=="":
                                messagebox.showwarning("Warning", "Please Enter Phone Number Of Employee!")
                            else:
                                if t8=="":
                                    messagebox.showwarning("Warning", "Please Enter Email Address Of Employee!")
                                else:
                                    if t9=="":
                                        messagebox.showwarning("Warning", "Please Enter Date Of Joining Of Employee!")
                                    else:
                                        if t10=="":
                                            messagebox.showwarning("Warning", "Please Enter Address Of Employee!")
                                        else:
                                            insertEmployee(t2,t3,t4,t5,t6,t7,t8,t9,t10,t11)
def insertEmployee(t2,t3,t4,t5,t6,t7,t8,t9,t10,t11):
    try:
        database = "employee"
        db = mysql.connector.connect(host="localhost", user="root", password="", db="mmt_garages")
        cursor = db.cursor()
        #String query = "INSERT INTO employee(Employee_Name,CNIC_Number,Designation,Date_of_Birth,Gender,Phone_Number,Email_Address,Date_of_Joining,Address,Extra_Detail) VALUES (?,?,?,?,?,?,?,?,?,?)";
        savequery = "insert into " + database + "(Employee_Name,CNIC_Number,Designation,Date_of_Birth,Gender,Phone_Number,Email_Address,Date_of_Joining,Address,Extra_Detail) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(savequery, (t2, t3, t4, t5, t6, t7, t8, t9, t10, t11))
            db.commit()
            numrows = int(cursor.rowcount)
            if numrows == 1:
                messagebox.showinfo("Information", "Entry Added Successfully !")
                clearaddemployee()
                reset_Employee()
            else:
                messagebox.showerror("Error", "Error Occur While inserting data")
                clearaddemployee()
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
            clearaddemployee()
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
        clearaddemployee()
    db.close()
#--------------------------------------------------------------------tab9 Car Entrance In Garage (Add Car)-------------------------------------------------------------------------------------------------
def clearcar():
    tab9t2.delete(0, 'end')
    tab9t3.delete(0, 'end')
    tab9t4.delete(0, 'end')
    tab9t7.delete(0, 'end')
    tab9t8.delete(0, 'end')
    tab9t9.delete(0, 'end')
    tab9t10.delete(0, 'end')
def addcar():
    t2 = tab9t2.get()
    t3 = tab9t3.get()
    t4 = tab9t4.get()
    t5 = date.today()
    now = datetime.now()
    t6 = now.strftime("%H:%M:%S")
    #t5 = tab9t5.get()
    #t6 = tab9t6.get()
    t7 = tab9t7.get()
    t8 = tab9t8.get()
    t9 = tab9t9.get()
    t10 = tab9t10.get()
    t11 =""
    t12 =""
    if t2=="":
        messagebox.showwarning("Warning", "Please Enter Car Name!")
    else:
            if t3=="":
                messagebox.showwarning("Warning", "Please Enter Car Model!")
            else:
                if t4=="":
                    messagebox.showwarning("Warning", "Please Enter Registration Number!")
                else:
                    if t7=="":
                        messagebox.showwarning("Warning", "Please Enter Owner Name!")
                    else:
                        if t8=="":
                            messagebox.showwarning("Warning", "Please Enter Owner CNIC Name!")
                        else:
                            if t9=="":
                                messagebox.showwarning("Warning","Please Enter Car Color")
                            else:
                                insertCar(t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12)

def insertCar(t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12):
    try:
        database="detail"
        db = mysql.connector.connect(host="localhost", user="root", password="", db="mmt_garages")
        cursor = db.cursor()
        #String query="INSERT INTO detail(Car_Name, Car_Model,Registration_Number,Date_of_Entry,Time_of_Entry,Owner_Name,Owner_CNIC_Number, Car_Color, Extra_Details,Exiting_Time,Exiting_Date) VALUES (?,?,?,?,?,?,?,?,?,?,?)";
        savequery = "insert into " + database + " (Car_Name, Car_Model,Registration_Number,Date_of_Entry,Time_of_Entry,Owner_Name,Owner_CNIC_Number, Car_Color, Extra_Details,Exiting_Time,Exiting_Date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(savequery,(t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12))
            db.commit()
            numrows = int(cursor.rowcount)
            if numrows == 1:
                messagebox.showinfo("Information","Entry Added Successfully !")
                clearcar()
                reset_car()
            else:
                messagebox.showerror("Error","Error Occur While inserting data")
                clearcar()
        except mysql.connector.Error as e:
            messagebox.showinfo("Error",e)
            clearcar()
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
        clearcar()
    db.close()
#---------------------------------------------------------tab2 View Customer------------------------------------------------------------------------------------------
def getrow_Customerdb(event):
    rowid = Customerdata.identify_row(event.y)
    item = Customerdata.item(Customerdata.focus())
    c1.set(item['values'][0])
    c2.set(item['values'][1])
    c3.set(item['values'][2])
    c4.set(item['values'][3])
    c5.set(item['values'][4])
    c6.set(item['values'][5])
    c7.set(item['values'][6])
    c8.set(item['values'][7])
    c9.set(item['values'][8])
    c10.set(item['values'][9])
    c11.set(item['values'][10])

def fetch_customer():
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery = "SELECT * FROM customer"
        print(savequery)
        try:
            cursor.execute(savequery)
            rows = cursor.fetchall()
            update_customer(rows)
        except mysql.connector.Error as e:
            messagebox.showinfo("Error",e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
    db.close()

def update_customer(rows):
    for i in rows:
        Customerdata.insert('','end',values=i)

def resetal_customer():
    Customerdata.delete(*Customerdata.get_children())
    fetch_customer()

def clear_customer():
    tab2t1.delete(0, 'end')
    tab2t2.delete(0, 'end')
    tab2t3.delete(0, 'end')
    tab2t4.delete(0, 'end')
    tab2t5.delete(0, 'end')
    tab2t6.delete(0, 'end')
    tab2t7.delete(0, 'end')
    tab2t8.delete(0, 'end')
    tab2t9.delete(0, 'end')
    tab2t10.delete(0, 'end')
    tab2t11.delete(0, 'end')
def remove_customer(event):
        t1 = tab2t1.get()
        t2 = tab2t2.get()
        t3 = tab2t3.get()
        t4 = tab2t4.get()
        t5 = tab2t5.get()
        t6 = tab2t6.get()
        t7 = tab2t7.get()
        t8 = tab2t8.get()
        t9 = tab2t9.get()
        t10 = tab2t10.get()
        t11 = tab2t11.get()
        if t1 == "":
            messagebox.showwarning("Warning", "Please Enter Customer Code!")
        else:
            if t2 == "":
                messagebox.showwarning("Warning", "Please Enter Customer Name!")
            else:
                if t3 == "":
                    messagebox.showwarning("Warning", "Please Enter CNIC Number!")
                else:
                    if t4 == "":
                        messagebox.showwarning("Warning", "Please Enter Date of Birth!")
                    else:
                        if t5 == "":
                            messagebox.showwarning("Warning", "Please Enter Gender!")
                        else:
                            if t6 == "":
                                messagebox.showwarning("Warning", "Please Enter Mobile No!")
                            else:
                                if t7 == "":
                                    messagebox.showwarning("Warning", "Please Enter Email Address!")
                                else:
                                    if t8 == "":
                                        messagebox.showwarning("Warning", "Please Enter Car Name!")
                                    else:
                                        if t9 == "":
                                            messagebox.showwarning("Warning", "Please Enter Car Model!")
                                        else:
                                            if t10 == "":
                                                messagebox.showwarning("Warning", "Please Enter Car Registration Number!")
                                            else:
                                                if t11 == "":
                                                    messagebox.showwarning("Warning", "Please Enter Address Of Customer!")
                                                else:
                                                    removeCustomer(t1,t2, t3, t4, t5, t6, t7, t8, t9, t10, t11)

def removeCustomer(t1,t2, t3, t4, t5, t6, t7, t8, t9, t10, t11):
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery="DELETE FROM customer WHERE Customer_Code= "+str(t1)+" AND Customer_Name='"+t2+"'"+" AND CNIC_Number='"+t3+"'"+" AND Date_of_Birth='"+t4+"'"+" AND Gender='"+t5+"'"+" AND Phone_Number='"+t6+"'"+" AND Email_Address='"+t7+"'"+" AND Car_Name='"+t8+"'"+" AND Car_Model='"+t9+"'"+" AND Car_Registration_Number='"+t10+"'"+" AND Address='"+t11+"'"
        try:
            cursor.execute(savequery)
            db.commit()
            # result = cursor.fetchone()
            # number_of_rows = result[0]
            #rows = cursor.fetchall()
            numrows = int(cursor.rowcount)
            #numrows = cursor.fetchall()
            print(numrows)
            if numrows == 1:
                messagebox.showinfo("Information","Entry Deleted Successful!")
                clear_customer()
                resetal_customer()

            else:
                messagebox.showerror("Error", "Invalid Customer Data Please Retry!")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()
    clear_customer()
    resetal_customer()

def update_customerdata(event):
        t1 = tab2t1.get()
        t2 = tab2t2.get()
        t3 = tab2t3.get()
        t4 = tab2t4.get()
        t5 = tab2t5.get()
        t6 = tab2t6.get()
        t7 = tab2t7.get()
        t8 = tab2t8.get()
        t9 = tab2t9.get()
        t10 = tab2t10.get()
        t11 = tab2t11.get()
        if t1 == "":
            messagebox.showwarning("Warning", "Please Enter Customer Code!")
        else:
            if t2 == "":
                messagebox.showwarning("Warning", "Please Enter Customer Name!")
            else:
                if t3 == "":
                    messagebox.showwarning("Warning", "Please Enter CNIC Number!")
                else:
                    if t4 == "":
                        messagebox.showwarning("Warning", "Please Enter Date of Birth!")
                    else:
                        if t5 == "":
                            messagebox.showwarning("Warning", "Please Enter Gender!")
                        else:
                            if t6 == "":
                                messagebox.showwarning("Warning", "Please Enter Mobile No!")
                            else:
                                if t7 == "":
                                    messagebox.showwarning("Warning", "Please Enter Email Address!")
                                else:
                                    if t8 == "":
                                        messagebox.showwarning("Warning", "Please Enter Car Name!")
                                    else:
                                        if t9 == "":
                                            messagebox.showwarning("Warning", "Please Enter Car Model!")
                                        else:
                                            if t10 == "":
                                                messagebox.showwarning("Warning",
                                                                       "Please Enter Car Registration Number!")
                                            else:
                                                if t11 == "":
                                                    messagebox.showwarning("Warning",
                                                                           "Please Enter Address Of Customer!")
                                                else:
                                                    updateCustomerdata(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11)
def updateCustomerdata(t1,t2, t3, t4, t5, t6, t7, t8, t9, t10, t11):
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery="UPDATE customer SET Customer_Name='"+t2+"'"+",CNIC_Number='"+t3+"'"+",Date_of_Birth='"+t4+"'"+",Gender='"+t5+"'"+",Phone_Number='"+t6+"'"+",Email_Address='"+t7+"'"+",Car_Name='"+t8+"'"+",Car_Model='"+t9+"'"+",Car_Registration_Number='"+t10+"'"+",Address='"+t11+"'"+" WHERE Customer_Code= "+str(t1)
        try:
            cursor.execute(savequery)
            db.commit()
            # result = cursor.fetchone()
            # number_of_rows = result[0]
            #rows = cursor.fetchall()
            numrows = int(cursor.rowcount)
            #numrows = cursor.fetchall()
            print(numrows)
            if numrows == 1:
                messagebox.showinfo("Information","Details Updated Successfully!")
                clear_customer()
                resetal_customer()

            else:
                messagebox.showerror("Error", "Invalid Details Or Same Data Has Been Entered Please Retry!")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()
    clear_customer()
    resetal_customer()
#--------------------------------------------------------------tab 4 View Stock-------------------------------------------------------------------------------------------------------
def getrow_Stockdb(event):
    rowid = Stockdata.identify_row(event.y)
    item = Stockdata.item(Stockdata.focus())
    s1.set(item['values'][0])
    s2.set(item['values'][1])
    s3.set(item['values'][2])
    s4.set(item['values'][3])
    s5.set(item['values'][4])
    s6.set(item['values'][5])
    s7.set(item['values'][6])
    s8.set(item['values'][7])
    s9.set(item['values'][8])
    s10.set(item['values'][9])
def fetch_stock():
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery = "SELECT * FROM stock"
        print(savequery)
        try:
            cursor.execute(savequery)
            rows = cursor.fetchall()
            update_stock(rows)
        except mysql.connector.Error as e:
            messagebox.showinfo("Error",e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
    db.close()

def update_stock(rows):
    for i in rows:
        Stockdata.insert('','end',values=i)

def reset_Stock():
    Stockdata.delete(*Stockdata.get_children())
    fetch_stock()

def remoeve_stock(event):
    t1 = tab4t1.get()
    t2 = tab4t2.get()
    t3 = tab4t3.get()
    t4 = tab4t4.get()
    t5 = tab4t5.get()
    t6 = tab4t6.get()
    t7 = tab4t7.get()
    t8 = tab4t8.get()
    t9 = tab4t9.get()
    t10 = tab4t10.get()
    if t1=="":
        messagebox.showwarning("Warning", "Please Enter Item Code!")
    else:
        if t2=="":
            messagebox.showwarning("Warning", "Please Enter Item Name!")
        else:
            if t3=="":
                messagebox.showwarning("Warning", "Please Enter Category Of Item!")
            else:
                if t4=="":
                    messagebox.showwarning("Warning", "Please Select Quantity!")
                else:
                    if t5=="":
                        messagebox.showwarning("Warning", "Please Enter Buying Price!")
                    else:
                        if t6=="":
                            messagebox.showwarning("Warning", "Please Enter Selling Price!")
                        else:
                            if t7=="":
                                messagebox.showwarning("Warning", "Please Enter Car Name!")
                            else:
                                if t8=="":
                                    messagebox.showwarning("Warning", "Please Enter Time Of Entry!")
                                else:
                                    if t9=="":
                                        messagebox.showwarning("Warning", "Please Date Of Entry!")
                                    else:
                                        removeStock(t1,t2,t3,t4,t5,t6,t7,t8,t9)

def removeStock(t1,t2, t3, t4, t5, t6, t7, t8, t9):
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery="DELETE FROM stock WHERE Item_Code= "+str(t1)+" AND Item_Name='"+t2+"'"+" AND Category='"+t3+"'"+" AND Quantity='"+t4+"'"+" AND Buying_Price='"+t5+"'"+" AND Selling_Price='"+t6+"'"+" AND Car_Name='"+t7+"'"+" AND Time_Of_Entry='"+t8+"'"+" AND Date_Of_Entry='"+t9+"'"
        try:
            cursor.execute(savequery)
            db.commit()
            # result = cursor.fetchone()
            # number_of_rows = result[0]
            #rows = cursor.fetchall()
            numrows = int(cursor.rowcount)
            #numrows = cursor.fetchall()
            print(numrows)
            if numrows == 1:
                messagebox.showinfo("Information","Entry Deleted Successful!")
                clear_stock()
                reset_Stock()
                reset_car_exit()
            else:
                messagebox.showerror("Error", "Invalid Item Data Please Retry!")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()
    clear_stock()
    reset_Stock()
def clear_stock():
    tab4t1.delete(0, 'end')
    tab4t2.delete(0, 'end')
    tab4t3.delete(0, 'end')
    tab4t4.delete(0, 'end')
    tab4t5.delete(0, 'end')
    tab4t6.delete(0, 'end')
    tab4t7.delete(0, 'end')
    tab4t8.delete(0, 'end')
    tab4t9.delete(0, 'end')
    tab4t10.delete(0, 'end')

def update_stockdata(event):
    t1 = tab4t1.get()
    t2 = tab4t2.get()
    t3 = tab4t3.get()
    t4 = tab4t4.get()
    t5 = tab4t5.get()
    t6 = tab4t6.get()
    t7 = tab4t7.get()
    t8 = tab4t8.get()
    t9 = tab4t9.get()
    t10 = tab4t10.get()
    if t1=="":
        messagebox.showwarning("Warning", "Please Enter Item Code!")
    else:
        if t2=="":
            messagebox.showwarning("Warning", "Please Enter Item Name!")
        else:
            if t3=="":
                messagebox.showwarning("Warning", "Please Enter Category Of Item!")
            else:
                if t4=="":
                    messagebox.showwarning("Warning", "Please Select Quantity!")
                else:
                    if t5=="":
                        messagebox.showwarning("Warning", "Please Enter Buying Price!")
                    else:
                        if t6=="":
                            messagebox.showwarning("Warning", "Please Enter Selling Price!")
                        else:
                            if t7=="":
                                messagebox.showwarning("Warning", "Please Enter Car Name!")
                            else:
                                if t8=="":
                                    messagebox.showwarning("Warning", "Please Enter Time Of Entry!")
                                else:
                                    if t9=="":
                                        messagebox.showwarning("Warning", "Please Date Of Entry!")
                                    else:
                                        updateStockdata(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10)
def updateStockdata(t1,t2, t3, t4, t5, t6, t7, t8, t9,t10):
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery="UPDATE stock SET Item_Name='"+t2+"'"+",Category='"+t3+"'"+",Quantity='"+t4+"'"+",Buying_Price='"+t5+"'"+",Selling_Price='"+t6+"'"+",Car_Name='"+t7+"'"+",Time_Of_Entry='"+t8+"'"+",Date_Of_Entry='"+t9+"'"+",Warranty='"+t10+"'"+" WHERE Item_Code= "+str(t1)
        try:
            cursor.execute(savequery)
            db.commit()
            # result = cursor.fetchone()
            # number_of_rows = result[0]
            #rows = cursor.fetchall()
            numrows = int(cursor.rowcount)
            #numrows = cursor.fetchall()
            print(numrows)
            if numrows == 1:
                messagebox.showinfo("Information","Details Updated Successfully!")
                clear_stock()
                reset_Stock()
                reset_car_exit()
            else:
                messagebox.showerror("Error", "Invalid Details Or Same Data Has Been Entered Please Retry!")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()
    clear_stock()
    reset_Stock()
#-----------------------------------------------------------tab6 View Employee----------------------------------------------------------------------------------------------------------
def getrow_Employeedb(event):
    rowid = Employeedata.identify_row(event.y)
    item = Employeedata.item(Employeedata.focus())
    e1.set(item['values'][0])
    e2.set(item['values'][1])
    e3.set(item['values'][2])
    e4.set(item['values'][3])
    e5.set(item['values'][4])
    e6.set(item['values'][5])
    e7.set(item['values'][6])
    e8.set(item['values'][7])
    e9.set(item['values'][8])
    e10.set(item['values'][9])
def fetch_employee():
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery = "SELECT * FROM employee"
        print(savequery)
        try:
            cursor.execute(savequery)
            rows = cursor.fetchall()
            update_employee(rows)
        except mysql.connector.Error as e:
            messagebox.showinfo("Error",e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
    db.close()

def update_employee(rows):
    for i in rows:
        Employeedata.insert('','end',values=i)

def reset_Employee():
    Employeedata.delete(*Employeedata.get_children())
    fetch_employee()
def removeemployee(event):
    t1 = tab6t1.get()
    t2 = tab6t2.get()
    t3 = tab6t3.get()
    t4 = tab6t4.get()
    t5 = tab6t5.get()
    t6 = tab6t6.get()
    t7 = tab6t7.get()
    t8 = tab6t8.get()
    t9 = tab6t9.get()
    t10 = tab6t10.get()
    t11 = tab6t11.get()
    if t1=="":
        messagebox.showwarning("warning"," Please Enter Employee_Code")
    else:
        if t2=="":
            messagebox.showwarning("Warning", "Please Enter Employee Name!")
        else:
                if t3=="":
                    messagebox.showwarning("Warning", "Please Enter Employee CNIC Number!")
                else:
                    if t4=="":
                        messagebox.showwarning("Warning", "Please Enter Designation Of Employee!")
                    else:
                        if t5=="":
                            messagebox.showwarning("Warning", "Please Enter Date Of Birth Of Employee!")
                        else:
                            if t6=="":
                                messagebox.showwarning("Warning", "Please Enter Gender Of Employee!")
                            else:
                                if t7=="":
                                    messagebox.showwarning("Warning", "Please Enter Phone Number Of Employee!")
                                else:
                                    if t8=="":
                                        messagebox.showwarning("Warning", "Please Enter Email Address Of Employee!")
                                    else:
                                        if t9=="":
                                            messagebox.showwarning("Warning", "Please Enter Date Of Joining Of Employee!")
                                        else:
                                            if t10=="":
                                                messagebox.showwarning("Warning", "Please Enter Address Of Employee!")
                                            else:
                                                remove_Emloyee(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11)
def remove_Emloyee(t1,t2, t3, t4, t5, t6, t7, t8, t9, t10, t11):
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery="DELETE FROM employee WHERE Employee_Code= "+str(t1)+" AND Employee_Name='"+t2+"'"+" AND CNIC_Number='"+t3+"'"+" AND Designation='"+t4+"'"+" AND Date_of_Birth='"+t5+"'"+" AND Gender='"+t6+"'"+" AND Phone_Number='"+t7+"'"+" AND Email_Address='"+t8+"'"+" AND Date_of_Joining='"+t9+"'"+" AND Address='"+t10+"'"+" AND Extra_Detail='"+t11+"'"
        try:
            cursor.execute(savequery)
            db.commit()
            # result = cursor.fetchone()
            # number_of_rows = result[0]
            #rows = cursor.fetchall()
            numrows = int(cursor.rowcount)
            #numrows = cursor.fetchall()
            print(numrows)
            if numrows == 1:
                messagebox.showinfo("Information","Entry Deleted Successful!")
                clear_stock()
                reset_Employee()

            else:
                messagebox.showerror("Error", "Invalid Customer Data Please Retry!")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()
    clear_stock()
    reset_Employee()

def clear_stock():
    tab6t1.delete(0, 'end')
    tab6t2.delete(0, 'end')
    tab6t3.delete(0, 'end')
    tab6t4.delete(0, 'end')
    tab6t5.delete(0, 'end')
    tab6t6.delete(0, 'end')
    tab6t7.delete(0, 'end')
    tab6t8.delete(0, 'end')
    tab6t9.delete(0, 'end')
    tab6t10.delete(0, 'end')
    tab6t11.delete(0, 'end')

def update_employeedata(event):
    t1 = tab6t1.get()
    t2 = tab6t2.get()
    t3 = tab6t3.get()
    t4 = tab6t4.get()
    t5 = tab6t5.get()
    t6 = tab6t6.get()
    t7 = tab6t7.get()
    t8 = tab6t8.get()
    t9 = tab6t9.get()
    t10 = tab6t10.get()
    t11 = tab6t11.get()
    if t1=="":
        messagebox.showwarning("warning"," Please Enter Employee_Code")
    else:
        if t2=="":
            messagebox.showwarning("Warning", "Please Enter Employee Name!")
        else:
                if t3=="":
                    messagebox.showwarning("Warning", "Please Enter Employee CNIC Number!")
                else:
                    if t4=="":
                        messagebox.showwarning("Warning", "Please Enter Designation Of Employee!")
                    else:
                        if t5=="":
                            messagebox.showwarning("Warning", "Please Enter Date Of Birth Of Employee!")
                        else:
                            if t6=="":
                                messagebox.showwarning("Warning", "Please Enter Gender Of Employee!")
                            else:
                                if t7=="":
                                    messagebox.showwarning("Warning", "Please Enter Phone Number Of Employee!")
                                else:
                                    if t8=="":
                                        messagebox.showwarning("Warning", "Please Enter Email Address Of Employee!")
                                    else:
                                        if t9=="":
                                            messagebox.showwarning("Warning", "Please Enter Date Of Joining Of Employee!")
                                        else:
                                            if t10=="":
                                                messagebox.showwarning("Warning", "Please Enter Address Of Employee!")
                                            else:
                                               updateemployeedata(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11)

def updateemployeedata(t1,t2, t3, t4, t5, t6, t7, t8, t9, t10, t11):
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery="UPDATE employee SET Employee_Name='"+t2+"'"+",CNIC_Number='"+t3+"'"+",Designation='"+t4+"'"+",Date_of_Birth='"+t5+"'"+",Gender='"+t6+"'"+",Phone_Number='"+t7+"'"+",Email_Address='"+t8+"'"+",Date_of_Joining='"+t9+"'"+",Address='"+t10+"'"+",Extra_Detail='"+t11+"'"+" WHERE Employee_Code= "+str(t1)
        try:
            cursor.execute(savequery)
            db.commit()
            # result = cursor.fetchone()
            # number_of_rows = result[0]
            #rows = cursor.fetchall()
            numrows = int(cursor.rowcount)
            #numrows = cursor.fetchall()
            print(numrows)
            if numrows == 1:
                messagebox.showinfo("Information","Entry Deleted Successful!")
                clear_stock()
                reset_Employee()

            else:
                messagebox.showerror("Error", "Invalid Customer Data Please Retry!")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()
    clear_stock()
    reset_Employee()
#-----------------------------------------------------------tab8 View Car--------------------------------------------------------------------------------------------------------------
def getrow_Cardb(event):
    rowid = Cardata.identify_row(event.y)
    item = Cardata.item(Cardata.focus())
    v1.set(item['values'][0])
    v2.set(item['values'][1])
    v3.set(item['values'][2])
    v4.set(item['values'][3])
    v5.set(item['values'][6])
    v6.set(item['values'][7])
    v7.set(item['values'][8])
    v8.set(item['values'][9])
    v9.set(item['values'][5])
    v10.set(item['values'][10])
    v11.set(item['values'][4])
    v12.set(item['values'][11])

def fetch_car():
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery = "SELECT * FROM detail"
        print(savequery)
        try:
            cursor.execute(savequery)
            rows = cursor.fetchall()
            update_car(rows)
        except mysql.connector.Error as e:
            messagebox.showinfo("Error",e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
    db.close()

def update_car(rows):
    for i in rows:
        Cardata.insert('','end',values=i)

def reset_car():
    Cardata.delete(*Cardata.get_children())
    fetch_car()

def removecar(event):
    t1 = tab8t1.get()
    t2 = tab8t2.get()
    t3 = tab8t3.get()
    t4 = tab8t4.get()
    t5 = tab8t5.get()
    t6 = tab8t6.get()
    t7 = tab8t7.get()
    t8 = tab8t8.get()
    t9 = tab8t9.get()
    t10 = tab8t10.get()
    t11 = tab8t11.get()
    t12 = tab8t12.get()
    if t1=="":
        messagebox.showwarning("Warning", "Please Enter Car Number")
    else:
        if t2=="":
            messagebox.showwarning("Warning", "Please Enter Car Name!")
        else:
                if t3=="":
                    messagebox.showwarning("Warning", "Please Enter Car Model!")
                else:
                    if t4=="":
                        messagebox.showwarning("Warning", "Please Enter Registration Number!")
                    else:
                        if t5=="":
                            messagebox.showwarning("Warning", "Please Enter Owner Name!")
                        else:
                            if t6=="":
                                messagebox.showwarning("Warning", "Please Enter Owner CNIC Name!")
                            else:
                                if t7=="":
                                    messagebox.showwarning("Warning","Please Enter Car Color")
                                else:
                                    if t9=="":
                                        messagebox.showwarning("Warning","Please Enter Car Entry Time")
                                    else:
                                        if t10=="":
                                            messagebox.showwarning("Warning","Please Enter Car Exit Time")
                                        else:
                                            if t11=="":
                                                messagebox.showwarning("Warning","Please Enter Car Entry Date")
                                            else:
                                                if t12=="":
                                                    messagebox.showwarning("Warning","Please Enter Car Exit Date")
                                                else:
                                                    remove_Car(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12)
def remove_Car(t1,t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12):
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery="DELETE FROM detail WHERE Car_Code= "+str(t1)+" AND Car_Name='"+t2+"'"+" AND Car_Model='"+t3+"'"+" AND Registration_Number='"+t4+"'"+" AND Owner_Name='"+t5+"'"+" AND Owner_CNIC_Number='"+t6+"'"+" AND Car_Color='"+t7+"'"+" AND Time_of_Entry='"+t9+"'"+" AND Exiting_Time='"+t10+"'"+" AND Date_of_Entry='"+t11+"'"+" AND Exiting_Date='"+t12+"'"
        try:
            cursor.execute(savequery)
            db.commit()
            # result = cursor.fetchone()
            # number_of_rows = result[0]
            #rows = cursor.fetchall()
            numrows = int(cursor.rowcount)
            #numrows = cursor.fetchall()
            print(numrows)
            if numrows == 1:
                messagebox.showinfo("Information","Entry Deleted Successful!")
                clear_car()
                reset_car()
                fetch_car_exit()
            else:
                messagebox.showerror("Error", "Invalid Customer Data Please Retry!")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()
    clear_car()
    reset_car()

def clear_car():
    tab8t1.delete(0, 'end')
    tab8t2.delete(0, 'end')
    tab8t3.delete(0, 'end')
    tab8t4.delete(0, 'end')
    tab8t5.delete(0, 'end')
    tab8t6.delete(0, 'end')
    tab8t7.delete(0, 'end')
    tab8t8.delete(0, 'end')
    tab8t9.delete(0, 'end')
    tab8t10.delete(0, 'end')
    tab8t11.delete(0, 'end')
    tab8t12.delete(0, 'end')

def update_cardata(event):
    t1 = tab8t1.get()
    t2 = tab8t2.get()
    t3 = tab8t3.get()
    t4 = tab8t4.get()
    t5 = tab8t5.get()
    t6 = tab8t6.get()
    t7 = tab8t7.get()
    t8 = tab8t8.get()
    t9 = tab8t9.get()
    t10 = tab8t10.get()
    t11 = tab8t11.get()
    t12 = tab8t12.get()
    if t1=="":
        messagebox.showwarning("Warning", "Please Enter Car Number")
    else:
        if t2=="":
            messagebox.showwarning("Warning", "Please Enter Car Name!")
        else:
                if t3=="":
                    messagebox.showwarning("Warning", "Please Enter Car Model!")
                else:
                    if t4=="":
                        messagebox.showwarning("Warning", "Please Enter Registration Number!")
                    else:
                        if t5=="":
                            messagebox.showwarning("Warning", "Please Enter Owner Name!")
                        else:
                            if t6=="":
                                messagebox.showwarning("Warning", "Please Enter Owner CNIC Name!")
                            else:
                                if t7=="":
                                    messagebox.showwarning("Warning","Please Enter Car Color")
                                else:
                                    if t9=="":
                                        messagebox.showwarning("Warning","Please Enter Car Entry Time")
                                    else:
                                        if t10=="":
                                            messagebox.showwarning("Warning","Please Enter Car Exit Time")
                                        else:
                                            if t11=="":
                                                messagebox.showwarning("Warning","Please Enter Car Entry Date")
                                            else:
                                                if t12=="":
                                                    messagebox.showwarning("Warning","Please Enter Car Exit Date")
                                                else:
                                                    updateCardata(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12)
def  updateCardata(t1,t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12):
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery="UPDATE detail SET Car_Name='"+t2+"'"+",Car_Model='"+t3+"'"+",Registration_Number='"+t4+"'"+",Owner_Name='"+t5+"'"+",Owner_CNIC_Number='"+t6+"'"+",Car_Color='"+t7+"'"+",Extra_Details='"+t8+"'"+",Time_of_Entry='"+t9+"'"+",Exiting_Time='"+t10+"'"+",Date_of_Entry='"+t11+"'"+",Exiting_Date='"+t12+"'"+" WHERE Car_Code= "+str(t1)
        try:
            cursor.execute(savequery)
            db.commit()
            # result = cursor.fetchone()
            # number_of_rows = result[0]
            #rows = cursor.fetchall()
            numrows = int(cursor.rowcount)
            #numrows = cursor.fetchall()
            print(numrows)
            if numrows == 1:
                messagebox.showinfo("Information","Entry Deleted Successful!")
                clear_car()
                reset_car()

            else:
                messagebox.showerror("Error", "Invalid Customer Data Please Retry!")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()
    clear_car()
    reset_car()
#---------------------------------------------------------------------tab10 Car Exiting From Garage------------------------------------------------------------------------------------------------------------------
def fetch_car_exit():
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery = "SELECT Item_Name, Quantity, Selling_Price FROM stock"
        print(savequery)
        try:
            cursor.execute(savequery)
            rows = cursor.fetchall()
            update_car_exit(rows)
        except mysql.connector.Error as e:
            messagebox.showinfo("Error",e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error",e)
    db.close()

def update_car_exit(rows):
    for i in rows:
        CarExitdata.insert('','end',values=i)

def reset_car_exit():
    CarExitdata.delete(*Cardata.get_children())
    fetch_car_exit()
#--------------------------------------------------tab10 Car Exiting From Garage-------------------------------------------------------------------------------------------------------------------------------------
def exitcar():
    t1=tab10t1.get()
    t2=tab10t2.get()
    t3=tab10t3.get()
    if t1=="":
        messagebox.showwarning("Warning","Please Enter Car Code!")
    else:
        if t2=="":
            messagebox.showwarning("Warning","Please Enter Part Name!")
        else:
            if t3=="":
                messagebox.showwarning("Warning","Please Enter Part Price")
            else:
                updateCarexit(t1,t2,t3)

def labourcharges():
    t1=tab10t1.get()
    t2=tab10t4.get()
    if t1=="":
        messagebox.showwarning("Warning","Please Enter Car Code!")
    else:
        if t2=="":
            messagebox.showwarning("Warning","Please Enter Labour Charges!")
        else:
            setcharges(t1,t2)
def setcharges(t1,t2):
    try:
        database="recept"
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery="UPDATE "+ database +" SET Machine_Fee='"+t2+"'"+" WHERE Car_Code="+t1
        try:
            cursor.execute(savequery)
            db.commit()
            # result = cursor.fetchone()
            # number_of_rows = result[0]
            #rows = cursor.fetchall()
            #numrows = int(cursor.rowcount)
            #numrows = cursor.fetchall()
            messagebox.showinfo("Information","Labour Charges Added Successful!")
            clear_Labourcharges()
            reset_carexit()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", "Invalid Data Please Retry!")
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()
    clear_Labourcharges()
    reset_carexit()

def clear_Labourcharges():
    tab10t1.delete(0,'end')
    tab10t4.delete(0,'end')

def updateCarexit(t1,t2,t3):
    try:
        database="recept"
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery="insert into "+database+"(Car_Code,Name,Price) values (%s,%s,%s)"
        try:
            cursor.execute(savequery,(t1,t2,t3))
            db.commit()
            # result = cursor.fetchone()
            # number_of_rows = result[0]
            #rows = cursor.fetchall()
            numrows = int(cursor.rowcount)
            #numrows = cursor.fetchall()
            print(numrows)
            if numrows == 1:
                messagebox.showinfo("Information","Entry Added Successful!")
                clear_exitcar()
                reset_carexit()

            else:
                messagebox.showerror("Error", "Invalid Data Please Retry!")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()
    clear_exitcar()
    reset_carexit()

def clear_exitcar():
    tab10t1.delete(0, 'end')
    tab10t2.delete(0, 'end')
    tab10t3.delete(0, 'end')

def fetch_cardata():
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery = "SELECT * FROM recept"
        print(savequery)
        try:
            cursor.execute(savequery)
            rows = cursor.fetchall()
            update_carexitdata(rows)
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
    fetch_cardata()

def createreceipt():
    t1=tab10t1.get()
    now = datetime.now()
    t2 = now.strftime("%H:%M:%S")
    t3 = date.today()
    if t1=="":
        messagebox.showwarning("Warning","Please Enter Car Code!")
    else:
            addreceiptdata(t1,t2,t3)
def addreceiptdata(t1,t2,t3):
    try:
        database="detail"
        db = mysql.connector.connect(host="localhost",user="root",password="",db="mmt_garages")
        cursor = db.cursor()
        savequery="UPDATE "+ database +" SET Exiting_Time='"+str(t2)+"'"+",Exiting_Date='"+str(t3)+"'"+" WHERE Car_Code="+t1
        try:
            cursor.execute(savequery)
            db.commit()
            # result = cursor.fetchone()
            # number_of_rows = result[0]
            #rows = cursor.fetchall()
            #numrows = int(cursor.rowcount)
            #numrows = cursor.fetchall()
            messagebox.showinfo("Information","Receipt Generated Successful!")
            clearentry()
            root.destroy()
            os.system('Receipt.py')
        except mysql.connector.Error as e:
            messagebox.showerror("Error", "Invalid Car Code Please Retry!")
            messagebox.showinfo("Error", e)
            clearentry()
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
        clearentry()
    db.close()
    clearentry()
def clearentry():
    t1=tab10t1.delete(0,'end')

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
            messagebox.showinfo("Information", "Receipt Cleared Successfully!")
            Cartdata.delete(*Cartdata.get_children())
        except mysql.connector.Error as e:
            messagebox.showerror("Error", "Cleared  Operation Failed Please Retry!")
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# top Navigation bar:
#topFrame = tk.Frame(root, bg=color["orange"])
#topFrame.pack(side="top", fill=tk.X)

# Header label text:
#homeLabel = tk.Label(topFrame, text="PE", font="Bahnschrift 15", bg=color["orange"], fg="gray17", height=2, padx=20)
#homeLabel.pack(side="right")

# Main label text:
tabControl = ttk.Notebook(SideBar)

tab1 = Frame(tabControl, background="white")#_from_rgb((33, 40, 62)))
tab2 = Frame(tabControl, background="white")#_from_rgb((33, 40, 62)))
tab3 = Frame(tabControl, background="white")#_from_rgb((33, 40, 62)))
tab4 = Frame(tabControl, background="white")#_from_rgb((33, 40, 62)))
tab5 = Frame(tabControl, background="white")#_from_rgb((33, 40, 62)))
tab6 = Frame(tabControl, background="white")#_from_rgb((33, 40, 62)))
tab7 = Frame(tabControl, background="white")#_from_rgb((33, 40, 62)))
tab8 = Frame(tabControl, background="white")
tab9 = Frame(tabControl, background="white")
tab10 = Frame(tabControl, background="white")
tab11 = Frame(tabControl, background=_from_rgb((33, 40, 62)))
tab12 = Frame(tabControl, background="gray17")

tabControl.add(tab1, text ='Tab 1')
tabControl.add(tab2, text ='Tab 2')
tabControl.add(tab3, text ='Tab 3')
tabControl.add(tab4, text ='Tab 4')
tabControl.add(tab5, text ='Tab 5')
tabControl.add(tab6, text ='Tab 6')
tabControl.add(tab7, text ='Tab 7')
tabControl.add(tab8, text ='Tab 8')
tabControl.add(tab9, text ='Tab 9')
tabControl.add(tab10, text ='Tab 10')
tabControl.add(tab11, text ='Tab 11')
tabControl.add(tab12, text ='Tab 12')
tabControl.place(x=0,y=90,height=606,width=1360)

top = Frame(SideBar,bg=_from_rgb((33,40,62)),width=1362)
top.place(x=0,y=0,height=92)

user_logo=ImageTk.PhotoImage(file="user.png")
user_label=Label(top,image=user_logo,bg=_from_rgb((33,40,62)),compound="left",text="About",font="Verdana 15 bold",fg=_from_rgb((0,200,244)))
user_label.bind("<Button>", tababout)
user_label.place(x=60,y=40)#,relwidth=1,relheight=1)

logout_logo=ImageTk.PhotoImage(file="logout.png")
logout_logo1=Label(top,image=logout_logo,bg=_from_rgb((33,40,62)),text="Logout ",compound="right",font="Verdana 15 bold",fg=_from_rgb((0,200,244)))
logout_logo1.bind("<Button>", tablogout)
logout_logo1.place(x=1230,y=40)

about_logo_student=ImageTk.PhotoImage(file="images/wallpaper.jpg")
about_image=Label(tab1,image=about_logo_student)
about_image.place(x=0,y=0)

Title=Label(top,text="MMT Garage Management System",bg=_from_rgb((33,40,62)),font="Verdana 25 bold",fg=_from_rgb((0,200,244)))
Title.place(x=380,y=10)

line_style = ttk.Style()
line_style.configure("Line.TSeparator", background=_from_rgb((0,200,244)))
separator = ttk.Separator(top,orient="horizontal",style="Line.TSeparator")
separator.place(x=60,y=70,width=1280)#relwidth=0.6, relheight=-1

# Navbar button:
navbarBtn = tk.Button(SideBar, image=navIcon, bg=_from_rgb((33,40,62)), activebackground=_from_rgb((33,40,62)), bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=30)

# setting Navbar frame:
navRoot = tk.Frame(SideBar, bg=_from_rgb((33,40,62)), height=1000, width=298,highlightthickness=3,highlightbackground=_from_rgb((0,200,244)))#300
navRoot.place(x=-300, y=0)
#tk.Label(navRoot, font="Bahnschrift 15", bg=color["orange"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 440#80
# option in the navbar:
options = ["Profile", "Settings", "Help", "About", "Feedback"]
# Navbar Option Buttons:

b1=Button(navRoot,bg=_from_rgb((33,40,62)),image=customer,compound="left",fg=_from_rgb((0,200,244)),relief="groove",width=283,text="   Customer",font = "Verdana 15 bold",activebackground=_from_rgb((0,200,244)), activeforeground=_from_rgb((33,40,62)),command=custvisible)
b1.place(x=0,y=120,height=40)

search=PhotoImage(file="search.png")
l1=Label(navRoot,bg=_from_rgb((33,40,62)),compound='left',image=search,fg=_from_rgb((0,200,244)),width=280,height=32,text="   View Customer",font = "Verdana 13 bold")
l1.bind("<Button>", viewtab2)
l1.pack_forget()

add=PhotoImage(file="add.png")
l2=Label(navRoot,bg=_from_rgb((33,40,62)),compound='left',image=add,fg=_from_rgb((0,200,244)),width=280,height=32,text="   Add Customer",font = "Verdana 13 bold")
l2.bind("<Button>", addtab3)
l2.pack_forget()

stock=PhotoImage(file="wheelbarrow.png")
b2=Button(navRoot,bg=_from_rgb((33,40,62)),image=stock,compound="left",fg=_from_rgb((0,200,244)),relief="groove",width=283,text="   Stock",font = "Verdana 15 bold",activebackground=_from_rgb((0,200,244)), activeforeground=_from_rgb((33,40,62)),command=stockvisible)
b2.place(x=0,y=250,height=40)

view_stock=PhotoImage(file="search.png")
l3=Label(navRoot,bg=_from_rgb((33,40,62)),compound='left',image=view_stock,fg=_from_rgb((0,200,244)),width=280,height=32,text="   View Stock",font = "Verdana 13 bold")
l3.bind("<Button>", viewtab4)
l3.pack_forget()

add_stock=PhotoImage(file="add.png")
l4=Label(navRoot,bg=_from_rgb((33,40,62)),compound='left',image=add_stock,fg=_from_rgb((0,200,244)),width=280,height=32,text="   Add Stock",font = "Verdana 13 bold")
l4.bind("<Button>", addtab5)
l4.pack_forget()

Employee=PhotoImage(file="employee.png")
b3=Button(navRoot,bg=_from_rgb((33,40,62)),image=Employee,compound="left",fg=_from_rgb((0,200,244)),relief="groove",width=283,text="   Employee",font = "Verdana 15 bold",activebackground=_from_rgb((0,200,244)), activeforeground=_from_rgb((33,40,62)),command=employeevisible)
b3.place(x=0,y=380,height=40)

view_employee=PhotoImage(file="search.png")
l5=Label(navRoot,bg=_from_rgb((33,40,62)),compound='left',image=view_employee,fg=_from_rgb((0,200,244)),width=280,height=32,text="   View Employee",font = "Verdana 13 bold")
l5.bind("<Button>", viewtab6)
l5.pack_forget()

add_employee=PhotoImage(file="add.png")
l6=Label(navRoot,bg=_from_rgb((33,40,62)),compound='left',image=add_employee,fg=_from_rgb((0,200,244)),width=280,height=32,text="   Add Employee",font = "Verdana 13 bold")
l6.bind("<Button>", addtab7)
l6.pack_forget()

Cars=PhotoImage(file="service.png")
b4=Button(navRoot,bg=_from_rgb((33,40,62)),image=Cars,compound="left",fg=_from_rgb((0,200,244)),relief="groove",width=283,text="   Car",font = "Verdana 15 bold",activebackground=_from_rgb((0,200,244)), activeforeground=_from_rgb((33,40,62)),command=carvisible)
b4.place(x=0,y=510,height=40)

view_cars=PhotoImage(file="search.png")
l7=Label(navRoot,bg=_from_rgb((33,40,62)),compound='left',image=view_cars,fg=_from_rgb((0,200,244)),width=280,height=32,text="   View Car",font = "Verdana 13 bold")
l7.bind("<Button>", viewtab8)
l7.pack_forget()

car_entrance=PhotoImage(file="car-repair.png")
l8=Label(navRoot,bg=_from_rgb((33,40,62)),compound='left',image=car_entrance,fg=_from_rgb((0,200,244)),width=280,height=32,text="   Car Entrance In Garage",font = "Verdana 13 bold")
l8.bind("<Button>", cartab9)
l8.pack_forget()

car_exiting=PhotoImage(file="car.png")
l9=Label(navRoot,bg=_from_rgb((33,40,62)),compound='left',image=car_exiting,fg=_from_rgb((0,200,244)),width=280,height=32,text="   Car Exiting From Garage",font = "Verdana 13 bold")
l9.bind("<Button>", cartab10)
l9.pack_forget()

home_logo=PhotoImage(file="home.png")
l10=Label(navRoot,bg=_from_rgb((33,40,62)),image=home_logo,fg=_from_rgb((0,200,244)),height=26,width=24)
l10.bind("<Button>", hometab)
l10.place(x=10,y=8)

logo_label = tk.Label(navRoot, image=logo, bg=_from_rgb((33,40,62)),bd=0,height=110,width=200)
logo_label.place(x=45, y=0)

# Navbar Close Button:
closeBtn = tk.Button(navRoot, image=closeIcon, bg=_from_rgb((33,40,62)), activebackground=_from_rgb((33,40,62)), bd=0, command=switch)
closeBtn.place(x=250, y=10)

#Inside Components Of Dashboard
#--------------------------------------------------------------------------------------------------------------------------------------------
#tab3 Add Customer
Add_Customer_logo=ImageTk.PhotoImage(file="add-friend.png")
Add_Customer=Label(tab3,image=Add_Customer_logo,bg="white",compound='left',fg=_from_rgb((33, 40, 62)),width=300,height=64,text="   Add Customer",font = "Verdana 20 bold")
Add_Customer.place(x=0,y=0)

tab3line_style = ttk.Style()
tab3line_style.configure("Line1.TSeparator", background=_from_rgb((33, 40, 62)))
tab3separator = ttk.Separator(tab3,orient="horizontal",style="Line1.TSeparator")
tab3separator.place(x=0,y=75,width=1360)

tab3l1=Label(tab3,text="Customer Code",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=500,y=100)
tab3l2=Label(tab3,text="Customer Name",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=490,y=140)
tab3l3=Label(tab3,text="CNIC Number",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=515,y=180)
tab3l4=Label(tab3,text="Date of Birth",bg="white",fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold").place(x=520,y=220)

tab3l5=Label(tab3,text="Gender",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=580,y=260)
tab3l6=Label(tab3,text="Mobile No",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=550,y=300)
tab3l7=Label(tab3,text="Email Address",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=500,y=340)
tab3l8=Label(tab3,text="Car Name",bg="white",fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold").place(x=550,y=380)

tab3l9=Label(tab3,text="Car Model",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=550,y=420)
tab3l10=Label(tab3,text="Car Registration Number",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=386,y=460)
tab3l11=Label(tab3,text="Address",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=570,y=500)

tab3l12=Label(tab3,bg="white",width=13, highlightthickness=0,bd=0,text="Auto Generated",justify=CENTER,fg=_from_rgb((0,200,244)),font = "Verdana 12 bold")
tab3l12.place(height=30,x=680,y=104)
#separator = ttk.Separator(tab3,orient="horizontal",style="Line1.TSeparator")
#separator.place(x=680,y=128,width=182 )

tab3t2=Entry(tab3,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab3t2.place(height=30,x=680,y=140)
separator = ttk.Separator(tab3,orient="horizontal",style="Line1.TSeparator")
separator.place(x=680,y=168,width=182 )

tab3t3=Entry(tab3,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab3t3.place(height=30,x=680,y=180)
separator = ttk.Separator(tab3,orient="horizontal",style="Line1.TSeparator")
separator.place(x=680,y=208,width=182 )

tab3t4=Entry(tab3,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab3t4.place(height=30,x=680,y=220)
separator = ttk.Separator(tab3,orient="horizontal",style="Line1.TSeparator")
separator.place(x=680,y=248,width=182 )

tab3t5=Entry(tab3,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab3t5.place(height=30,x=680,y=260)
separator = ttk.Separator(tab3,orient="horizontal",style="Line1.TSeparator")
separator.place(x=680,y=288,width=182 )

tab3t6=Entry(tab3,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab3t6.place(height=30,x=680,y=300)
separator = ttk.Separator(tab3,orient="horizontal",style="Line1.TSeparator")
separator.place(x=680,y=328,width=182 )

tab3t7=Entry(tab3,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab3t7.place(height=30,x=680,y=340)
separator = ttk.Separator(tab3,orient="horizontal",style="Line1.TSeparator")
separator.place(x=680,y=368,width=182 )

tab3t8=Entry(tab3,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab3t8.place(height=30,x=680,y=380)
separator = ttk.Separator(tab3,orient="horizontal",style="Line1.TSeparator")
separator.place(x=680,y=408,width=182 )

tab3t9=Entry(tab3,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab3t9.place(height=30,x=680,y=420)
separator = ttk.Separator(tab3,orient="horizontal",style="Line1.TSeparator")
separator.place(x=680,y=448,width=182 )

tab3t10=Entry(tab3,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab3t10.place(height=30,x=680,y=460)
separator = ttk.Separator(tab3,orient="horizontal",style="Line1.TSeparator")
separator.place(x=680,y=488,width=182 )

tab3t11=Entry(tab3,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab3t11.place(height=30,x=680,y=500)
separator = ttk.Separator(tab3,orient="horizontal",style="Line1.TSeparator")
separator.place(x=680,y=528,width=182 )

tab3b1=Button(tab3,bg=_from_rgb((33, 40, 62)),bd=0,width=13,text="SAVE",font = "Verdana 10 bold",fg=_from_rgb((0,200,244)),command=addcustomer)
tab3b1.place(x=650,y=560,height=35)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#tab5 Add stock
Add_Stock_logo=ImageTk.PhotoImage(file="cart.png")
Add_Stock=Label(tab5,image=Add_Stock_logo,bg="white",compound='left',fg=_from_rgb((33, 40, 62)),width=300,height=64,text="   Add Item",font = "Verdana 20 bold")
Add_Stock.place(x=0,y=0)

tab5line_style = ttk.Style()
tab5line_style.configure("Line2.TSeparator", background=_from_rgb((33, 40, 62)))
tab5separator = ttk.Separator(tab5,orient="horizontal",style="Line2.TSeparator")
tab5separator.place(x=0,y=75,width=1360)

tab5l1=Label(tab5,text="Item Code",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=540,y=100)
tab5l2=Label(tab5,text="Item Name",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=535,y=140)
tab5l3=Label(tab5,text="Category",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=560,y=180)
tab5l4=Label(tab5,text="Quantity",bg="white",fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold").place(x=565,y=220)

tab5l5=Label(tab5,text="Buying Price (INR)",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=450,y=260)
tab5l6=Label(tab5,text="Selling Price (INR)",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=450,y=300)
tab5l7=Label(tab5,text="Car Name",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=550,y=340)
tab5l8=Label(tab5,text="Time Of Entry",bg="white",fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold").place(x=500,y=380)

tab5l9=Label(tab5,text="Date Of Entry",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=500,y=420)
tab5l10=Label(tab5,text="Warranty",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=550,y=460)


tab5l12=Label(tab5,bg="white",width=13, highlightthickness=0,bd=0,text="Auto Generated",justify=CENTER,fg=_from_rgb((0,200,244)),font = "Verdana 12 bold")
tab5l12.place(height=30,x=680,y=104)
#separator = ttk.Separator(tab3,orient="horizontal",style="Line1.TSeparator")
#separator.place(x=680,y=128,width=182 )

tab5t2=Entry(tab5,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab5t2.place(height=30,x=680,y=140)
separator = ttk.Separator(tab5,orient="horizontal",style="Line2.TSeparator")
separator.place(x=680,y=168,width=182 )

n = tk.StringVar()
tab5t3 = ttk.Combobox(tab5, width=27, textvariable=n)
tab5t3['values'] = ("Door and Windows", "Air Conditioning System", "Modification Parts", "Body Parts", "Audio Video Devices", "Electronics", "Denting Painting", "Engine Parts")
tab5t3.place(height=30,x=680,y=180)
tab5t3.set('Door and Windows')
#tab5t3.current()

#tab5t3=Entry(tab5,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
#tab5t3.place(height=30,x=680,y=180)
#separator = ttk.Separator(tab5,orient="horizontal",style="Line2.TSeparator")
#separator.place(x=680,y=208,width=182 )


tab5t4=Spinbox(tab5,bg="white",width=12, from_=0, to=1000,highlightthickness=0,bd=1,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab5t4.place(height=25,x=680,y=232)
#separator = ttk.Separator(tab5,orient="horizontal",style="Line2.TSeparator")
#separator.place(x=680,y=248,width=182 )

tab5t5=Entry(tab5,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab5t5.place(height=30,x=680,y=260)
separator = ttk.Separator(tab5,orient="horizontal",style="Line2.TSeparator")
separator.place(x=680,y=288,width=182 )

tab5t6=Entry(tab5,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab5t6.place(height=30,x=680,y=300)
separator = ttk.Separator(tab5,orient="horizontal",style="Line2.TSeparator")
separator.place(x=680,y=328,width=182 )

tab5t7=Entry(tab5,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab5t7.place(height=30,x=680,y=340)
separator = ttk.Separator(tab5,orient="horizontal",style="Line2.TSeparator")
separator.place(x=680,y=368,width=182 )

tab5l13=Label(tab5,bg="white",width=13,highlightthickness=0,bd=0,text="Auto Entered",justify=CENTER,fg=_from_rgb((0,200,244)),font = "Verdana 12 bold")
tab5l13.place(height=30,x=680,y=390)

tab5l14=Label(tab5,bg="white",width=13,highlightthickness=0,bd=0,text="Auto Entered",justify=CENTER,fg=_from_rgb((0,200,244)),font = "Verdana 12 bold")
tab5l14.place(height=30,x=680,y=430)
# tab5t8=Entry(tab5,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
# tab5t8.place(height=30,x=680,y=380)
# separator = ttk.Separator(tab5,orient="horizontal",style="Line2.TSeparator")
# separator.place(x=680,y=408,width=182 )

#tab5t9=Entry(tab5,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
#tab5t9.place(height=30,x=680,y=420)
#separator = ttk.Separator(tab5,orient="horizontal",style="Line2.TSeparator")
#separator.place(x=680,y=448,width=182 )

tab5t10=Entry(tab5,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab5t10.place(height=30,x=680,y=460)
separator = ttk.Separator(tab5,orient="horizontal",style="Line2.TSeparator")
separator.place(x=680,y=488,width=182 )

#tab5t11=Entry(tab5,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
#tab5t11.place(height=30,x=680,y=500)
#separator = ttk.Separator(tab5,orient="horizontal",style="Line2.TSeparator")
#separator.place(x=680,y=528,width=182 )

tab5b1=Button(tab5,bg=_from_rgb((33, 40, 62)),bd=0,width=13,text="SAVE",font = "Verdana 10 bold",fg=_from_rgb((0,200,244)),command=addstock)
tab5b1.place(x=650,y=520,height=35)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#tab7 Add Employee
Add_Employee_logo=ImageTk.PhotoImage(file="add-friend (1).png")
Add_Employee=Label(tab7,image=Add_Employee_logo,bg="white",compound='left',fg=_from_rgb((33, 40, 62)),width=300,height=64,text="   Add Employee",font = "Verdana 20 bold")
Add_Employee.place(x=0,y=0)

tab7line_style = ttk.Style()
tab7line_style.configure("Line3.TSeparator", background=_from_rgb((33, 40, 62)))
tab7separator = ttk.Separator(tab7,orient="horizontal",style="Line3.TSeparator")
tab7separator.place(x=0,y=75,width=1360)

tab7l1=Label(tab7,text="Employee Code",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=490,y=100)
tab7l2=Label(tab7,text="Employee Name",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=480,y=140)
tab7l3=Label(tab7,text="CNIC Number",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=505,y=180)
tab7l4=Label(tab7,text="Designation",bg="white",fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold").place(x=525,y=216)

tab7l5=Label(tab7,text="Date Of Birth",bg="white",fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold").place(x=512,y=260)

tab7l6=Label(tab7,text="Gender",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=580,y=300)
tab7l7=Label(tab7,text="Mobile No",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=550,y=340)
tab7l8=Label(tab7,text="Email Address",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=500,y=380)
tab7l9=Label(tab7,text="Date of Joining",bg="white",fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold").place(x=490,y=420)

#tab7l9=Label(tab7,text="Car Model",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=550,y=420)
#tab7l10=Label(tab7,text="Car Registration Number",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=386,y=460)
tab7l10=Label(tab7,text="Address",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=570,y=460)#500

tab7l11=Label(tab7,bg="white",width=13, highlightthickness=0,bd=0,text="Auto Generated",justify=CENTER,fg=_from_rgb((0,200,244)),font = "Verdana 12 bold")
tab7l11.place(height=30,x=680,y=104)

tab7l12=Label(tab7,bg="white",width=13, highlightthickness=0,bd=0,text="Extra Details",justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab7l12.place(height=30,x=420,y=500)

tab7l13=Label(tab7,bg="white",width=10, highlightthickness=0,bd=0,text="(Optional)",justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 10 bold")
tab7l13.place(height=30,x=585,y=500)

#separator = ttk.Separator(tab3,orient="horizontal",style="Line1.TSeparator")
#separator.place(x=680,y=128,width=182 )

tab7t2=Entry(tab7,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab7t2.place(height=30,x=680,y=140)
separator = ttk.Separator(tab7,orient="horizontal",style="Line3.TSeparator")
separator.place(x=680,y=168,width=182 )

tab7t3=Entry(tab7,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab7t3.place(height=30,x=680,y=180)
separator = ttk.Separator(tab7,orient="horizontal",style="Line3.TSeparator")
separator.place(x=680,y=208,width=182 )

tab7t4=Entry(tab7,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab7t4.place(height=30,x=680,y=220)
separator = ttk.Separator(tab7,orient="horizontal",style="Line3.TSeparator")
separator.place(x=680,y=248,width=182 )

tab7t5=Entry(tab7,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab7t5.place(height=30,x=680,y=260)
separator = ttk.Separator(tab7,orient="horizontal",style="Line3.TSeparator")
separator.place(x=680,y=288,width=182 )

tab7t6=Entry(tab7,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab7t6.place(height=30,x=680,y=300)
separator = ttk.Separator(tab7,orient="horizontal",style="Line3.TSeparator")
separator.place(x=680,y=328,width=182 )

tab7t7=Entry(tab7,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab7t7.place(height=30,x=680,y=340)
separator = ttk.Separator(tab7,orient="horizontal",style="Line3.TSeparator")
separator.place(x=680,y=368,width=182 )

tab7t8=Entry(tab7,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab7t8.place(height=30,x=680,y=380)
separator = ttk.Separator(tab7,orient="horizontal",style="Line3.TSeparator")
separator.place(x=680,y=408,width=182 )

#tab7t9=Entry(tab7,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
#tab7t9.place(height=30,x=680,y=420)
#separator = ttk.Separator(tab7,orient="horizontal",style="Line1.TSeparator")
#separator.place(x=680,y=448,width=182 )

#tab7t10=Entry(tab7,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
#tab7t10.place(height=30,x=680,y=460)
#separator = ttk.Separator(tab7,orient="horizontal",style="Line1.TSeparator")
#separator.place(x=680,y=488,width=182 )

tab7t9=Entry(tab7,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab7t9.place(height=30,x=680,y=420)
separator = ttk.Separator(tab7,orient="horizontal",style="Line3.TSeparator")
separator.place(x=680,y=448,width=182 )

tab7t10=Entry(tab7,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab7t10.place(height=30,x=680,y=460)
separator = ttk.Separator(tab7,orient="horizontal",style="Line3.TSeparator")
separator.place(x=680,y=488,width=182 )

tab7t11=Entry(tab7,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab7t11.place(height=30,x=680,y=500)
separator = ttk.Separator(tab7,orient="horizontal",style="Line3.TSeparator")
separator.place(x=680,y=528,width=182 )

tab7b1=Button(tab7,bg=_from_rgb((33, 40, 62)),bd=0,width=13,text="SAVE",font = "Verdana 10 bold",fg=_from_rgb((0,200,244)),command=addemployee)
tab7b1.place(x=650,y=540,height=35)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#tab9 Add Car
Car_Entrance_logo=ImageTk.PhotoImage(file="repair.png")
Car_Entrance=Label(tab9,image=Car_Entrance_logo,bg="white",compound='left',fg=_from_rgb((33, 40, 62)),width=300,height=64,text="   Add Car",font = "Verdana 20 bold")
Car_Entrance.place(x=0,y=0)

tab9line_style = ttk.Style()
tab9line_style.configure("Line4.TSeparator", background=_from_rgb((33, 40, 62)))
tab9separator = ttk.Separator(tab9,orient="horizontal",style="Line4.TSeparator")
tab9separator.place(x=0,y=75,width=1360)

tab9l1=Label(tab9,text="Car Code",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=550,y=100)
tab9l2=Label(tab9,text="Car Name",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=540,y=140)
tab9l3=Label(tab9,text="Car Model",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=537,y=180)
tab9l4=Label(tab9,text="Registration Number",bg="white",fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold").place(x=414,y=220)

tab9l5=Label(tab9,text="Date of Entry",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=500,y=260)
tab9l6=Label(tab9,text="Time of Entry",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=498,y=300)
tab9l7=Label(tab9,text="Owner Name",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=504,y=340)
tab9l8=Label(tab9,text="Owner CNIC Number",bg="white",fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold").place(x=416,y=380)

tab9l9=Label(tab9,text="Car Color",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=546,y=420)
tab9l10=Label(tab9,text="Extra Details",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=505,y=460)
#tab9l11=Label(tab9,text="Address",fg=_from_rgb((33, 40, 62)),bg="white",font = "Verdana 15 bold").place(x=560,y=500)

tab9l11=Label(tab9,bg="white",width=13, highlightthickness=0,bd=0,text="Auto Generated",justify=CENTER,fg=_from_rgb((0,200,244)),font = "Verdana 12 bold")
tab9l11.place(height=30,x=680,y=104)
#separator = ttk.Separator(tab3,orient="horizontal",style="Line1.TSeparator")
#separator.place(x=680,y=128,width=182 )

tab9t2=Entry(tab9,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab9t2.place(height=30,x=680,y=140)
separator = ttk.Separator(tab9,orient="horizontal",style="Line4.TSeparator")
separator.place(x=680,y=168,width=182 )

tab9t3=Entry(tab9,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab9t3.place(height=30,x=680,y=180)
separator = ttk.Separator(tab9,orient="horizontal",style="Line4.TSeparator")
separator.place(x=680,y=208,width=182 )

tab9t4=Entry(tab9,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab9t4.place(height=30,x=680,y=220)
separator = ttk.Separator(tab9,orient="horizontal",style="Line4.TSeparator")
separator.place(x=680,y=248,width=182 )

tab9t5=Label(tab9,fg=_from_rgb((0,200,244)),width=13,text="Auto Entered",highlightthickness=0,bd=0,justify=CENTER,bg="white",font = "Verdana 12 bold")
tab9t5.place(height=30,x=680,y=263)
#separator = ttk.Separator(tab8,orient="horizontal",style="Line4.TSeparator")
#separator.place(x=680,y=288,width=182 )

tab9t6=Label(tab9,fg=_from_rgb((0,200,244)),width=13,text="Auto Entered",highlightthickness=0,bd=0,justify=CENTER,bg="white",font = "Verdana 12 bold")
tab9t6.place(height=30,x=680,y=303)
#separator = ttk.Separator(tab8,orient="horizontal",style="Line4.TSeparator")
#separator.place(x=680,y=328,width=182 )

tab9t7=Entry(tab9,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab9t7.place(height=30,x=680,y=340)
separator = ttk.Separator(tab9,orient="horizontal",style="Line4.TSeparator")
separator.place(x=680,y=368,width=182 )

tab9t8=Entry(tab9,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab9t8.place(height=30,x=680,y=380)
separator = ttk.Separator(tab9,orient="horizontal",style="Line4.TSeparator")
separator.place(x=680,y=408,width=182 )

tab9t9=Entry(tab9,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab9t9.place(height=30,x=680,y=420)
separator = ttk.Separator(tab9,orient="horizontal",style="Line4.TSeparator")
separator.place(x=680,y=448,width=182)

tab9t10=Entry(tab9,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
tab9t10.place(height=30,x=680,y=460)
separator = ttk.Separator(tab9,orient="horizontal",style="Line4.TSeparator")
separator.place(x=680,y=488,width=182)

#tab9t11=Entry(tab9,bg="white",width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
#tab9t11.place(height=30,x=680,y=500)
#separator = ttk.Separator(tab9,orient="horizontal",style="Line3.TSeparator")
#separator.place(x=680,y=528,width=182)

tab9b1=Button(tab9,bg=_from_rgb((33, 40, 62)),bd=0,width=13,text="SAVE",font = "Verdana 10 bold",fg=_from_rgb((0,200,244)),command=addcar)
tab9b1.place(x=650,y=510,height=35)
#-------------------------------------------------------------------------------tab2 View Customer-----------------------------------------------------------------------------------
c1 = StringVar()
c2 = StringVar()
c3 = StringVar()
c4 = StringVar()
c5 = StringVar()
c6 = StringVar()
c7 = StringVar()
c8 = StringVar()
c9 = StringVar()
c10 = StringVar()
c11 = StringVar()

style5 = ttk.Style()
#style5.theme_use("clam")
style5.layout('TNotebook.Tab', [])
style5.configure("Treeview.Heading", background=_from_rgb((33, 40, 62)),fieldbackground=_from_rgb((33, 40, 62)),foreground=_from_rgb((0,200,244)))


View_Customer_Frame = Frame(tab2,bg=_from_rgb((0,200,244)))
View_Customer_Frame.place(x=0,y=2,height=65,width=1362)

View_Customer_logo=ImageTk.PhotoImage(file="customer_logo.png")
View_Customer_image=Label(View_Customer_Frame,compound='left',image=View_Customer_logo,bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),text="   View Customer",font = "Verdana 20 bold")
View_Customer_image.place(x=510,y=-1)

Customerdata = ttk.Treeview(tab2,columns=(1,2,3,4,5,6,7,8,9,10,11),show="headings",height="26")
Customerdata.bind('<Double 1>',getrow_Customerdb)
Customerdata.place(x=0,y=70,width="680")
Customerdata.heading(1,text="Customer Code")
Customerdata.heading(2,text="Customer Name")
Customerdata.heading(3,text="CNIC Number")
Customerdata.heading(4,text="Date of Birth")
Customerdata.heading(5,text="Gender")
Customerdata.heading(6,text="Phone Number")
Customerdata.heading(7,text="Email Address")
Customerdata.heading(8,text="Car Name")
Customerdata.heading(9,text="Car Model")
Customerdata.heading(10,text="Car Registration Number")
Customerdata.heading(11,text="Address")
Customerdata.column(1, anchor=tkinter.N,minwidth=0, width=110, stretch=NO)
Customerdata.column(2, anchor=tkinter.N,minwidth=0, width=110, stretch=NO)
Customerdata.column(3, anchor=tkinter.N,minwidth=0, width=110, stretch=NO)
Customerdata.column(4, anchor=tkinter.N,minwidth=0, width=110, stretch=NO)
Customerdata.column(5, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
Customerdata.column(6, anchor=tkinter.N,minwidth=0, width=135, stretch=NO)
Customerdata.column(7, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
Customerdata.column(8, anchor=tkinter.N,minwidth=0, width=141, stretch=NO)
Customerdata.column(9, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
Customerdata.column(10, anchor=tkinter.N,minwidth=0, width=141, stretch=NO)
Customerdata.column(11, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
fetch_customer()

tab2line_style = ttk.Style()
tab2line_style.configure("tab2.TSeparator", background=_from_rgb((33, 40, 62)))
separator = ttk.Separator(tab2,orient='vertical',style="tab2.TSeparator")
separator.place(x=730,y=67,width=3, height=535)

separator1 = ttk.Separator(tab2,orient='vertical',style="tab2.TSeparator")
separator1.place(x=677,y=67,width=3, height=535)

Edit_Customer_Frame = Frame(tab2,bg=_from_rgb((0,200,244)))
Edit_Customer_Frame.place(x=780,y=70,height=530,width=500)


Delete_Customer_logo=ImageTk.PhotoImage(file="trash-bin.png")
Delete_Customer_label=Label(Edit_Customer_Frame,image=Delete_Customer_logo,bg=_from_rgb((33, 40, 62)))
Delete_Customer_label.bind("<Button>", remove_customer)
Delete_Customer_label.place(x=0,y=0)

Save_Customer_logo=ImageTk.PhotoImage(file="edit.png")
Save_Customer_label=Label(Edit_Customer_Frame,image=Save_Customer_logo,bg=_from_rgb((33, 40, 62)))
Save_Customer_label.bind("<Button>", update_customerdata)
Save_Customer_label.place(x=463,y=0)

Customer_Details_Label=Label(Edit_Customer_Frame,text="Customer Details",bg=_from_rgb((33, 40, 62)),height="0",fg=_from_rgb((0,200,244)),font = "Verdana 15 bold").place(x=150,y=0)

tab2l1=Label(Edit_Customer_Frame,text="Customer Code",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=120,y=50)
tab2l2=Label(Edit_Customer_Frame,text="Customer Name",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=114,y=90)
tab2l3=Label(Edit_Customer_Frame,text="CNIC Number",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=132,y=130)
tab2l4=Label(Edit_Customer_Frame,text="Date of Birth",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Tahoma 14 normal").place(x=140,y=170)

tab2l5=Label(Edit_Customer_Frame,text="Gender",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=180,y=210)
tab2l6=Label(Edit_Customer_Frame,text="Mobile No",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=158,y=250)
tab2l7=Label(Edit_Customer_Frame,text="Email Address",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=124,y=290)
tab2l8=Label(Edit_Customer_Frame,text="Car Name",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Tahoma 14 normal").place(x=156,y=330)

tab2l9=Label(Edit_Customer_Frame,text="Car Model",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=156,y=370)
tab2l10=Label(Edit_Customer_Frame,text="Car Registration Number",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=35,y=410)
tab2l11=Label(Edit_Customer_Frame,text="Address",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=172,y=450)

tab2line_style = ttk.Style()
tab2line_style.configure("tab2.TSeparator", background=_from_rgb((33, 40, 62)))


tab2t1=Entry(Edit_Customer_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=c1)
tab2t1.place(height=24,x=260,y=50)
separator = ttk.Separator(Edit_Customer_Frame,orient="horizontal",style="tab2.TSeparator")
separator.place(x=260,y=71,width=182)

tab2t2=Entry(Edit_Customer_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=c2)
tab2t2.place(height=24,x=260,y=90)
separator = ttk.Separator(Edit_Customer_Frame,orient="horizontal",style="tab2.TSeparator")
separator.place(x=260,y=111,width=182)

tab2t3=Entry(Edit_Customer_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=c3)
tab2t3.place(height=24,x=260,y=130)
separator = ttk.Separator(Edit_Customer_Frame,orient="horizontal",style="tab2.TSeparator")
separator.place(x=260,y=151,width=182)

tab2t4=Entry(Edit_Customer_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=c4)
tab2t4.place(height=24,x=260,y=170)
separator = ttk.Separator(Edit_Customer_Frame,orient="horizontal",style="tab2.TSeparator")
separator.place(x=260,y=191,width=182)

tab2t5=Entry(Edit_Customer_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=c5)
tab2t5.place(height=24,x=260,y=210)
separator = ttk.Separator(Edit_Customer_Frame,orient="horizontal",style="tab2.TSeparator")
separator.place(x=260,y=231,width=182)

tab2t6=Entry(Edit_Customer_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=c6)
tab2t6.place(height=24,x=260,y=250)
separator = ttk.Separator(Edit_Customer_Frame,orient="horizontal",style="tab2.TSeparator")
separator.place(x=260,y=271,width=182)

tab2t7=Entry(Edit_Customer_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=c7)
tab2t7.place(height=24,x=260,y=290)
separator = ttk.Separator(Edit_Customer_Frame,orient="horizontal",style="tab2.TSeparator")
separator.place(x=260,y=311,width=182)

tab2t8=Entry(Edit_Customer_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=c8)
tab2t8.place(height=24,x=260,y=330)
separator = ttk.Separator(Edit_Customer_Frame,orient="horizontal",style="tab2.TSeparator")
separator.place(x=260,y=351,width=182)

tab2t9=Entry(Edit_Customer_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=c9)
tab2t9.place(height=24,x=260,y=370)
separator = ttk.Separator(Edit_Customer_Frame,orient="horizontal",style="tab2.TSeparator")
separator.place(x=260,y=391,width=182)

tab2t10=Entry(Edit_Customer_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=c10)
tab2t10.place(height=24,x=260,y=410)
separator = ttk.Separator(Edit_Customer_Frame,orient="horizontal",style="tab2.TSeparator")
separator.place(x=260,y=431,width=182)

tab2t11=Entry(Edit_Customer_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=c11)
tab2t11.place(height=24,x=260,y=450)
separator = ttk.Separator(Edit_Customer_Frame,orient="horizontal",style="tab2.TSeparator")
separator.place(x=260,y=471,width=182)

#------------------------------------------------------------tab4 View Stock---------------------------------------------------------------------------------------
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

style4 = ttk.Style()
style4.theme_use("clam")
style4.layout('TNotebook.Tab', [])
style4.configure("Treeview.Heading", background=_from_rgb((33, 40, 62)),fieldbackground=_from_rgb((33, 40, 62)),foreground=_from_rgb((0,200,244)))


View_Stock_Frame = Frame(tab4,bg=_from_rgb((0,200,244)))
View_Stock_Frame.place(x=0,y=2,height=65,width=1362)

View_Stock_logo=ImageTk.PhotoImage(file="Shopping-Cart.png")
View_Stock_image=Label(View_Stock_Frame,compound='left',image=View_Stock_logo,bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),text="   View Stock",font = "Verdana 20 bold")
View_Stock_image.place(x=510,y=-1)

Stockdata = ttk.Treeview(tab4,columns=(1,2,3,4,5,6,7,8,9,10),show="headings",height="26")
Stockdata.bind('<Double 1>',getrow_Stockdb)
Stockdata.place(x=0,y=70,width="680")
Stockdata.heading(1,text="Item Number")
Stockdata.heading(2,text="Item Name")
Stockdata.heading(3,text="Category")
Stockdata.heading(4,text="Quantity")
Stockdata.heading(5,text="Buying Price")
Stockdata.heading(6,text="Selling Price")
Stockdata.heading(7,text="Car Name")
Stockdata.heading(8,text="Time Of Entry")
Stockdata.heading(9,text="Date Of Entry")
Stockdata.heading(10,text="Warranty")
Stockdata.column(1, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
Stockdata.column(2, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
Stockdata.column(3, anchor=tkinter.N,minwidth=0, width=97, stretch=NO)
Stockdata.column(4, anchor=tkinter.N,minwidth=0, width=80, stretch=NO)
Stockdata.column(5, anchor=tkinter.N,minwidth=0, width=87, stretch=NO)
Stockdata.column(6, anchor=tkinter.N,minwidth=0, width=112, stretch=NO)
Stockdata.column(7, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
Stockdata.column(8, anchor=tkinter.N,minwidth=0, width=141, stretch=NO)
Stockdata.column(9, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
Stockdata.column(10, anchor=tkinter.N,minwidth=0, width=141, stretch=NO)
fetch_stock()

tab4line_style = ttk.Style()
tab4line_style.configure("tab4.TSeparator", background=_from_rgb((33, 40, 62)))
separator = ttk.Separator(tab4,orient='vertical',style="tab4.TSeparator")
separator.place(x=730,y=67,width=3, height=535)

separator2 = ttk.Separator(tab4,orient='vertical',style="tab2.TSeparator")
separator2.place(x=677,y=67,width=3, height=535)

Edit_Stock_Frame = Frame(tab4,bg=_from_rgb((0,200,244)))
Edit_Stock_Frame.place(x=780,y=70,height=530,width=500)


Delete_Stock_logo=ImageTk.PhotoImage(file="trash-bin.png")
Delete_Stock_label=Label(Edit_Stock_Frame,image=Delete_Stock_logo,bg=_from_rgb((33, 40, 62)))
Delete_Stock_label.bind("<Button>",remoeve_stock)
Delete_Stock_label.place(x=0,y=0)

Save_Stock_logo=ImageTk.PhotoImage(file="edit.png")
Save_Stock_label=Label(Edit_Stock_Frame,image=Save_Stock_logo,bg=_from_rgb((33, 40, 62)))
Save_Stock_label.bind("<Button>", update_stockdata)
Save_Stock_label.place(x=463,y=0)

Customer_Stock_Label=Label(Edit_Stock_Frame,text="Stock Details",bg=_from_rgb((33, 40, 62)),height="0",fg=_from_rgb((0,200,244)),font = "Verdana 15 bold").place(x=170,y=0)

tab4l1=Label(Edit_Stock_Frame,text="Item Number",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=120,y=50)
tab4l2=Label(Edit_Stock_Frame,text="Item Name",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=135,y=90)
tab4l3=Label(Edit_Stock_Frame,text="Category",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=155,y=130)
tab4l4=Label(Edit_Stock_Frame,text="Quantity",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Tahoma 14 normal").place(x=160,y=170)

tab4l5=Label(Edit_Stock_Frame,text="Buying Price(INR)",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=80,y=210)
tab4l6=Label(Edit_Stock_Frame,text="Profit on an Item(INR)",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=40,y=250)
tab4l7=Label(Edit_Stock_Frame,text="Item belongs to Car",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=60,y=290)
tab4l8=Label(Edit_Stock_Frame,text="Time of Entry",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Tahoma 14 normal").place(x=110,y=330)

tab4l9=Label(Edit_Stock_Frame,text="Date of Entry",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=110,y=370)
tab4l10=Label(Edit_Stock_Frame,text="Warranty",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=145,y=410)

tab4line_style = ttk.Style()
tab4line_style.configure("tab4.TSeparator", background=_from_rgb((33, 40, 62)))


tab4t1=Entry(Edit_Stock_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=s1)
tab4t1.place(height=24,x=260,y=50)
separator = ttk.Separator(Edit_Stock_Frame,orient="horizontal",style="tab4.TSeparator")
separator.place(x=260,y=72,width=182)

tab4t2=Entry(Edit_Stock_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=s2)
tab4t2.place(height=24,x=260,y=90)
separator = ttk.Separator(Edit_Stock_Frame,orient="horizontal",style="tab4.TSeparator")
separator.place(x=260,y=112,width=182)

tab4t3=Entry(Edit_Stock_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=s3)
tab4t3.place(height=24,x=260,y=130)
separator = ttk.Separator(Edit_Stock_Frame,orient="horizontal",style="tab4.TSeparator")
separator.place(x=260,y=152,width=182)

tab4t4=Entry(Edit_Stock_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=s4)
tab4t4.place(height=24,x=260,y=170)
separator = ttk.Separator(Edit_Stock_Frame,orient="horizontal",style="tab4.TSeparator")
separator.place(x=260,y=192,width=182)

tab4t5=Entry(Edit_Stock_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=s5)
tab4t5.place(height=24,x=260,y=210)
separator = ttk.Separator(Edit_Stock_Frame,orient="horizontal",style="tab4.TSeparator")
separator.place(x=260,y=232,width=182)

tab4t6=Entry(Edit_Stock_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=s6)
tab4t6.place(height=24,x=260,y=250)
separator = ttk.Separator(Edit_Stock_Frame,orient="horizontal",style="tab4.TSeparator")
separator.place(x=260,y=272,width=182)

tab4t7=Entry(Edit_Stock_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=s7)
tab4t7.place(height=24,x=260,y=290)
separator = ttk.Separator(Edit_Stock_Frame,orient="horizontal",style="tab4.TSeparator")
separator.place(x=260,y=312,width=182)

tab4t8=Entry(Edit_Stock_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=s8)
tab4t8.place(height=24,x=260,y=330)
separator = ttk.Separator(Edit_Stock_Frame,orient="horizontal",style="tab4.TSeparator")
separator.place(x=260,y=352,width=182)

tab4t9=Entry(Edit_Stock_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=s9)
tab4t9.place(height=24,x=260,y=370)
separator = ttk.Separator(Edit_Stock_Frame,orient="horizontal",style="tab4.TSeparator")
separator.place(x=260,y=392,width=182)

tab4t10=Entry(Edit_Stock_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=s10)
tab4t10.place(height=24,x=260,y=410)
separator = ttk.Separator(Edit_Stock_Frame,orient="horizontal",style="tab4.TSeparator")
separator.place(x=260,y=432,width=182)
#------------------------------------------------------------------------tab6 View Employee------------------------------------------------------------------------
e1 = StringVar()
e2 = StringVar()
e3 = StringVar()
e4 = StringVar()
e5 = StringVar()
e6 = StringVar()
e7 = StringVar()
e8 = StringVar()
e9 = StringVar()
e10 = StringVar()
e11 = StringVar()




style6 = ttk.Style()
style6.theme_use("clam")
style6.layout('TNotebook.Tab', [])
style6.configure("Treeview.Heading", background=_from_rgb((33, 40, 62)),fieldbackground=_from_rgb((33, 40, 62)),foreground=_from_rgb((0,200,244)))


View_Employee_Frame = Frame(tab6,bg=_from_rgb((0,200,244)))
View_Employee_Frame.place(x=0,y=2,height=65,width=1362)

View_Employee_logo=ImageTk.PhotoImage(file="team.png")
View_Employee_image=Label(View_Employee_Frame,compound='left',image=View_Employee_logo,bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),text="   View Employees",font = "Verdana 20 bold")
View_Employee_image.place(x=510,y=-1)

Employeedata = ttk.Treeview(tab6,columns=(1,2,3,4,5,6,7,8,9,10,11),show="headings",height="26")
Employeedata.bind('<Double 1>',getrow_Employeedb)
Employeedata.place(x=0,y=70,width="680")
Employeedata.heading(1,text="Employee No")
Employeedata.heading(2,text="Employee Name")
Employeedata.heading(3,text="CNIC Number")
Employeedata.heading(4,text="Designation")
Employeedata.heading(5,text="Date of Birth")
Employeedata.heading(6,text="Gender")
Employeedata.heading(7,text="Phone Number")
Employeedata.heading(8,text="Email Address")
Employeedata.heading(9,text="Date of Joining")
Employeedata.heading(10,text="Address")
Employeedata.heading(11,text="Extra Details")
Employeedata.column(1, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
Employeedata.column(2, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
Employeedata.column(3, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
Employeedata.column(4, anchor=tkinter.N,minwidth=0, width=90, stretch=NO)
Employeedata.column(5, anchor=tkinter.N,minwidth=0, width=75, stretch=NO)
Employeedata.column(6, anchor=tkinter.N,minwidth=0, width=110, stretch=NO)
Employeedata.column(7, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
Employeedata.column(8, anchor=tkinter.N,minwidth=0, width=141, stretch=NO)
Employeedata.column(9, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
Employeedata.column(10, anchor=tkinter.N,minwidth=0, width=141, stretch=NO)
Employeedata.column(11, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
fetch_employee()

tab6line_style = ttk.Style()
tab6line_style.configure("tab6.TSeparator", background=_from_rgb((33, 40, 62)))
separator = ttk.Separator(tab6,orient='vertical',style="tab6.TSeparator")
separator.place(x=730,y=67,width=3, height=535)

separator3 = ttk.Separator(tab6,orient='vertical',style="tab2.TSeparator")
separator3.place(x=677,y=67,width=3, height=535)

Edit_Employee_Frame = Frame(tab6,bg=_from_rgb((0,200,244)))
Edit_Employee_Frame.place(x=780,y=70,height=530,width=500)


Delete_Employee_logo=ImageTk.PhotoImage(file="trash-bin.png")
Delete_Employee_label=Label(Edit_Employee_Frame,image=Delete_Customer_logo,bg=_from_rgb((33, 40, 62)))
Delete_Employee_label.bind("<Button>", removeemployee)
Delete_Employee_label.place(x=0,y=0)

Save_Employee_logo=ImageTk.PhotoImage(file="edit.png")
Save_Employee_label=Label(Edit_Employee_Frame,image=Save_Employee_logo,bg=_from_rgb((33, 40, 62)))
Save_Employee_label.bind("<Button>", update_employeedata)
Save_Employee_label.place(x=463,y=0)

Customer_Details_Label=Label(Edit_Employee_Frame,text="Employee Details",bg=_from_rgb((33, 40, 62)),height="0",fg=_from_rgb((0,200,244)),font = "Verdana 15 bold").place(x=150,y=0)

tab6l1=Label(Edit_Employee_Frame,text="Employee Code",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=120,y=50)
tab6l2=Label(Edit_Employee_Frame,text="Employee Name",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=114,y=90)
tab6l3=Label(Edit_Employee_Frame,text="CNIC Number",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=132,y=130)
tab6l4=Label(Edit_Employee_Frame,text="Designation",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Tahoma 14 normal").place(x=150,y=170)

tab6l5=Label(Edit_Employee_Frame,text="Date of Birth",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=138,y=210)
tab6l6=Label(Edit_Employee_Frame,text="Gender",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=185,y=250)
tab6l7=Label(Edit_Employee_Frame,text="Phone Number",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=124,y=290)
tab6l8=Label(Edit_Employee_Frame,text="Email Address",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Tahoma 14 normal").place(x=125,y=330)

tab6l9=Label(Edit_Employee_Frame,text="Date of Joining",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=120,y=370)
tab6l10=Label(Edit_Employee_Frame,text="Address",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=178,y=410)
tab6l11=Label(Edit_Employee_Frame,text="Extra Details",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=142,y=450)

tab6line_style = ttk.Style()
tab6line_style.configure("tab6.TSeparator", background=_from_rgb((33, 40, 62)))

tab6t1=Entry(Edit_Employee_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e1)
tab6t1.place(height=24,x=260,y=50)
separator = ttk.Separator(Edit_Employee_Frame,orient="horizontal",style="tab6.TSeparator")
separator.place(x=260,y=71,width=182)

tab6t2=Entry(Edit_Employee_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e2)
tab6t2.place(height=24,x=260,y=90)
separator = ttk.Separator(Edit_Employee_Frame,orient="horizontal",style="tab6.TSeparator")
separator.place(x=260,y=111,width=182)

tab6t3=Entry(Edit_Employee_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e3)
tab6t3.place(height=24,x=260,y=130)
separator = ttk.Separator(Edit_Employee_Frame,orient="horizontal",style="tab6.TSeparator")
separator.place(x=260,y=151,width=182)

tab6t4=Entry(Edit_Employee_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e4)
tab6t4.place(height=24,x=260,y=170)
separator = ttk.Separator(Edit_Employee_Frame,orient="horizontal",style="tab6.TSeparator")
separator.place(x=260,y=191,width=182)

tab6t5=Entry(Edit_Employee_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e5)
tab6t5.place(height=24,x=260,y=210)
separator = ttk.Separator(Edit_Employee_Frame,orient="horizontal",style="tab6.TSeparator")
separator.place(x=260,y=231,width=182)

tab6t6=Entry(Edit_Employee_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e6)
tab6t6.place(height=24,x=260,y=250)
separator = ttk.Separator(Edit_Employee_Frame,orient="horizontal",style="tab6.TSeparator")
separator.place(x=260,y=271,width=182)

tab6t7=Entry(Edit_Employee_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e7)
tab6t7.place(height=24,x=260,y=290)
separator = ttk.Separator(Edit_Employee_Frame,orient="horizontal",style="tab6.TSeparator")
separator.place(x=260,y=311,width=182)

tab6t8=Entry(Edit_Employee_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e8)
tab6t8.place(height=24,x=260,y=330)
separator = ttk.Separator(Edit_Employee_Frame,orient="horizontal",style="tab6.TSeparator")
separator.place(x=260,y=351,width=182)

tab6t9=Entry(Edit_Employee_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e9)
tab6t9.place(height=24,x=260,y=370)
separator = ttk.Separator(Edit_Employee_Frame,orient="horizontal",style="tab6.TSeparator")
separator.place(x=260,y=391,width=182)

tab6t10=Entry(Edit_Employee_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e10)
tab6t10.place(height=24,x=260,y=410)
separator = ttk.Separator(Edit_Employee_Frame,orient="horizontal",style="tab6.TSeparator")
separator.place(x=260,y=431,width=182)

tab6t11=Entry(Edit_Employee_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=e11)
tab6t11.place(height=24,x=260,y=450)
separator = ttk.Separator(Edit_Employee_Frame,orient="horizontal",style="tab6.TSeparator")
separator.place(x=260,y=471,width=182)
#-----------------------------------------------------------------------tab8 View Car------------------------------------------------------------------------------
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
v7 = StringVar()
v8 = StringVar()
v9 = StringVar()
v10 = StringVar()
v11 = StringVar()
v12 = StringVar()

style8 = ttk.Style()
style8.theme_use("clam")
style8.layout('TNotebook.Tab', [])
style8.configure("Treeview.Heading", background=_from_rgb((33, 40, 62)),fieldbackground=_from_rgb((33, 40, 62)),foreground=_from_rgb((0,200,244)))


View_Car_Frame = Frame(tab8,bg=_from_rgb((0,200,244)))
View_Car_Frame.place(x=0,y=2,height=65,width=1362)

View_Car_logo=ImageTk.PhotoImage(file="two-cars.png")
View_Car_image=Label(View_Car_Frame,compound='left',image=View_Car_logo,bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),text="   View Cars",font = "Verdana 20 bold")
View_Car_image.place(x=530,y=-1)

Cardata = ttk.Treeview(tab8,columns=(1,2,3,4,5,6,7,8,9,10,11,12),show="headings",height="26")
Cardata.bind('<Double 1>',getrow_Cardb)
Cardata.place(x=0,y=70,width="680")
Cardata.heading(1,text="Car Code")
Cardata.heading(2,text="Car Name")
Cardata.heading(3,text="Car Model")
Cardata.heading(4,text="Registration Number")
Cardata.heading(5,text="Date of Entry")
Cardata.heading(6,text="Time Of Entry")
Cardata.heading(7,text="Owner Name")
Cardata.heading(8,text="Owner CNIC Number")
Cardata.heading(9,text="Car Color")
Cardata.heading(10,text="Extra Details")
Cardata.heading(11,text="Exiting Time")
Cardata.heading(12,text="Exiting Date")
Cardata.column(1, anchor=tkinter.N,minwidth=0, width=91, stretch=NO)
Cardata.column(2, anchor=tkinter.N,minwidth=0, width=86, stretch=NO)
Cardata.column(3, anchor=tkinter.N,minwidth=0, width=80, stretch=NO)
Cardata.column(4, anchor=tkinter.N,minwidth=0, width=120, stretch=NO)
Cardata.column(5, anchor=tkinter.N,minwidth=0, width=87, stretch=NO)
Cardata.column(6, anchor=tkinter.N,minwidth=0, width=112, stretch=NO)
Cardata.column(7, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
Cardata.column(8, anchor=tkinter.N,minwidth=0, width=141, stretch=NO)
Cardata.column(9, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
Cardata.column(10, anchor=tkinter.N,minwidth=0, width=141, stretch=NO)
Cardata.column(11, anchor=tkinter.N,minwidth=0, width=80, stretch=NO)
Cardata.column(12, anchor=tkinter.N,minwidth=0, width=130, stretch=NO)
fetch_car()

tab6line_style = ttk.Style()
tab6line_style.configure("tab6.TSeparator", background=_from_rgb((33, 40, 62)))
separator = ttk.Separator(tab8,orient='vertical',style="tab6.TSeparator")
separator.place(x=730,y=67,width=3, height=535)

separator4 = ttk.Separator(tab8,orient='vertical',style="tab2.TSeparator")
separator4.place(x=677,y=67,width=3, height=535)

Edit_Car_Frame = Frame(tab8,bg=_from_rgb((0,200,244)))
Edit_Car_Frame.place(x=780,y=70,height=530,width=500)


Delete_Car_logo=ImageTk.PhotoImage(file="trash-bin.png")
Delete_Car_label=Label(Edit_Car_Frame,image=Delete_Customer_logo,bg=_from_rgb((33, 40, 62)))
Delete_Car_label.bind("<Button>", removecar)
Delete_Car_label.place(x=0,y=0)

Save_Car_logo=ImageTk.PhotoImage(file="edit.png")
Save_Car_label=Label(Edit_Car_Frame,image=Save_Car_logo,bg=_from_rgb((33, 40, 62)))
Save_Car_label.bind("<Button>", update_cardata)
Save_Car_label.place(x=463,y=0)

tab8line_style = ttk.Style()
tab8line_style.configure("tab8.TSeparator", background=_from_rgb((33, 40, 62)))

Customer_Car_Label=Label(Edit_Car_Frame,text="Car Details",bg=_from_rgb((33, 40, 62)),height="0",fg=_from_rgb((0,200,244)),font = "Verdana 15 bold").place(x=180,y=0)

tab8l1=Label(Edit_Car_Frame,text="Car Number",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=120,y=50)
tab8l2=Label(Edit_Car_Frame,text="Car Name",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=138,y=90)
tab8l3=Label(Edit_Car_Frame,text="Car Model",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=135,y=130)
tab8l4=Label(Edit_Car_Frame,text="Registration Number",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Tahoma 14 normal").place(x=50,y=170)

tab8l5=Label(Edit_Car_Frame,text="Owner Name",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=110,y=210)
tab8l6=Label(Edit_Car_Frame,text="Owner CNIC Number",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=40,y=250)
tab8l7=Label(Edit_Car_Frame,text="Car Color",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=137,y=290)
tab8l8=Label(Edit_Car_Frame,text="Extra Details",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Tahoma 14 normal").place(x=110,y=330)

tab8l9=Label(Edit_Car_Frame,text="Car Entry",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Tahoma 14 normal").place(x=255,y=370)
tab8l10=Label(Edit_Car_Frame,text="Car Exit",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Tahoma 14 normal").place(x=370,y=370)

tab8t1=Entry(Edit_Car_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=v1)
tab8t1.place(height=24,x=260,y=50)
separator = ttk.Separator(Edit_Car_Frame,orient="horizontal",style="tab8.TSeparator")
separator.place(x=260,y=72,width=182)

tab8t2=Entry(Edit_Car_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=v2)
tab8t2.place(height=24,x=260,y=90)
separator = ttk.Separator(Edit_Car_Frame,orient="horizontal",style="tab8.TSeparator")
separator.place(x=260,y=112,width=182)

tab8t3=Entry(Edit_Car_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=v3)
tab8t3.place(height=24,x=260,y=130)
separator = ttk.Separator(Edit_Car_Frame,orient="horizontal",style="tab8.TSeparator")
separator.place(x=260,y=152,width=182)

tab8t4=Entry(Edit_Car_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=v4)
tab8t4.place(height=24,x=260,y=170)
separator = ttk.Separator(Edit_Car_Frame,orient="horizontal",style="tab8.TSeparator")
separator.place(x=260,y=192,width=182)

tab8t5=Entry(Edit_Car_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=v5)
tab8t5.place(height=24,x=260,y=210)
separator = ttk.Separator(Edit_Car_Frame,orient="horizontal",style="tab8.TSeparator")
separator.place(x=260,y=232,width=182)

tab8t6=Entry(Edit_Car_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=v6)
tab8t6.place(height=24,x=260,y=250)
separator = ttk.Separator(Edit_Car_Frame,orient="horizontal",style="tab8.TSeparator")
separator.place(x=260,y=272,width=182)

tab8t7=Entry(Edit_Car_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=v7)
tab8t7.place(height=24,x=260,y=290)
separator = ttk.Separator(Edit_Car_Frame,orient="horizontal",style="tab8.TSeparator")
separator.place(x=260,y=312,width=182)

tab8t8=Entry(Edit_Car_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=v8)
tab8t8.place(height=24,x=260,y=330)
separator = ttk.Separator(Edit_Car_Frame,orient="horizontal",style="tab8.TSeparator")
separator.place(x=260,y=352,width=182)

tab8l11=Label(Edit_Car_Frame,text="Time:",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Tahoma 14 normal").place(x=190,y=395)
tab8l12=Label(Edit_Car_Frame,text="Date:",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Tahoma 14 normal").place(x=190,y=445)

tab8t9=Entry(Edit_Car_Frame,bg=_from_rgb((0,200,244)),width=6, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=v9)
tab8t9.place(height=24,x=255,y=400)
separator = ttk.Separator(Edit_Car_Frame,orient="horizontal",style="tab8.TSeparator")
separator.place(x=255,y=421,width=85)

tab8t10=Entry(Edit_Car_Frame,bg=_from_rgb((0,200,244)),width=6, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=v10)
tab8t10.place(height=24,x=365,y=400)
separator = ttk.Separator(Edit_Car_Frame,orient="horizontal",style="tab8.TSeparator")
separator.place(x=365,y=421,width=85)

tab8t11=Entry(Edit_Car_Frame,bg=_from_rgb((0,200,244)),width=6, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=v11)
tab8t11.place(height=24,x=255,y=450)
separator = ttk.Separator(Edit_Car_Frame,orient="horizontal",style="tab8.TSeparator")
separator.place(x=255,y=471,width=85)

tab8t12=Entry(Edit_Car_Frame,bg=_from_rgb((0,200,244)),width=6, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold",textvariable=v12)
tab8t12.place(height=24,x=365,y=450)
separator = ttk.Separator(Edit_Car_Frame,orient="horizontal",style="tab8.TSeparator")
separator.place(x=365,y=471,width=85)
#tab8t2=Entry(Edit_Car_Frame,bg=_from_rgb((0,200,244)),width=13, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")
#tab8t2.place(height=24,x=260,y=90)
#separator = ttk.Separator(Edit_Car_Frame,orient="horizontal",style="tab8.TSeparator")
#separator.place(x=260,y=112,width=182)
#---------------------------------------------------tab10 Car Exiting From Garage---------------------------------------------------------------------------------------------------------------
View_CarExit_Frame = Frame(tab10,bg=_from_rgb((0,200,244)))
View_CarExit_Frame.place(x=0,y=2,height=65,width=1362)

View_CarExit_logo=ImageTk.PhotoImage(file="Shopping-Cart.png")
View_CarExit_image=Label(View_CarExit_Frame,compound='left',image=View_Stock_logo,bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),text="   View Stock",font = "Verdana 20 bold")
View_CarExit_image.place(x=50,y=-1)

View_CarExit_logo1=ImageTk.PhotoImage(file="order.png")
View_CarExit_image1=Label(View_CarExit_Frame,compound='left',image=View_CarExit_logo1,bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),text="   Add To Cart",font = "Verdana 20 bold")
View_CarExit_image1.place(x=420,y=-1)

CarExitdata = ttk.Treeview(tab10,columns=(1,2,3),show="headings",height="26")
#Stockdata.bind('<Double 1>',getrow_Stockdb)
CarExitdata.place(x=0,y=70,width="380")
CarExitdata.heading(1,text="Stock")
CarExitdata.heading(2,text="Quantity")
CarExitdata.heading(3,text="Buying Price")
CarExitdata.column(1, anchor=tkinter.N,minwidth=0, width=126, stretch=NO)
CarExitdata.column(2, anchor=tkinter.N,minwidth=0, width=126, stretch=NO)
CarExitdata.column(3, anchor=tkinter.N,minwidth=0, width=126, stretch=NO)
fetch_car_exit()
tab10line_style = ttk.Style()
tab10line_style.configure("tab10.TSeparator", background=_from_rgb((33, 40, 62)))
separator = ttk.Separator(tab10,orient='vertical',style="tab10.TSeparator")
separator.place(x=730,y=67,width=3, height=535)

separator10 = ttk.Separator(tab10,orient='vertical',style="tab10.TSeparator")
separator10.place(x=380,y=67,width=3, height=535)

Cartdata = ttk.Treeview(tab10,columns=(1,2,3,4,5),show="headings",height="26")
#Stockdata.bind('<Double 1>',getrow_Stockdb)
Cartdata.place(x=384,y=70,width="345")
Cartdata.heading(1,text="Car Code")
Cartdata.heading(2,text="Sr_No")
Cartdata.heading(3,text="Name")
Cartdata.heading(4,text="Price")
Cartdata.heading(5,text="Labor Charges")
Cartdata.column(1, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)
Cartdata.column(2, anchor=tkinter.N,minwidth=0, width=50, stretch=NO)
Cartdata.column(3, anchor=tkinter.N,minwidth=0, width=50, stretch=NO)
Cartdata.column(4, anchor=tkinter.N,minwidth=0, width=50, stretch=NO)
Cartdata.column(5, anchor=tkinter.N,minwidth=0, width=100, stretch=NO)

Exit_Car_Frame = Frame(tab10,bg=_from_rgb((0,200,244)))
Exit_Car_Frame.place(x=780,y=70,height=530,width=500)

Exit_Car_Label=Label(Exit_Car_Frame,text="Car Exit Details",bg=_from_rgb((33, 40, 62)),height="0",fg=_from_rgb((0,200,244)),font = "Verdana 15 bold").place(x=155,y=0)

tab10l1=Label(Exit_Car_Frame,text="Exiting Time",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=135,y=50)
tab10l2=Label(Exit_Car_Frame,text="Exiting Date",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=138,y=90)
tab10l3=Label(Exit_Car_Frame,text="Car Code",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=165,y=130)#170
tab10l4=Label(Exit_Car_Frame,text="Name",bg=_from_rgb((0,200,244)),fg=_from_rgb((33, 40, 62)),font = "Tahoma 14 normal").place(x=170,y=210)

tab10l5=Label(Exit_Car_Frame,text="Price",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=178,y=240)
tab10l6=Label(Exit_Car_Frame,text="Labour Charges",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 normal").place(x=108,y=330)

tab10l7=Label(Exit_Car_Frame,text="Auto Entered",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 12 normal").place(x=260,y=50)
tab10l8=Label(Exit_Car_Frame,text="Auto Entered",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 12 normal").place(x=260,y=90)

tab10l9=Label(Exit_Car_Frame,text="Parts Changed",fg=_from_rgb((33, 40, 62)),bg=_from_rgb((0,200,244)),font = "Tahoma 14 bold").place(x=180,y=170)


tab10t1=Entry(Exit_Car_Frame,bg=_from_rgb((0,200,244)),width=7, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")#,textvariable=v3)
tab10t1.place(height=24,x=260,y=130)
separator = ttk.Separator(Exit_Car_Frame,orient="horizontal",style="tab8.TSeparator")
separator.place(x=260,y=152,width=100)

tab10t2=Entry(Exit_Car_Frame,bg=_from_rgb((0,200,244)),width=7, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")#,textvariable=v5)
tab10t2.place(height=24,x=230,y=210)
separator = ttk.Separator(Exit_Car_Frame,orient="horizontal",style="tab8.TSeparator")
separator.place(x=230,y=232,width=100)


tab10t3=Entry(Exit_Car_Frame,bg=_from_rgb((0,200,244)),width=7, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")#,textvariable=v6)
tab10t3.place(height=24,x=230,y=250)
separator = ttk.Separator(Exit_Car_Frame,orient="horizontal",style="tab8.TSeparator")
separator.place(x=230,y=272,width=100)

tab10t4=Entry(Exit_Car_Frame,bg=_from_rgb((0,200,244)),width=7, highlightthickness=0,bd=0,justify=CENTER,fg=_from_rgb((33, 40, 62)),font = "Verdana 15 bold")#,textvariable=v6)
tab10t4.place(height=24,x=255,y=330)
separator = ttk.Separator(Exit_Car_Frame,orient="horizontal",style="tab8.TSeparator")
separator.place(x=255,y=351,width=100)

tab10b1=Button(Exit_Car_Frame,bg=_from_rgb((33, 40, 62)),text="SAVE",width=7,justify=CENTER,fg=_from_rgb((0,200,244)),font = "Verdana 12 bold",command=exitcar)
tab10b1.place(height=24,x=210,y=290)


tab10b2=Button(Exit_Car_Frame,bg=_from_rgb((33, 40, 62)),text="SAVE",width=7,justify=CENTER,fg=_from_rgb((0,200,244)),font = "Verdana 12 bold",command=labourcharges)
tab10b2.place(height=24,x=210,y=370)

tab10b3=Button(Exit_Car_Frame,bg=_from_rgb((33, 40, 62)),text="Save Receipt",width=13,justify=CENTER,fg=_from_rgb((0,200,244)),font = "Verdana 12 bold",command=createreceipt)
tab10b3.place(height=24,x=100,y=420)


tab10b4=Button(Exit_Car_Frame,bg=_from_rgb((33, 40, 62)),text="CLEAR",width=13,justify=CENTER,fg=_from_rgb((0,200,244)),font = "Verdana 12 bold",command=reset_allcarexit)
tab10b4.place(height=24,x=255,y=420)
#-------------------------------------------------tab11 About-----------------------------------------------------------------------------------------------------------------------------------

About_logo=ImageTk.PhotoImage(file="About.png")
About_label=Label(tab11,image=About_logo)
About_label.place(x=0,y=0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# window in mainloop:
root.mainloop()













