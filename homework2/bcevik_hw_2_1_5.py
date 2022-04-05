"""
Battal Cevik
Class: CS 521 - Semester
Date: 02/21/2022
Homework 2 Problem 1.5
1.5: Write a program that: prompts user for weight and height in one input and performs BMI calculation
Also prints BMI calculation
"""
while True:
    try:
        # I would like to take two inputs at a time and typecasts them to float
        weight, height = [float(numbers) for numbers in
                          input("Enter user weight is in kg and height is in meters: ").split(",")]
        print("User weight is {} kg and height is {} meters".format(weight, height))
        # perform BMI calculation
        bmi_calculation = weight / height ** 2
        # print BMI calculation
        print("User BMI result is: ", bmi_calculation)
        break
    except ValueError:
        # I would like to guide user if enters wrong input
        print("This is not a valid kg or meters", "Inputs are separated by comma", "Enter value again")
