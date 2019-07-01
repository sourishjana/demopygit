import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="Sourish",
    passwd="sourish@123",
    database="testdb"#now this statement creates tables in the testbd in mysql
)
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM students WHERE age=45")
myresult=mycursor.fetchall()

for row in myresult:
    print(row)

print("------------printing the students whose name starts by some letter-------------")

mycursor.execute("SELECT * FROM students WHERE name LIKE 'am%'")
#'am%' means the name starting with 'am' again '%an%' means any name having 'an' at the middle
#'%da' means the name ending with 'da'
myresult=mycursor.fetchall()

for row in myresult:
    print(row)

mycursor.execute("SELECT * FROM students WHERE name LIKE '%rl'")
#'am%' means the name starting with 'am' again '%an%' means any name having 'an' at the middle
#'%da' means the name ending with 'da'
myresult=mycursor.fetchall()

for row in myresult:
    print(row)

print("basically sql injection which is a common hacking technique so we should use another technique")

sql="SELECT * FROM students WHERE name=%s"
mycursor.execute(sql , ("carl", ))

myresult=mycursor.fetchall()

for row in myresult:
    print(row)