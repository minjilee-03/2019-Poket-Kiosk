import mysql.connector

mydb = mysql.connector.connect(
    user="root",
    password="mirim",
    host="127.0.0.1",
    port=3306,
    database="poketkiosk"
)

mycursor = mydb.cursor()

sql = "UPDATE user SET codename = %s WHERE id = %s"
val = ("123456", "1")

mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record was inserted")
