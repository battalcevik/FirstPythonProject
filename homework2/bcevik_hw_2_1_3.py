"""
Battal Cevik
Class: CS 521 - Semester
Date: 02/21/2022
Homework 2 Problem 1.3
1.3: Write a Python program that asks the user to enter an integer (n) and
computes the value of n+n*n+n*n*n+n*n*n*n = ?.
The program must then print the formula, replacing the ‘n’ variables with the user input,
and the ? with the calculation results.
"""
# Enter user input as an integer
n = int(input("Please enter an integer: "))
# Assigning a formula to variable
total_cal = n + n*n + n*n*n + n*n*n*n
m = n

# print the formula and calculation results
print("Formula: ", m, "+", m, "*", m, "+", m, "*", m, "*", m, "+", m, "*", m, "*", m, "*", m, " :", total_cal)

