import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="Sourish",
    passwd="sourish@123"
)
mycursor=mydb.cursor()#here cursor is an pointer to the databases which points the databases
#consider cursor as an object and mycursor as a object variable
mycursor.execute("CREATE DATABASE testdb")
#now execute is a method of the object cursor

#you can test the upper execute statement by running the lower written codes
#to check that any database is created or not


#mycursor.execute("SHOW DATABASES")
#for data in mycursor:
    #print(data)
