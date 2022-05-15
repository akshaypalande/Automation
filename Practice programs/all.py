'''

@Author: Akshay palande

@Date: 2021-05-12 10:00:30

@Last Modified by: Akshay Palande

@Last Modified time: 2021-02-11 10:00:30

@Title : Basic Python programming

'''


#1. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

first_name = input("Input your First Name : ")
last_name = input("Input your Last Name : ")
print ( last_name + " " + first_name + " is part of Bridzlab")


#2 Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23') """

# List and Tuple

values = input("enter the sample data:  ")
list = values.split(", ")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)


# 3. Write a Python program to display the first and last colors from the following list. 
# color_list = ["Red","Green","White" ,"Black"]

color_list = ["Red","Green","White" ,"Black"]
print(" First and Last color from above list are " + color_list[0] + " and " + color_list[-1])

# 4. Write a Python program to calculate the length of a string.

def string_length(string_1):
    count = 0
    for char in string_1:
        count += 1
    return count
print(string_length('First and Last color from above list are Red and Black'))

# 5. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar
year = int(input("Enter the year : "))
month = int(input("Enter the month : "))
print(calendar.month(year, month))

# 6. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import date
first_date = date(2022, 5, 21)
second_date = date(2022, 5, 12)
difference = first_date - second_date
print(difference.days)

# 7.Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

def strings(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(strings('cat', 'dog'))

# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.

def find_longest_word(list):
    word_len = []
    for n in list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["Akshay", "Maharashtra", "Bridzlab", "Python", "Protocol"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])

# 9.Write a Python program to count the occurrences of each word in a given sentence.

def wordcount(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( wordcount('Write the Python program to count the occurrences of the each word in a given sentence to understand strings program'))


