import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="Sourish",
    passwd="sourish@123",
    database="testdb"
)
mycursor=mydb.cursor()
sql="UPDATE students SET age=13 WHERE name='carl'"
mycursor.execute(sql)
mydb.commit()

print("-------------limiting data----------------")
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM students LIMIT 5")
myresult=mycursor.fetchall()

for i in myresult:
    print(i)

print("if I want to print the rows from amanda to jack")


mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM students LIMIT 5 OFFSET 4")
myresult=mycursor.fetchall()

for i in myresult:
    print(i)