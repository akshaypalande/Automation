"""
@Author: Akshay Palande
@Date: 2022-05-14 4:00:00
@Last Modified By: Akshay Palande
@Last Modified Date: 2022-05-14 4:00:00
@Title: factorial program

"""

def factor(number):

    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
    return number


userinput = int(input("Enter an Number:"))
print(" Factors : " + str(factor(userinput)))