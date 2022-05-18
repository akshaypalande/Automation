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
def two_dimensional_array():
    """
    Description:
        This function is used for printing 2D array. 
        It takes number of rows and colums and,
        also element of array from user.    
    """

try:

        row = int(input("Enter the number of rows:"))
        col = int(input("Enter the number of columns:"))

        # for storing 2D array of type list
        matrix = []
        print("Enter the entries row wise:")

        for i in range(row):  # loop for row
            array = []
            for j in range(col):  # loop for column
              array.append(int(input()))   # inserting input into blank array
            matrix.append(array)  # appending array with matrix

        # for loop for printing the 2D array
        print("The 2D array is given below:")
        for i in range(row):
            for j in range(col):
                print(matrix[i][j], end="  ")
            print()

except ValueError:
        print("Enter a valid integer input")
        two_dimensional_array()

two_dimensional_array()
