import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="Sourish",
    passwd="sourish@123",
    database="testdb",
)
mycursor=mydb.cursor()
sql="DELETE FROM students WHERE name='salman'"
mycursor.execute(sql)
mydb.commit()

#for dropping a table we will bw using
#sql="DROP TABLE students"
#specify the name of table you want to delete