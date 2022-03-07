"""
Battal Cevik
Class: CS 521 - Semester
Date: 03/06/2022
Homework 3 Problem 3.2.1
Write a Python program that counts the number of odd numbers, even numbers, squares of
an integer and cubes of an integer from 2 to 130 (inclusive). For example, 9 is both odd and
a square, 8 is even and a cube.
"""
# Create a constant variable
FIRST_NUMBER = 2
LAST_NUMBER = 130
num_range = range(FIRST_NUMBER, LAST_NUMBER + 1)
count_odd = []
count_even = []
count_square = []
count_cube = []


# Create a function to find squares in the range of number
def square_numbers(number):
    square_count = int(number ** (1 / 2))
    return round(square_count) ** 2 == number


# Create a function to find cubes in the range of number
def cube_numbers(number):
    cube_count = number ** (1 / 3)
    return round(cube_count) ** 3 == number


# Print statement for the title of output
print("Checking numbers from ", FIRST_NUMBER, "to", LAST_NUMBER)


# Creating for loop to find numbers of even, odd, square, cube
for num in num_range:
    if num % 2 == 0:
        count_even.append(num)
    if num % 2 == 1:
        count_odd.append(num)
    if square_numbers(num):
        count_square.append(num)
    if cube_numbers(num):
        count_cube.append(num)

# Print Statement for output
print("Even(", len(count_even), "):", count_even)
print("Odd(", len(count_odd), "):", count_odd)
print("Square(", len(count_square), "):", count_square)
print("Cube(", len(count_cube), "):", count_cube)
