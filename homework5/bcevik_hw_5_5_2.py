"""
Battal Cevik
Class: CS 521 - Spring Semester
Date: 04/1/2022
Homework 5 Problem 5.5.2
takes as input from the user a date and time (24‐hour clock) as "MM/DD/YYYY HH:mm:SS"
o Assume that everything must be provided with leading zeros
     calls the function is_valid_datetime () that:
o takes a string argument
o validates that the string has all the elements to be a valid date and time
o returns 2 values:
"""

# Takes as input from the user a date and time (24‐hour clock) as "MM/DD/YYYY HH:mm:SS"
input_date_time = input("Enter a date time (MM/DD/YYY HR:MIN:SEC): ")


# Create the function is_valid_datetime ()
def is_validate_datetime(time):
    try:
        # Split the input with escape character to assign into 2 list as date and time
        date_time = time.split(" ")
        # Split the date into 3 list item by using /
        date = date_time[0].split("/")
        # Split the time into 3 list item by using :
        time = date_time[1].split(":")
        # Create if condition to print correct format of the output
        if "12" >= date[0] >= "01":
            if "31" >= date[1] >= "01":
                if "01" <= date[2] <= "9999":
                    if "25" >= time[0] >= "0":
                        if "59" >= time[1] >= "0":
                            if "59" >= time[2] >= "0":
                                print("DD/MM/YYYY is {}/{}/{}".format(date[1], date[0], date[2]))
                                print("HR:MIN:SEC is {}:{}:{}".format(time[0], time[1], time[2]))
                                print("MM/YYYY is {}/{}".format(date[0], date[2]))
                                if time[0] > "12":
                                    print("The time is PM")
                                else:
                                    print("The time is AM")
        # Create if condition to print invalid requests if user enter invalid data
        if date[0] < "01" or date[0] > "12":
            print("Invalid: there can be only 12 months in a year.")
        elif date[1] < "01" or date[1] > "31":
            print("Invalid: there can be only 31 days in a month.")
        elif date[0] < "1" and date[1] < "1" and date[2] < "1":
            print("Invalid: there can not be a negative year.")
        elif time[0] < "0" or time[0] > "23":
            print("Invalid: there can be only 24 hours in a day.")
        elif time[1] < "0" or time[1] > "59":
            print("Invalid: there can be only 60 minutes in a hour.")
        elif time[2] < "0" or time[2] > "59":
            print("Invalid: there can be only 60 seconds in a minute.")
    except Exception as e:
        print("Exception error is: ", e)
    return time


# Call the function to see output of the code
is_validate_datetime(input_date_time)
