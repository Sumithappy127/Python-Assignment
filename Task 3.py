import mysql.connector

#Database connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="s1u9m9i6t"
)

mycursor = mydb.cursor()
mycursor.execute("drop database my__school")

#created database 
mycursor.execute("CREATE DATABASE my__school")

#use database
mycursor.execute("USE my__school")

#create table
mycursor.execute("""
CREATE TABLE students (
  student_id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  age INT,
  grade DECIMAL(5,2)
)
""")

#Insert data into tables
mycursor.execute("""insert into students(first_name,last_name,age,grade) 
                 values("Alice", "Smith", 18, 95.5),("sumit","thakur",19,81.2)""")    #Added 1 more data to table students
mydb.commit() 

#update data
mycursor.execute("""update students set grade = 97.0 where first_name="Alice" """)
mydb.commit()  

#Delete data
mycursor.execute("""delete from students where last_name="smith" """)
mydb.commit() 

#To see table data
mycursor.execute("select * from students")
myresult = mycursor.fetchall()

print("Student Records:")
for row in myresult:
    print(f"ID: {row[0]}  Name: {row[1]} {row[2]}  Age: {row[3]}  Grade: {row[4]}")

mycursor.close()
mydb.close()