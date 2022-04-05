"""
Battal Cevik
Class: CS 521 - Semester
Date: 02/21/2022
Homework 2 Problem 1.2
1.2: Prompt user for input and then print that input as a string, an integer, and a floating-point value.
What data types can be input that will print without generating any errors?
Answer this question at the end of your code by using a docscring comment.
"""
# Enter a value as user input
enter_input = input("Please enter any data values: ")
# Check the condition and print the value statement
input_str = str(enter_input)
print(enter_input)
input_int = int(enter_input)
print(input_int)
input_float = float(enter_input)
print(input_float)


# Misunderstanding of the question 2 so I comment out.
# if enter_input.strip().isdigit():
#     print("User input is number: ", enter_input)
# elif enter_input.split():
#     print("User input is String: ", enter_input)
# else:
#     print("User input is Float: ", enter_input)

"""Integer Data type will be printed without generating any error"""
