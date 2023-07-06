from datetime import date
import numpy as np
import face_recognition
import cv2
import mysql.connector
import os
from tkinter import messagebox
import tkinter as tk


root = tk.Tk()
root.withdraw()


def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

try:
    database = 'data'
    db = mysql.connector.connect(host="localhost", user="root", password="", db="temp")
    cursor = db.cursor()
    savequery = "SELECT * FROM "+database
    print(savequery)
    try:
        cursor.execute(savequery)
        myresult = cursor.fetchone()
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
except mysql.connector.Error as e:
    messagebox.showinfo("Error", e)
db.close()

Classroom=myresult[0]
Teacher_Name=myresult[1]
Folder_Name=myresult[2]
Subject=myresult[3]
today = date.today()
d1 = today.strftime("%Y/%m/%d")
Attendance="Present"
path = "C:/Roadster/Major/Attendance/"+Classroom+"/"

images = []
classNames = []
myList = os.listdir(path)
#print(myList)

for cl in myList:
    curImag = cv2.imread(f'{path}/{cl}')
    images.append(curImag)
    imge=os.path.splitext(cl)[0]
    imge1= imge.split("-")[0]
    classNames.append(imge1)
#print(classNames)

def findencondings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
encodeListKnown = findencondings(images)
#print('Encoding Complete')

def markAttendance(Roll_No,Classroom,Subject,Teacher_Name,Attendance):
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", db="classroom")
        cursor = db.cursor()
        savequery = "UPDATE " + Classroom + " SET Subject='" + Subject + "'" + ",Teacher='" + Teacher_Name + "'" + ",Attendance='" + Attendance + "'" + ",Date='" + d1 + "'" + " WHERE Roll_No=" + Roll_No
        #print(savequery)
        try:
            cursor.execute(savequery)
            db.commit()
            numrows = int(cursor.rowcount)
            #print(numrows)
            if numrows == 1:
                messagebox.showinfo("Information", "Attendance Marked Successfully!")

            else:
                messagebox.showerror("Error", "Attendance Already Marked")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error", e)
    except mysql.connector.Error as e:
        messagebox.showinfo("Error", e)
    db.close()


if len(images) != 0:
    cap = cv2.VideoCapture(1)
    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            #print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                Roll_No = classNames[matchIndex].upper()
                #print(Roll_No)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, Roll_No, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markAttendance(Roll_No,Classroom,Subject,Teacher_Name,Attendance)
        cv2.imshow('Webcam',img)
        key = cv2.waitKey(200)
        #print(key)
        if key in [ord('a'), 1048673]:
            print('')
        elif key in [27, 1048603]:
            try:
                db = mysql.connector.connect(host="localhost", user="root", password="", db="temp")
                cursor = db.cursor()
                savequery = "truncate table data"
                #print(savequery)
                try:
                    cursor.execute(savequery)
                    messagebox.showinfo("Information", "Do you want to exit?")
                    cv2.destroyAllWindows()
                    cap.release()
                except mysql.connector.Error as e:
                    messagebox.showinfo("Error", e)
            except mysql.connector.Error as e:
                messagebox.showinfo("Error", e)
            db.close()
            break
else:
    messagebox.showerror("error","No Records To Mark Attendance You Are Redirected To The Dashboard")
    root.destroy()
    cv2.destroyAllWindows()


































