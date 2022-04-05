"""
Battal Cevik
Class: CS 521 - Semester
Date: 03/06/2022
Homework 3 Problem 3.4.4
Write a program that prompts the user to enter a three‐digit whole number such that the
digits are in ascending order and without duplicates.
The program loops and re‐prompts the user until a correct value is entered. Make sure to
check whether the user entered the correct data type.
"""

while True:
    number = input('Please enter a 3-digit integer: ')

    num_length = len(number)
    set_length = len(set(list(number)))
    if num_length != set_length:
        print("Your number contains duplication.")
        continue
    if num_length != 3:
        print("You did not enter a 3-digit number.")
        continue
    if not number.isdigit():
        print("This is not an integer. Please re-enter.")
        continue
    if not ((number[1] < number[2]) and (number[0] < number[1])):
        print("The digits are not in ascending order.")
        continue
    print("Number Accepted!")
    break
