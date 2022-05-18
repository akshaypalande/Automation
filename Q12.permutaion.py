'''
@Author: Akshay palande
@Date: 2022-05-16 05:01:10
@Last Modified by: Akshay palande
@Last Modified Time: 2022-05-16 05:1:10
@Title: permutation

'''

"""

12.Write static functions to return all permutation of a String using iterative method and
Recursion method. Check if the arrays returned by two string functions are equal.
    
    
"""


# Recursive function to generate all permutations of a string

def permute(word, recursive):
    if (len(word) == 0):
        print(recursive, end = "  ")
        return
    
    
     
    for i in range(len(word)):
        ch = word[i]
        left_substr = word[0:i]
        right_substr = word[i + 1:]
        rest = left_substr + right_substr
        permute(rest, recursive + ch)
 
# Driver Code
recursive = ""
 
word = 'ABC'

print("All possible strings are : ")
permute(word, recursive)
    
print(" ")

print("permutaion using iterative method")
    
# Iterative function to generate all permutations of a string in Python
def permutation(iterative):
 
    # base case
    if not iterative:
        return []
 
    # create a list to store (partial) permutations
    partial = []
 
    # initialize the list with the first character of the string
    partial.append(iterative[0])
 
    # do for every character of the specified string
    for i in range(1, len(iterative)):
 
        # consider previously constructed partial permutation one by one
 
        # iterate backward
        for j in reversed(range(len(partial))):
 
            # remove the current partial permutation from the list
            curr = partial.pop(j)
 
            # Insert the next character of the specified string into all
            # possible positions of current partial permutation.
            # Then insert each of these newly constructed strings into the list
 
            for k in range(len(curr) + 1):
                partial.append(curr[:k] + iterative[i] + curr[k:])
 
    print(partial, end='')
    
    print(" ")   
 
if __name__ == '__main__':
 
    iterative = 'ABC'
    permutation(iterative)
    
print(" ")   
if(iterative == recursive):
    print("Arrays returned by two string functions are Equal")
else:
    print("Arrays returned by two string functions are not Equal")