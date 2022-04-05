"""
Battal Cevik
Class: CS 521 - Semester
Date: 02/21/2022
Homework 2 Problem 2.7
2.7: Rewrite this following ‘for loop’ as a ‘while loop’ and create a working program:
Hint: X is a constant variable.
for i in range(1, X + 1):
if X % i == 0:
print(i)
"""
# Write program with for loop
X = 10
for i in range(1, X + 1):
    if X % i == 0:
        print(i)


# Write program with while loop
X = 10
i = 1
while i < X+1:
    if X % i == 0:
        print(i)
    i = i + 1

