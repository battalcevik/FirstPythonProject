"""
Battal Cevik
Class: CS 521 - Spring Semester
Date: 04/1/2022
Homework 5 Problem 5.15.5
The formula for calculating the amount of money in a savings account that begins with an
initial principal value (P) and earns annual interest (i) for (n) years is: P(1 + i)n
Note that i is a decimal, not a percent interest rate:
Prompt the user on three lines for principal, percent interest rate and number of years
to invest (using descriptive prompts)
Call your function calc_compound_interest()
Call a second function calc_compound_interest_recursive()
"""


# Use a while loop to keep prompting until entries are valid
while True:
    try:
        principle_value = int(input("Please enter principle value: "))
        int_rate_value = float(input("Please enter interest rate in decimal value (0.1, NOT 10%) : "))
        years_value = int(input("Please enter years: "))
        if int_rate_value < 0 or int_rate_value > 1 or principle_value < 0 or years_value < 0:
            print("Please re-enter values again! Follow the instructions")
        else:
            print("User has entered valid inputs")
            break
    except Exception as e:
        print("Exception error is: ", e)


# Create function calc_compound_interest()
def calc_compound_interest(principle, int_rate, years):
    ending_value = []
    try:
        ending_value = principle * ((1 + int_rate) ** years)
    except Exception as e:
        print("Exception error is: ", e)
    return ending_value


# Create second function calc_compound_interest_recursive()
def calc_compound_interest_recursive(principle, int_rate, years):
    ending_value2 = []
    try:
        if years <= 0:
            return principle
        else:
            # calculates the value recursively – calling a base calculation over and over
            ending_value2 = 0 + calc_compound_interest_recursive((principle * (1 + int_rate)), int_rate, years - 1)
    except Exception as e:
        print("Exception error is: ", e)
    return ending_value2


# Call compound Interest Function
compound_function = calc_compound_interest(principle_value, int_rate_value, years_value)
# Call compound Interest Recursive Function
recursive_function = calc_compound_interest_recursive(principle_value, int_rate_value, years_value)

# formatted with 2 decimal places
print("Call compound function interest rate calculation: ", f"{compound_function:,.2f}")
print("Call compound function interest rate calculation: ", f"{recursive_function:,.2f}")
# formatted with 4 decimal places
print("Call compound function interest rate calculation: ", f"{compound_function:,.4f}")
print("Call compound function interest rate calculation: ", f"{recursive_function:,.4f}")

compound_calculation = round(float(f"{compound_function:,.4f}"))
recursive_calculation = round(float(f"{recursive_function:,.4f}"))
try:
    if compound_calculation == recursive_calculation:
        print("The two values are equal when rounded to 4 decimal places.")
    else:
        print("The two values are NOT equal when rounded to 4 decimal places.")
except Exception as e:
    print("The Exception error is: ", e)



