"""
Battal Cevik
Class: CS 521 - Spring Semester
Date: 03/18/2022
Homework 4 Problem 4.9.5
Create 3 functions with docstring:
1. letter_counts() takes a string as its argument and returns a dictionary of the letters as
keys and frequency counts as values.
2. most_common_letter() takes a string as its argument and returns a string of the most
common letter(s). In the case of a tie for the most common letter, return them all.
This function should call letter_counts().
3. string_count_histogram() takes a string as its argument and returns a list of the unique
letters, with each letter being the repeated number of times it appears in the string. This list will then be printed one element per line (as a histogram).
This function should call letter_counts().
"""


# Create letter counts function
def letter_counts(my_string):
    counts_dict = {i: my_string.count(i) for i in set(my_string)}
    try:
        counts_dict.pop(' ')
    except:
        pass
        print("")
    return counts_dict


# Create most common letter function
def most_common_letter(my_string):
    counts_dict = letter_counts(my_string)
    sorted_list = sorted([(key, value) for key, value in counts_dict.items()], key=lambda s: s[1], reverse=True)
    most_common = [sorted_list[0][0]]
    max_val = sorted_list[0][1]
    for key, value in sorted_list[1:]:
        if value == max_val:
            most_common.append(key)
    return most_common, max_val


# Create count histogram function
def string_count_histogram(my_string):
    counts_dict = letter_counts(my_string)
    return sorted([key * value for key, value in counts_dict.items()])


if __name__ == '__main__':
    # Example Output #1
    first_string = "WAS IT A RAT I SAW"
    assert len(first_string) > 14, "String has to be at least 15 characters"
    print("The string being analyzed is: ", first_string)
    print("Dictionary of letter counts: ", letter_counts(first_string))
    most_commons = most_common_letter(first_string)
    print("Most frequent letter {} appears {} times.".format(most_commons[0], most_commons[1]))
    hist = string_count_histogram(first_string)
    print_sen = "Histogram: \n"
    for i in hist:
        print_sen += i + "\n"
    print(print_sen)

    # Example Output #2
    second_string = "WWWAS IT A RAT I SAW"
    assert len(second_string) > 14, "String has to be at least 15 characters"
    print("The string being analyzed is: ", second_string)
    print("Dictionary of letter counts: ", letter_counts(second_string))
    most_commons = most_common_letter(second_string)
    print("Most frequent letter {} appears {} times.".format(most_commons[0], most_commons[1]))
    hist = string_count_histogram(second_string)
    print_sen = "Histogram: \n"
    for i in hist:
        print_sen += i + "\n"
    print(print_sen)
