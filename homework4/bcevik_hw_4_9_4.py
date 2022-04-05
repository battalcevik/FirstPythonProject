"""
Battal Cevik
Class: CS 521 - Spring Semester
Date: 03/18/2022
Homework 4 Problem 4.9.4
Using my_dict = {a':15, 'c':18, 'b':20}, write a program to:
a. print all the keys.
b. print all the values.
c. print all the keys and values pairs.
d. print all the keys and values pairs in ascending order of key.
e. print all the keys and values pairs in ascending order of value.
"""

my_dict = {'a': 15, 'c': 18, 'b': 20}
# Print only keys from my dictionary
print("Keys: ", list(my_dict.keys()))
# Print only values from my dictionary
print("Values: ", str(list(my_dict.values())).replace("[", "").replace("]", ""))
# Print Key value pairs
print("Key value pairs: ", str(my_dict).replace("'", "").replace("{", "").replace("}", ""))
# Print Key Value pairs ordered by key
print("Key value pairs ordered by key: ",
      sorted([(key, value) for key, value in my_dict.items()], key=lambda s: s[0]))
# Print Key Value pairs ordered by key
print("Key value pairs ordered by value: ",
      sorted([(key, value) for key, value in my_dict.items()], key=lambda s: s[1]))
