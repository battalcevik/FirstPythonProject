"""
Battal Cevik
Class: CS 521 - Semester
Date: 03/06/2022
Homework 3 Problem 3.6.5
Manually create a text file with a single sentence of 20 words.
Write a program that reads the file and writes the words to a new text file so that there are
four lines of five single spaced words.
"""
import sys

# Open a file in write format and add text to the file
file1 = open('bcevik_hw_3_6_5_file1.txt', 'w')
file1.write("Hello From Alaska which is Located at the northwest corner of North America," "\n"
            "Alaska is the northernmost and westernmost state")
file1.close()

# Reading the file with exception handling after adding text
try:
    file1 = open('bcevik_hw_3_6_5_file1.txt', 'r')
    # Reading the file1 and splitting them by words
    file1_data = file1.read().split()
    # check if text file has 20 words.
    split_length = len(file1_data)
    print(split_length)
except FileNotFoundError as e:
    sys.exit("Error: This file does not exist: ", e)
except IOError as e:
    sys.exit("Error: This file does n ot found: ", e)

# Open another file in write mode
try:
    file2 = open('bcevik_hw_3_6_5_file2.txt', 'w')
except FileNotFoundError as e:
    sys.exit("Error: This file does not exist: ", e)
except IOError as e:
    sys.exit("Error: This file does n ot found: ", e)
    # print("File does not exist: ", e)

# Creating 5 words of blocks and type to second file
for i in range(0, len(file1_data), 5):
    file2.write(' '.join(file1_data[i:i + 5]))
    file2.write('\n')

# Close both files
file1.close()
file2.close()
