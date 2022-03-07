"""
Battal Cevik
Class: CS 521 - Semester
Date: 02/21/2022
Homework 2 Problem 2.6
2.6: Using a ‘for loop’, write a program that calculated and prints all the leap years from
1900 to 2020 (inclusive). Do not use the calendar library.
Then perform this calculation a second time using a ‘while loop’.
"""
leap_year = range(1900, 2021)
checking_year = 0


def find_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return year
    print()


# Code written with for loop
for n in leap_year:
    if find_leap_year(n):
        checking_year = checking_year + 1
        print(find_leap_year(n), end="\n")
print("Checking year: ", checking_year)

# Code written with while loop
x = 1900
while x < 2021:
    if x % 4 == 0:
        x += 1
    print("Test", x)