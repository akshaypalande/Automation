"""
@Author: Akshay Palande
@Date: 2022-05-16 12:00:00
@Last Modified By: Akshay Palande
@Last Modified Date: 2022-05-16 12:00:00
@Title: Find effevtive temperature
"""

"""

2D Array
a. Desc -> A library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output.
b. I/P -> M rows, N Cols, and M * N inputs for 2D Array. Use Java Scanner Class
c. Logic -> create 2 dimensional array in memory to read in M rows and N cols
d. O/P -> Print function to print 2 Dimensional Array. In Java use PrintWriter with
OutputStreamWriter to print the output to the screen.
    
"""

def matrix():
    """
    Description:
        This function is used for printing 2D array. 
        It takes number of rows and colums and,
        also element of array from user.    
    """

rows = int(input("Enter Number of Rows: "))
cols = int(input("Enter number of columns: "))

arr = [[0 for row in range(rows)] for column in range(cols)]

for A in range(rows):
        for B in range(cols):
            arr[A][B] = A*B

        print(arr)

matrix()
