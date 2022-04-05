"""
Battal Cevik
Class: CS 521 - Spring Semester
Date: 03/18/2022
Homework 4 Problem 4.9.3
Start with 2 constant lists. One with first names and another of last names.
First validate that both lists are the same size and if not, exit with an error message.
Use zip to create a dictionary with the keys as the last names and the values as the first names.
Print the generated dictionary with an appropriate description.
"""

FIST_NAME = ['Jane', 'John', 'Jack']
LAST_NAME = ['Doe', 'Deer', 'Black']
# Create if else condition to zip dictionary with the keys and values
if len(FIST_NAME) == len(LAST_NAME):
    my_dictionary = dict(zip(LAST_NAME, FIST_NAME))
    print('First Names: ', FIST_NAME)
    print('Last Names: ', LAST_NAME)
    print('Name dictionary: ', my_dictionary)
else:
    print("Both Lists are not the same size, exit with an error message")

