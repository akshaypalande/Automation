"""
@Author: Akshay Palande
@Date: 2022-05-14 4:00:00
@Last Modified By: Akshay Palande
@Last Modified Date: 2022-05-14 4:00:00
@Title: factorial program

"""

"""
    
6. Factors
a. Desc -> Computes the prime factorization of N using brute force.
b. I/P -> Number to find the prime factors
c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
d. O/P -> Print the prime factors of number N.
    
"""


def prime_factor(num):
    ## Finding all factors of the given number
    
    factors_list = []
    factor = 2
    while(factor <= num):
        if(num % factor == 0):
            factors_list.append(factor)
        factor = factor + 1
        
    print(factors_list)
    
    ## Finding which of the factors are prime
    
    prime_factors = []
    for i in factors_list:
        for j in range(2,i):
            if(i % j == 0):
                break
        else:
            prime_factors.append(i)
    
    ## Prints results        
    num = str(num)
    prime_factors = str(prime_factors)
    print("The prime factors of " + num + " are " + prime_factors)
    
    
## Takes user input and calls on the prime factorization function                
while True:
    a = int(input('give me a number greater than 1 or enter 0 to quit: '))
    if (a == 0):
        break
    prime_factor(a)
                
