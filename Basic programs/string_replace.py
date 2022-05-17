'''
    @Author: Akshay Palande
    @Date: 2022-05-14 3:22:37
    @Last Modified by: Akshay Palande
    @Last Modified time: 2022-05-14 3:22:37
    @Title : User Input, string replace program
    
'''

"""
    
1. User Input and Replace String Template “Hello <<UserName>>, How are you?”
a. I/P -> Take User Name as Input. Ensure UseName has min 3 char
b. Logic -> Replace <<UserName>> with the proper name
c. O/P -> Print the String with User Name
    
"""

template = 'Hello <<username>>, How are you?'

username = input("Enter Name: ")

if(len(username)<3):
    print("username have minimum 3 character")
else:
    print()

print("'Hello {}, How are you?'".format(username))
