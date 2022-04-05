"""
Battal Cevik
Class: CS 521 - Spring Semester
Date: 03/18/2022
Homework 4 Problem 4.7.1
Given a constant list of integers in the range 1 to 10 inclusive, use list comprehension (no
explicit loops) to:
find the sum of the even integers in list L.
find the sum of the odd integers in list L.
"""

NUMBER_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_num = 1
last_num = 10
num_range = range(first_num, last_num + 1)
# using list comprehension
even_nos = [num for num in num_range if num % 2 == 0]
odd_nos = [num for num in num_range if num % 2 == 1]
even_sum = sum(even_nos)
odd_sum = sum(odd_nos)
print("Evaluating the numbers in: ", str(NUMBER_LIST).replace("[", "").replace("]", ""))
print("Even: ", even_sum)
print("Odd: ", odd_sum)

LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Evaluating the numbers in: ', )