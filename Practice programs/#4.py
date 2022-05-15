'''

@Author: Akshay palande

@Date: 2021-05-12 10:00:30

@Last Modified by: Akshay Palande

@Last Modified time: 2021-02-11 10:00:30

@Title : Basic Python programming

'''



# 4. Write a Python program to calculate the length of a string.

def string_length(string_1):
    count = 0
    for char in string_1:
        count += 1
    return count
print(string_length('First and Last color from above list are Red and Black'))

