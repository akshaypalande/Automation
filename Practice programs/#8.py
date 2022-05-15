'''

@Author: Akshay palande

@Date: 2021-05-12 10:00:30

@Last Modified by: Akshay Palande

@Last Modified time: 2021-02-11 10:00:30

@Title : Basic Python programming

'''


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


