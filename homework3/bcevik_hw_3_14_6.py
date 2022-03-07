"""
Battal Cevik
Class: CS 521 - Semester
Date: 03/06/2022
Homework 3 Problem 3.14.6
Create a text file containing student records by line and each record is of the format:
Name of Student
Student ID
GPA
"""
import sys

# Create a text file containing student records
file1 = open('bcevik_hw_3_14_6.txt', 'w')

# Entering student data
file1.write("Tyrion Lannister, 1, 3.7")
file1.write("\nDaenerys Targaryen, 52, 2.8")
file1.write("\nJon Snow, 13, 3.9")
file1.write("\nSansa Stark, 24, 3.4")
file1.close()

# Read the file
try:
    file1 = open('bcevik_hw_3_14_6.txt', 'r')
except FileNotFoundError as e:
    sys.exit("Error: This file does not exist: ", e)
except IOError as e:
    sys.exit("Error: This file does n ot found: ", e)

# Creating a list to assign my data into the list
file1_array = []

# Creating a for loop to read each line, split it and put in array
for each_line in file1:
    file1_array.append(each_line.strip().split(', '))
# Close to file
file1.close()

# Storing records in a list
print(file1_array)

