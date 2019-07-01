import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="Sourish",
    passwd="sourish@123",
    database="testdb"#now this statement creates tables in the testbd in mysql
)
mycursor=mydb.cursor()

sqlFormula="INSERT INTO students (name,age) VALUES(%s,%s)"
students=[("jack",29),
    ("salman",45),
    ("amanda",32),
    ("katrina",20)
          ]
mycursor.executemany(sqlFormula,students)#we have to pass sqlformula and student1 in method

mydb.commit()#withot this statement no changes will occur