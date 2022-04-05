"""
Battal Cevik
Class: CS 521 - Spring Semester
Date: 04/1/2022
Homework 5 Problem 5.5.1
Takes as input from the user an English sentence
Calls the function vc_counter() that:
 takes a string argument
 counts the number of vowels and consonants in the string
 returns a dictionary of the counts, using the keys total_vowels and total_consonants
Uses the return from vc_counter() to print the total vowels and consonants with appropriate
descriptions.
"""

# Prompt an English sentence from user:  The quick brown fox's jump landed past the lazy dog!
my_string = input("Enter an English sentence: ")


# Create a function vc_counter takes a string argument
def vc_counter(input_string):
    VOWELS = set('AEIOUaeoiu')
    CONSONANTS = set('BCDFGJKLMNPQSTVXZHRWYbcdfgjklmnpqstvxzhrwy')
    # Counts the number of vowels and consonants in the string in dictionary
    my_dictionary = {"total_vowels": 0, "total_consonants": 0}
    # Create a for loop to find each element in string
    for i in input_string:
        if i in VOWELS:
            my_dictionary["total_vowels"] = my_dictionary["total_vowels"] + 1
        elif i in CONSONANTS:
            my_dictionary["total_consonants"] = my_dictionary["total_consonants"] + 1
    return my_dictionary


# return from vc_counter() to print the total vowels and consonants
print("Total # of vowels in sentence:", vc_counter(my_string)["total_vowels"])
print("Total # of consonants in sentence:", vc_counter(my_string)["total_consonants"])
