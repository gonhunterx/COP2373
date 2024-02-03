# import random and time for calculations and simulation 
import random 
import time 

# constants for race start and end 
RACE_START = 1
RACE_END = 70 

def move_hare(hare):
    # move hare 
    # randomize move to choose 
    move = random.randrange(1, 11)
    if 1 <= move <= 2:
        # sleep no move 
        hare = hare 
    elif move in (3, 4):
        hare += 9
    elif move == 5:# big slip 
        hare -= 12
    elif move in (6, 7, 8): # small hop  
        hare += 1
    else: # slip 
        hare -= 2
    # ensure hare does not slip at start or go over race end 
    if hare < 1:
        hare = 1
    elif hare > RACE_END:
        hare = RACE_END
    return hare 

def move_tortoise(tortoise):
    # move tortoise 
    # randomize move to choose 
    move = random.randrange(1, 11) 
    if 1 <= move <= 5: # fast 
        tortoise += 3
    elif move in (6,7): # slip 
        tortoise -= 6
    else: # slow plod 
        tortoise += 1
    # ensure tortoise doesnt split beyond start position or past the finish 
    if tortoise < 1:
        tortoise = 1
    elif tortoise > RACE_END:
        tortoise = RACE_END
    return tortoise

# function used to continuously print positions 
def print_positions(tortoise, hare):
    # initlize it with a loop using our constants for range params 
    for i in range(RACE_START, RACE_END + 1):
        # check if they are on the same spot 
        if i == tortoise == hare:
            print("OUCH!!!", end='')
        # print hare's location 
        elif i == hare:
            print('H', end='')
        # print tortoise's location 
        elif i == tortoise:
            print('T', end='')
        # fill empty spots 
        else:
            print(' ', end='')
    # continue to print 
    print()
    
# function to use in the main menu for starting the race     
def initiate_race():
    # starting print message
    print("BANG!!!!!\nAND THEY'RE OFF!!!!!!")
    # set the hare and the tortoise to the start of the race 
    hare = RACE_START 
    tortoise = RACE_START
    # print their positions 
    print_positions(tortoise, hare)

    # loop to continue until one of them has finished the race     
    while tortoise < RACE_END and hare < RACE_END:
        # initlize the move functions for both hare and tortoise 
        hare = move_hare(hare)
        tortoise = move_tortoise(tortoise)
        # print positions 
        print_positions(tortoise, hare)
        # delay output by 1 second per iteration 
        time.sleep(1)
    # conditional finish statements 
    if tortoise > hare:
        print('TORTOISE WINS!!! YAY!!!')
    elif hare > tortoise:
        print('Hare wins. Yuch.')
    else:
        print("It's a tie.")
    
# main menu for calling functions and displaying menu options 
def main():
    while True:
        print("Initiate race (y/n)")
        choice = input("Input: ").lower()
        if choice == "y":
            initiate_race()
        elif choice == "n":
            break
        else:
            print("Please enter 'y' or 'n'.")

# calling the main function only 
if __name__ == "__main__":
    main()