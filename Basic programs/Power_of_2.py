"""

@Author: Akshay Palande
@Date: 2022-05-14 5:30:00
@Last Modified By: Akshay Palande
@Last Modified Date: 2022-05-14 5:30:00
@Title: Leap year program

"""

"""

4. Power of 2
a. Desc -> This program takes a command-line argument N and prints a table of the
powers of 2 that are less than or equal to 2^N.
b. I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
c. Logic -> repeat until i equals N.

"""

def power_table(input):
    
    for i in range(input + 1):
        if i <= input:
            final = 2 ** i
    print("2 * ", i, " = ", (final))


userinput = int(input("Enter the number : "))
if(userinput >= 0 & userinput <= 31):
    power_table(userinput)
else:
    print("Please Enter Valid Input ")