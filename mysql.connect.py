import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="Sourish",
    passwd="sourish@123"
)
print(mydb)
