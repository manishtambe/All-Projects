from random import random
import sqlite3
import smtplib
from email.message import EmailMessage


def save_register(name, phone, login, passw, email):
    try:
        connect = sqlite3.connect("storage.db")
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER NOT NULL PRIMARY KEY, Name TEXT, Phone NUMBER, User TEXT, Password TEXT, Email TEXT)")
        if (name != "" and phone != "" and login != "" and passw != "" and email != ""):
            cursor.execute("INSERT INTO users(Name, Phone, User, Password, Email) VALUES(?,?,?,?,?)",(name, phone, login, passw, email,))
            connect.commit()
            connect.close()
            msg = "success"
            return msg
        else:
            msg = "failure"
            return msg
    except Exception as Error:
        print(Error)
        msg = "failure"
        return msg

def recovery_password(user_email):
    try:
        connect = sqlite3.connect("storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT Password FROM users WHERE Email =?", (user_email,))
        user_info = cursor.fetchone()
        connect.close()
        msg = EmailMessage()
        password = user_info[0]
        msg.set_content("Hello , \n Password for your account is : " + password)
        msg['subject'] = "Password recovery."
        msg['from'] = "ROADSTR SYSTEMS"
        msg['to'] = user_email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("digitalchamp2016@gmail.com", "QAZWSXEDCRFV@109")
        server.send_message(msg)
        msg = "success"
        return msg
    except Exception as Error:
        print(Error)
        msg = "failure"
        return msg


def login_user(user_name, password):
    try:
        connect = sqlite3.connect("storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT Password FROM users WHERE User =?", (user_name,))
        get_password = cursor.fetchone()
        print(get_password)
        if password == get_password[0]:
            cursor.execute("SELECT Name FROM users WHERE User =?", (user_name,))
            user = cursor.fetchone()
            connect.commit()
            msg = "success"
            connect.close()
            return msg
        else:
            msg = "failure"
            connect.close()
            return msg
    except Exception as Error:
        print(Error)
        msg = "failure"
        return msg

