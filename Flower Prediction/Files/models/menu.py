import sqlite3
from datetime import *
from tokenize import Number

def addmoney(number,card,cvv,date,cardname,amount):
    try:
        connect = sqlite3.connect("storage.db")
        cursor = connect.cursor()
        print(number,card,cvv,date,cardname,amount)
        cursor.execute("CREATE TABLE IF NOT EXISTS rechargedata (id INTEGER NOT NULL PRIMARY KEY, MobNo NUMBER, CardNo NUMBER, CVV NUMBER, ExpiryDate TEXT, CardName TEXT, Amount NUMBER, TransDate TEXT, TransTime TEXT, ServiceP TEXT, Plan TEXT)")
        cursor.execute("INSERT INTO rechargedata (MobNo, CardNo, CVV, ExpiryDate, CardName, Amount) VALUES (?,?,?,?,?,?)",(number,card,cvv,date,cardname,amount))
        connect.commit()
        connect.close()
        msg = "success"
        return msg

    except Exception as Error:
        print(Error)
        msg = "failed"
        return msg

def recharge(number,service,plan,amount):
    today = date.today()
    now = datetime.now()
    T_time = now.strftime("%H:%M:%S")
    T_date = today.strftime("%d/%m/%Y")
    try:
        connect = sqlite3.connect("storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT Amount FROM rechargedata where MobNo=?",(number,))
        oldAmount = cursor.fetchone()
        newAmount = int(oldAmount[0]) - int(amount)
        cursor.execute("UPDATE rechargedata SET Amount = ?, TransDate = ?, TransTime = ?, ServiceP = ?, Plan = ?  WHERE MobNo = ?",(newAmount,T_date,T_time,service,plan,number))
        connect.commit()
        connect.close()
        msg = "success"
        return msg
    except Exception as Error:
        print(Error)
        msg = "failed"
        return msg


def Balance(number):
    try:
        connect = sqlite3.connect("storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * from rechargedata where MobNo=?",(number,))
        details = cursor.fetchone()
        connect.commit()
        connect.close()
        msg = "success"
        return details

    except Exception as Error:
        print(Error)
        msg = "failed"
        return msg
