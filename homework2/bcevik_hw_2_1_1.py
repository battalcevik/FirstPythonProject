"""
Battal Cevik
Class: CS 521 - Semester
Date: 02/21/2022
Homework 2 Problem 1.1
1.1: Write a Python program that prompts the user to enter a number.
In one calculation, take that number, add 2, multiply by 3, subtract 6, and divide by 3.
Use an IF statement to check whether the input matches the calculated value
and print the result of this check in a descriptive message.
"""
# Enter a number as a user input
user_num = int(input("Please enter a number: "))
# Do math calculation
user_cal = (((user_num+2)*3)-6)/3
# Check the statement if it is correct
if user_num == user_cal:
    print("Input matches the calculated value: ", user_cal)
else:
    print("The input does not matches the calculated value", user_cal)
