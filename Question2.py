# Problem Statement:
# Your task is to write a Python program that accomplishes the following:  
# First create a database , table and add these column ‘student_id’, ‘first_name’, ‘last_name’, 
# ‘age’, ‘grade’.  
# Connects to your MySQL database with python.  
# Inserts a new student record into the "students" table with the following details:  
# First Name: "Alice"  
# Last Name: "Smith"  
# Age: 18  
# Grade: 95.5  
# Updates the grade of the student with the first name "Alice" to 97.0.  
# Deletes the student with the last name "Smith."  
# Fetches and displays all student records from the "students" table. 

# SOLUTION:-

# To connect with mysql we have to install mysql connector :-
    # pip install mysql-connector-python

# Now, after the installation of mysql library we cn perform all the CRUD operations with following python code:-

import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

# Create cursor
mycursor = mydb.cursor()

# Create the "students" table (if it doesn't exist)
sql = """
CREATE TABLE IF NOT EXISTS students (
  student_id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  age INT,
  grade FLOAT
)
"""
mycursor.execute(sql)

# Insert a new student record
insert = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
data = ("Alice", "Smith", 18, 95.5)
mycursor.execute(insert, data)
mydb.commit()
print("Student record inserted.")

# Update the grade of the student with the first name "Alice"
update = "UPDATE students SET grade = %s WHERE first_name = %s"
update_data = (97.0, "Alice")
mycursor.execute(update, update_data)
mydb.commit()
print("Grade updated for Alice.")

# Delete the student with the last name "Smith"
delete = "DELETE FROM students WHERE last_name = %s"
delete_data = ("Smith",)
mycursor.execute(delete, delete_data)
mydb.commit()
print("Student with last name Smith deleted.")

# Display all student records
mycursor.execute("SELECT * FROM students")
students = mycursor.fetchall()
print("All student records:")
for student in students:
    print(student)

# Close cursor and connection
mycursor.close()
mydb.close()

