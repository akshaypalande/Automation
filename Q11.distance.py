"""
@Author: Akshay Palande
@Date: 2022-05-16 12:00:00
@Last Modified By: Akshay Palande
@Last Modified Date: 2022-05-16 12:00:00
@Title: Find effevtive temperature
"""

"""

Write a program Distance.python that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function
    
"""


import math
import sys
def calculateDistance(x, y):

    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

# Taking input from user

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

# x = int(sys.argv[1]) 
# y  = int(sys.argv[2])
# Calling Function
dist = calculateDistance(x,y)
    

print("The Euclidean Distance between points is: ", dist)

# implement commond arugument

"""

The code calculates the Euclidean distance between two points.
 The code starts by asking for input of x and y, which are integers.
 Then it calculates the square root of (x^2 + y^2).
 Next, it prints out "The Euclidean Distance between points is: ", dist.
 Finally, it calls calculateDistance() to print out the result.
 def calculateDistance(): dist = math.sqrt(math.pow(x, 2) + math.pow(y, 2)) print("The Euclidean Distance between points is: ", dist)
 The code is a function that calculates the Euclidean distance between two points.
 The input for this function is an integer value of x and y.

"""
