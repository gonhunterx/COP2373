import random 
import numpy as np 


class Player:
    def __init__(self, name):
        self.name = name 
        self.inventory = {}
        

class Game:
    def __init__(self, player):
        self.running = True 
        self.player = player
    
    def campaigne_menu(self):
        print("1. Enter dungeon")
        print("2. Enter castle")
        print("3. Leave capmaigne mode")
        selection = input("Input: ")
        return selection
        
            
    def campaigne(self):
        print(f"{self.player.name} enters campaigne  mode...")
        selection = self.campaigne_menu()
        if selection == "1":
            print("You enter the dungeon")
            print("What do you do? (look, walk)")
            choice = input("Input: ")
            if choice.lower() == "walk":
                print("You walk further into the dungeon and see a door and a hallway to the left lit by a dim torch...")
                choice = input("Input (open, walk, exit)")
                if choice.lower() == "open":
                    print("You try to open the door and fail...")
                    
                
            
                    
    
    def shop(self):
        print(f"{self.player.name} enters the shop...")
        

    def run(self):
        print("Welcome to Namatashi")

        while self.running:
            print("=" * 20)
            print("Menu:")
            print("1. Enter Story")
            print("2. Go to shop")
            print("3. Exit game")
            choice = input("Input: ")
            if choice == "1":
                self.campaigne()
            elif choice == "2":
                self.shop()
            elif choice == "3":
                break
            
        
player_name = input("What is your name?: ")
player = Player(player_name)
game = Game(player)
game.run()