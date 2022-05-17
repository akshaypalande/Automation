
"""
@Author: Akshay Palande
@Date: 2022-05-16 12:00:00
@Last Modified By: Akshay Palande
@Last Modified Date: 2022-05-16 12:00:00
@Title: Find effevtive temperature
"""

"""
    
16. Write a program WindChill.java that takes two double command-line arguments t
and v and prints the wind chill. Use Math.pow(a, b) to compute ab.
Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour),
the National Weather Service defines the effective temperature (the wind chill) to
be:

w = 35.74+0.6215+(0.4275t-35.75)v0.16

Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger
than 120 or less than 3 (you may assume that the values you get are in that range).
    

"""


def calculateWindChill(temperatureValue, windSpeed):
    """
    Description:
        this function effective temperature
    Parameter:
        temperatureValue parameter consist temperature value
        windSpeed parameter consist wind speed value
    Return:
        retun wind chill value
    """
    windChill = 35.74 + 0.6215 * temperatureValue + (0.4275 * temperatureValue - 35.75) * (windSpeed ** 0.16)
    return windChill

try:
    temperatureValue = int(input("Enter temperatute value :"))
    windSpeed = int(input("Enter wind speed :"))
except ValueError:
    print("Enter proper value")

windChill = calculateWindChill(temperatureValue, windSpeed)
print("The calculated WindChill = ", windChill)