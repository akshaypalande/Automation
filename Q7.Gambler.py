"""
@Author: Akshay Palande
@Date: 2022-05-16 1:00:00
@Last Modified By: Akshay Palande
@Last Modified Date: 2022-05-16 1:00:00
@Title: Gambler Logical Problem
"""

"""

  Gambler
a. Desc -> Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. Run the experiment N
times, averages the results, and prints them out.
b. I/P -> $Stake, $Goal and Number of times
c. Logic -> Play till the gambler is broke or has won
d. O/P -> Print Number of Wins and Percentage of Win and Loss. 
    
"""

# as we are dealing with with gambling problem, i am using random module

import random

def start_gamble(stake, goal):
    """
    Description:
        This function is used for getting bet result.
        Here a player start with stake and goal and play the game
        untill his pocket is empty or he has achieved his goal.
    Parameter:
        It takes two parameter stake is a starting amount of a player,
        And goal is the winning amount or target amount to win by player.
    """
    try:
    # defining variables here
        win = loss = totalGambles = 0

        while not(stake == 0 or stake == goal): # game will go on untill stake is 0 or goal is reached.
            gamble = random.randint(0, 1)
            totalGambles += 1
            if gamble == 0:
                stake += 1
                win += 1

            else:
                stake -= 1
                loss += 1

        print(" You won ", win, " times ")
        print(" You Lost ", loss, " times ")
        print(" Your Total Gamble Played ", totalGambles, " times")
        # Getting the Percentage of Winning
        win_percentage = float((win / totalGambles) * 100)
        print(" Win Percent%", win_percentage)
        # Getting the Percentage of Loosing
        loss_percentage = float((loss / totalGambles) * 100)
        print(" Loss Percent%", loss_percentage)

    except Exception as e:
        print(e)

if __name__ == "__main__":

    print("*********************************************")
    print("       ## Welcome To Gambling World ##       ")
    print("*********************************************")

    try:
        stake = int(input("Enter the starting stake: "))
        while stake < 2:
            stake = int(input("Please start at least with 1 rs : "))

        goal = int(input("Enter a winning goal amount : "))
        while goal < stake:
            goal = int(input("Enter an amount greater than your stake : "))

    except ValueError:
        print("Enter a valid integer value")

start_gamble(stake, goal)

"""
The code starts by declaring variables.
 The stake is the amount of money that the player has put down, and goal is the amount of money that they want to win.
 The bet variable is how many bets will be made on this game.
 The while loop starts with a condition: if stake >= 0 and stake <= goal then it means that there are no more stakes left to make, so the program should stop running.
 If not, then it continues until there are no more stakes left to make or until gambler == 0 which means that all bets have been won or lost (if you lose all your bets).
 If gambler == 1 then we know for sure that all bets have been won because when you gamble in roulette you always get a number between 0-36 (except for 00) so if someone wins every bet they would get 36/37 odds which equals 100% chance of winning
 The code is a while loop that keeps going until the stake amount in rupees is greater than or equal to the goal amount and there are no more bets left.
 The code starts by setting the stake amount in rupees to zero, then it sets the goal amount to zero.
 Then it sets up an if statement with two conditions: If gambler==0, then won+=1 and stake=stake+1.
 If gambler==1, then lost+=1 and stake=-1.
 
 """