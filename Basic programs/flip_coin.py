"""
@Author: Akshay Palande
@Date: 2022-05-14 03:02:00
@Last Modified By: Akshay Palande
@Last Modified Date: 2022-05-14 03:02:00
@Title: Flip Coin and print percentage of Heads and Tails
”"""


""" 
2. Flip Coin and print percentage of Heads and Tails
a. I/P -> The number of times to Flip Coin. Ensure it is positive integer.
b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
heads
c. O/P -> Percentage of Head vs Tails
    
"""
    
    
import random

print("Enter the number of times you want to flip the coin:")
flip = int(input())
head = 0
tail = 0 

"""
    Description:
        This function is used to take input the number of times the user
        wants to flip a coin and check heads or tails.And later get the 
        percentage of heads vs Percentage of Tails.
    Parameter:
        input is used for get user input which gives number of times user
        wants to flip a coin.
    """

for number in range(0, flip) :
    # random generate a random value between 0.0 and 0.1
    coin = random.random();
    if coin < 0.5 :
        tail += 1
    else :
        head += 1
        
    """ here we are using random function, to count probability of head and tail
    """
        
# Calculating head and tail percentage
      
tailPercentage = (tail/flip)*100
headPercentage = 100 - tailPercentage

# calculate head percentage and then minus tail.


# printing the percentage value of flips for head and tail
print("Tail percentage is = ", tailPercentage,"%")
print("Head Percentage is = ", headPercentage,"%")

