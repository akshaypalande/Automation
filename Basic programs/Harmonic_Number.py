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
    """
    Description:
        This function genrate harmonic number of nth number
    
    Parameter:
        number parameter is nth harmonic value
        
    Return:
        harmonic return value is nth harmonic value
    """
 
    harmonic = 1.00

    for i in range(2, number + 1) :
        harmonic += 1 / i
 
    return harmonic

print("Enter a number:")
number = int(input())
print("harmonic value = ", round(nthHarmonic(number),2))

"""

The n-th harmonic number Hn is defined by

Hn = 1 + 1/2 + 1/3 + ... + 1/n,
so that
      H1 =     1,
      H2 =    3/2,
      H3 =   11/6,
      H4 =   25/12,
      H5 =  137/60,
      H6 =   49/20,
      H7 =  363/140,
      H8 =  761/280,
      H9 = 7129/2520,

"""
