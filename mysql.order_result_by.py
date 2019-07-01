import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="Sourish",
    passwd="sourish@123",
    database="testdb",
)
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM students ORDER BY name")
#instead of name we can use age to sort by age
myresult=mycursor.fetchall()
for i in myresult:
    print(i)

print("-------------decending order--------------")
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM students ORDER BY age DESC")
#instead of name we can use age to sort by age
myresult=mycursor.fetchall()
for i in myresult:
    print(i)