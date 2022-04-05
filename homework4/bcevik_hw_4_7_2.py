"""
Battal Cevik
Class: CS 521 - Spring Semester
Date: 03/18/2022
Homework 4 Problem 4.7.2
Given a constant list of integers, write Python code to generate a new list with same number
of elements as the original list such that each integer in the new list is the sum of its nearest
neighbors and itself from the original list. Print both lists with descriptions.
"""

INPUT_LIST = [10, 20, 30, 40, 50]
# Create a result_list to add the first integers from Input list and its neighbor
result_list = [INPUT_LIST[0] + INPUT_LIST[1]]
n = 1
# Do while loop to add left and right neighbors to the number from Input List
while n < len(INPUT_LIST) - 1:
    result_list.append(INPUT_LIST[n - 1] + INPUT_LIST[n] + INPUT_LIST[n + 1])
    n = n + 1
# Add the last number and its neighbor to the result list
result_list.append(INPUT_LIST[n - 1] + INPUT_LIST[n])
print("Input List: ", INPUT_LIST)
print("Result List:", result_list)
