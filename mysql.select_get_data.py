import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="Sourish",
    passwd="sourish@123",
    database="testdb"#now this statement creates tables in the testbd in mysql
)
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM students")
myresult=mycursor.fetchall()#this methoD actually fetch each and every data from the above
#above written lines
for row in myresult:
    print(row)


print("-----------getting a particular coloumn------------")


mycursor.execute("SELECT age FROM students")
myresult=mycursor.fetchall()#this methoD actually fetch each and every data from the above
#above written lines
for row in myresult:
    print(row)


print("------------getting a particular row--------------")
mycursor.execute("SELECT * FROM students WHERE age=45")#instead of * we can give age or name
myresult=mycursor.fetchone()#this methoD actually fetch only one data form thousands of columns
#from the above written lines
for row in myresult:
    print(row)