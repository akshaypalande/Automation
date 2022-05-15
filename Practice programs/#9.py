'''

@Author: Akshay palande

@Date: 2021-05-12 10:00:30

@Last Modified by: Akshay Palande

@Last Modified time: 2021-02-11 10:00:30

@Title : Basic Python programming

'''


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


