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

number = int(input("\nEnter number of unique coupon numbers to generate :"))
print( )
print(random.sample(range(1, 9), number))


