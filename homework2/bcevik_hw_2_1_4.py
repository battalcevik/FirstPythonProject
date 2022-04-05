"""
Battal Cevik
Class: CS 521 - Semester
Date: 02/21/2022
Homework 2 Problem 1.4
1.4: Write a three-line program that (1) prompts for a number,(2) converts the input to an integer
and (3) prints the number 0 if the user input is even and the number 1 if the user input is odd.
"""
# Enter a number as a user input
enter_number = int(input("Please enter a number: "))
# Check the number if it is odd or even
reminder = "0" if enter_number % 2 == 0 else "1"
# print the output
print(f"{reminder }")
