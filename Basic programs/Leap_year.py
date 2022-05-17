"""
@Author: Akshay Palande
@Date: 2022-05-14 5:00:00
@Last Modified By: Akshay Palande
@Last Modified Date: 2022-05-14 5:00:00
@Title: Leap year program

"""

"""

3. Leap Year
a. I/P -> Year, ensure it is a 4 digit number.
b. Logic -> Determine if it is a Leap Year.
c. O/P -> Print the year is a Leap Year or not.

"""

def leapyear(year):
    """
    Description: 
        This function will first check that a give user input is 4-digit or not,if that is true then
        It will further check for condition if  statement and gives the result.
    Parameter:
        year  is used for getting user input of year for checking leap year or not.
    """

year = int(input("please enter a year : "))


if (year <= 999 or year > 9999):
        print("Please enter a valid year")
        
else:

    if (year % 400 == 0 & year % 100 != 0) or (year % 4 == 0):

            print(year, " is a leap year ")
    else:
            print(year,  " is not a leap year ")

# mod returns, try on pen paper
