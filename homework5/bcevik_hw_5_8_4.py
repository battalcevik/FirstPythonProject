"""
Battal Cevik
Class: CS 521 - Spring Semester
Date: 04/1/2022
Homework 5 Problem 5.8.4
Write a python program that does the following:
    Prompt for a file name of text words.
    Words can be on many lines with multiple words per line.
    Read the file and convert the words to a list.
    Call a function you created called list_to_once_words(), that takes a list as an argument and
    returns a list that contains only words that occurred once in the file.
    Print the results of the function with an appropriate description.
    Think about everything you must do when working with a file.
"""
import sys

# Prompt for a file name from user
file_name = input("Please enter file name (example:bcevik_hw_5_8_4) as text: ")
# Read the file
try:
    file_read = open(file_name, "r")
except FileNotFoundError as e:
    sys.exit("Error: This file does not exist: ", e)
except IOError as e:
    sys.exit("Error: This file does n ot found: ", e)

# Creating a list to assign file data into the list
file_words = []
for lines in file_read:
    line = lines.strip().split(' ')
    for words in line:
        if len(words) > 0:
            file_words.append(words)

# Close the file
file_read.close()
print("Print how many words are listed in file: ", len(file_words))


def list_to_once_words(word_list):
    count_words = []
    try:
        for unique_word in word_list:
            if word_list.count(unique_word) == 1:
                count_words.append(unique_word)
        print("Print how many unique word are listed in file: ", len(count_words))
    except Exception as e:
        print("Exception error is: ", e)
    return count_words


print("Unique words that occurred only once in file: ", list_to_once_words(file_words))
