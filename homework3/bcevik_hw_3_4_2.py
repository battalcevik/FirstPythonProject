"""
Battal Cevik
Class: CS 521 - Semester
Date: 03/06/2022
Homework 3 Problem 3.4.2
Set a constant with an odd length string.
Confirm in code that the string is of an odd length. Otherwise, print a relevant message for
the user and end the program.
"""
my_text = "A man a plan a canal Panama"

if len(my_text) % 2 == 0:
    print("The string length is even, quitting program")
else:
    print('My ' + str(len(my_text)) + '-character string is: "' + my_text + '"')
    print('The middle character is: "' + my_text[len(my_text) // 2] + '"')
    print('The first half of the string is: "' + my_text[:len(my_text) // 2] + '"')
    print('The second half of the string is: "' + my_text[(len(my_text) // 2)+1:] + '"')

