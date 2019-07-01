import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="Sourish",
    passwd="sourish@123",
    database="testdb"#now this statement creates tables in the testbd in mysql
)
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE students(name VARCHAR(45),age INT(10))")

#to show your tables use the below statements
#mycursor.execute("SHOW TABLES")
#for data in mycursor:
    #print(data)