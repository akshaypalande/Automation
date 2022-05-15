"""

@Author: Akshay Palande
@Date: 2022-05-14 5:50:00
@Last Modified By: Akshay Palande
@Last Modified Date: 2022-05-14 5:50:00
@Title: Harmonic Number Program

"""

"""

5. Harmonic Number
a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
(http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).
b. I/P -> The Harmonic Value N. Ensure N != 0
c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
d. O/P -> Print the Nth Harmonic Value.

"""

def nthHarmonic(number) :
 
    harmonic = 1.00

    for i in range(2, number + 1) :
        harmonic += 1 / i
 
    return harmonic

print("Enter a number:")
number = int(input())
print(round(nthHarmonic(number),2))