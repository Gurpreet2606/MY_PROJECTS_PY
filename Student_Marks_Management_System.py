print("\n======STUDENT MARKS MANAGEMENT SYSTEM======\n")
name = input("Enter the student name: ")
python_marks = float(input("Enter the marks of python:"))
Java_marks = float(input("Enter the marks of java:"))
Php_marks = float(input("Enter the marks of php:"))
total_marks = python_marks + Java_marks + Php_marks
average_marks = total_marks / 3
print("\n======STUDENT RESULT======")
print(f"student name: {name}")
print(f"total marks: {total_marks}")
print(f"average marks: {average_marks}")

if average_marks >= 90:
    print("Grade: A")
elif average_marks >= 75:
    print("Grade: B")
elif average_marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")


# Student Marks Management System with pass/fail status
# python_marks = float(input("python marks:"))
# Java_marks = float(input("java marks:"))
# Php_marks = float(input("php marks:"))
if python_marks >= 35 and Java_marks >= 35 and Php_marks >= 35:
    print("pass")
else:
    print("fail")
