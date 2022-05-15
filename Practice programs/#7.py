'''

@Author: Akshay palande

@Date: 2021-05-12 10:00:30

@Last Modified by: Akshay Palande

@Last Modified time: 2021-02-11 10:00:30

@Title : Basic Python programming

'''


# 7.Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

def strings(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(strings('cat', 'dog'))