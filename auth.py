import mysql.connector

connect = mysql.connector.connect(user='root', password='root', host='localhost', database='bazis')

db = connect.cursor()

db.execute("SELECT * FROM users;")

data = db.fetchall()

print(data)

connect.close