import sqlite3

number = 8766408524
connect = sqlite3.connect("storage.db")
cursor = connect.cursor()
cursor.execute("SELECT Amount FROM rechargedata where MobNo=?",(number,))
user_info = cursor.fetchone()

connect.close()
print(user_info[0])
