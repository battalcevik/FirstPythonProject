"""
Battal Cevik
Class: CS 521 - Spring Semester
Date: 04/1/2022
Homework 5 Problem 5.6.3
Write a python program that does the following:
Prompts the user for three numbers in one request.
Be sure to specify the “delimiter” by which a user enters those three numbers.
Divides the first number by the second number and add that result to the third number.
Prints output that shows in one line the formula applied and the result of the calculation.
"""


# Create a function to do calculations
def number_check(number1, number2, number3):
    try:
        first_number = int(number1)
        second_number = int(number2)
        third_number = int(number3)
        calculate = first_number / second_number + third_number
        print("({}/{}) + {} = {}".format(first_number, second_number, third_number, calculate))
    except Exception as e:
        print("Exception error is: ", e)
    return


# Asking user to enter 3 numbers input
x = [int(x) for x in input("Please input three numbers separated by comma: ").split(',')]
num_1 = x[0]
num_2 = x[1]
num_3 = x[2]
# Validate input by checking the user entered 3 values
if len(x) <= 3:
    # call number check function
    number_check(num_1, num_2, num_3)
else:
    print("User entered more than 3 values")



