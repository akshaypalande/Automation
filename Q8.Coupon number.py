"""
@Author: Akshay Palande
@Date: 2022-05-16 2:00:00
@Last Modified By: Akshay Palande
@Last Modified Date: 2022-05-16 2:00:00
@Title: Coupon problem
"""

""" 

Coupon Numbers
a. Desc -> Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.
b. I/P -> N Distinct Coupon Number
c. Logic -> repeatedly choose a random number and check whether it's a new one.
d. O/P -> total random number needed to have all distinct numbers.
e. Functions => Write Class Static Functions to generate random number and to
process distinct coupons.

"""

import random

def distinct_coupons():
  """
    Description:
        This function is used to generate random and unique coupon numbers.
        User input is given for number and range of coupon numbers.
        Random fuction is used to generate random coupon numbers.
    
    """         
coupon = []   #empty list
random_numbers=0  #no.of random numbers needed to generate distinct coupons

try:
    
    number = int(input("\nHow many digit numbers you want to generate as distinct coupon number : "))
    print("Distinct Coupon Numbers Generated")
    for element in range(number):
                coupon_number = random.randint(0,9)
                if coupon_number not in coupon:
                    coupon.append(coupon_number)  #adding the distinct random number gnerated to list 
                    print(coupon_number)
                    random_numbers+=1
                    
  
                    
    else:
        pass           
    #print(distinct_coupons)
    print(random_numbers,end = " ")
except Exception as err:
            print("Not A Valid Number",err)
distinct_coupons() 
print()

