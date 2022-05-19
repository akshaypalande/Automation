"""
@Author: Akshay Palande
@Date: 2022-05-17 08:00:00 
@Last Modified by: Akshay palande
@Last Modified time: 2022:05:17 08:00:00
@Title : Program Aim is find the roots of the equation a*x*x + b*x + c. 
"""
"""

15.Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
can be found using a formula
delta = b*b - 4*a*c
Root 1 of x = (-b + sqrt(delta))/(2*a)
Root 2 of x = (-b - sqrt(delta))/(2*a)
Take a, b and c as input values to find the roots of x

"""


import math

def quadratic():
    """
    Description:
        This function is used for calculating  root of a equation .
        It takes point a ,b and y values from the user and then find delta by applying formulae.
        And then calculate the root of the equation.
          
    """

    try:
        a = int(input("Enter value for a : "))
        b = int(input("Enter value for b : "))
        c = int(input("Enter value for c : "))

        delta = abs(b * b - 4 * a * c) # getting absolute value.

        root1 = (-b + math.pow(delta, 1 / 2)) / (2 * a)
        root2 = (-b - math.pow(delta, 1 / 2)) / (2 * a)
        print("The First Root Of Equation Is " , root1)
        print("The Second Root Of Equation Is ", root2)
    
    except ValueError:
        print("Enter a Numeric value")
        quadratic()
    except ZeroDivisionError:
        print("Value of a shouldnt be zero :")
        quadratic()

quadratic()