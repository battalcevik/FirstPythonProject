"""
Battal Cevik
Class: CS 521 - Spring Semester
Date: 03/18/2022
Homework 4 Problem 4.9.6
Create a program that:
prompts a user for a number
validates that a number was entered
re‐prompts on error
converts the number to words using a dictionary
prints out the converted numbers as words
The program must only have one input command and work for any size positive or negative number.
Decimal point should be converted to ‘point’.
If the user enters commas, tell them to try again without the commas.
"""

if __name__ == "__main__":
    numbers_dict = {"0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four",
                    "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine",
                    ".": "Point", "-": "Negative"}
    not_number = True
    # Create while loop to catch while it is not number it re-promts on error
    while not_number:
        number = input("Enter a number:")
        if "," in number:
            print("Please try again without entering commas")
        else:
            try:
                float(number)
                not_number = False
            except:
                print('"{}" is not a valid number. Please try again'.format(number))
    # Print the number as text
    print("As Text:", " ".join([numbers_dict[i] for i in str(number)]))
