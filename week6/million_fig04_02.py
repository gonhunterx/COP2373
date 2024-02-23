# using defaultdict to utilize its capabilities of automatic initialization which means I do not have to check if a key exists 
# before updating its value 
from collections import defaultdict
# fig04_02.py
"""Simulating the dice game Craps."""
import random


# roll dice function that came with the original program 
def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple


# defaultdicts initlized with the int type for more secure manipulation
wins = defaultdict(int)
losses = defaultdict(int)
# setting total games variable = to 1 million to use in for loop 
total_games = 1000000


# for loop initlized with a variable I will not use in the look therefore I used '_'
for _ in range(total_games):
    # setting variables for the loop 
    # how this is working is that every time it goes through the loop roll_count resets to 1. 
    # that means for each iteration it has the opportunity to climb in the number of rolls and that is how I am storing the 
    # roll count in each defaultdict (wins and losses) and the associated number of wins or losses at the specific keys
    roll_count = 1
    # initlize the game statas as continue and removed the initial dice roll check logic. 
    game_status = 'CONTINUE'
    die_values = roll_dice()
    sum_of_dice = sum(die_values)
    
    
    if sum_of_dice in (7, 11): # win on first roll 
        # incrementing the wins default dict at the specified roll_count
        wins[roll_count] += 1
    elif sum_of_dice in (2, 3, 12):
        # increment losses at roll_count
        losses[roll_count] += 1
    else:
        # else we need to create the point and set it equal to the sum of the dice 
        my_point = sum_of_dice
        while game_status == 'CONTINUE':
            # incrementing roll_count 
            roll_count += 1
            die_values = roll_dice()
            sum_of_dice = sum(die_values)
            if sum_of_dice == my_point: # win by making point 
                # increment wins at specific roll_count 
                wins[roll_count] += 1
                game_status = 'WON'
            elif sum_of_dice == 7: # loss by rolling 7
                # increment losses at specific roll_count 
                losses[roll_count] += 1
                game_status = 'LOST'

# calculating percentages 
percentage_wins = sum(wins.values()) / total_games * 100 
percentage_losses = sum(losses.values()) / total_games * 100


# creating a new dict for handling the percentage of resolved values for wins and losses in one dict 
resolved_on_roll = defaultdict(int)
for roll in wins:
    resolved_on_roll[roll] += wins[roll]
for roll in losses:
    resolved_on_roll[roll] += losses[roll]

# creating a cumulative counter
cumulative = 0
# normal dictionary for storing percentages 
cumulative_percentages = {}
# for loop to iterate through the populated resolved_on_roll dictionary
# using .keys() because I can access the values of the specific key for incrementing my counter 
for roll in sorted(resolved_on_roll.keys()):
    # increment the cumulative counter with the value at the roll 
    cumulative += resolved_on_roll[roll]
    # set the percentage for the current, in loop, roll value 
    cumulative_percentages[roll] = cumulative / total_games * 100

# output
print(f"Percentage of wins: {percentage_wins:.2f}%")
print(f"Percentage of losses: {percentage_losses:.2f}%")
print("Percentage of wins/losses based on the total number of rolls (1 million)\n")

# headers for columns 
header1 = f"{'Rolls':<5}{'% Resolved':>17}{'Cumulative %':>20}"
header2 = f"{'':<5}{'on this roll':>17}{'of games resolved':>20}"

# printing headers I made so that I can have multi-line text in one sequence for terminal output
print(header1)
print(header2)

# going through our last dict cumulative_percentages to get the sorted keys and using the associated values 
for roll in sorted(cumulative_percentages.keys()):
    print(f"{roll:<5}{resolved_on_roll[roll] / total_games * 100:>15.2f}%{cumulative_percentages[roll]:>18.2f}%")













##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
