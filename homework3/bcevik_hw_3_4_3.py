"""
Battal Cevik
Class: CS 521 - Semester
Date: 03/06/2022
Homework 3 Problem 3.4.3
Write a program that prompts the user for a sentence and calculates the number of
uppercase letters, lowercase letters, digits, and punctuation. Output the results neatly
formatted, centered and labeled in columns.
"""
# importing the string module
import string
# Assigning all the punctuations to a variable x_string
x_string = string.punctuation

# Prompt a sentence from user
user_sentence = input("Please enter a sentence: ")
# Convert it to list
x_list = list(user_sentence)
# Create string variables to print output
str_upper = "# Upper"
str_lower = "# Lower"
str_digit = "# Digits"
str_punc = "# Punct."
str_hyphen = "--------"

# Assigning counts from loop
upper_count = 0
lower_count = 0
digits_count = 0
punc_count = 0

# For loop to count variables in list
for char in x_list:
    if char.isupper():
        upper_count = upper_count + 1
    if char.islower():
        lower_count = lower_count + 1
    if char.isdigit():
        digits_count = digits_count + 1
    if char in x_string:
        punc_count = punc_count + 1

# Print Statement to create an output
print(str_upper.center(8, ' '), str_lower.center(8, ' '), str_digit.center(8, ' '), str_punc.center(8, ' '))
print(str_hyphen.center(8), str_hyphen.center(8), str_hyphen.center(8), str_hyphen.center(8))
print(str(upper_count).center(8), str(lower_count).center(8), str(digits_count).center(8), str(punc_count).center(8))

