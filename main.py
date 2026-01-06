import time
from input_system import parse_command
import Inventory_System
from file_management import save_file
from file_management import load_file
import movement_system
from random import randint

def startGame():
    try:
        # Loads files and gets username before starting the timer, so it doesn't affect the player's score
        file = load_file('rooms_items.json')
        items, rooms = file['Objects'], file['Rooms']
        flavourfile = load_file('flavour_text.json')
        info = flavourfile['Info']
        print(f"Scenario: {info["Name"]}")
        print(info["Description"])

        username = input("Username: ")
        player = Player(name = username)
        
        time_start = time.time() 

        moves = 0
        while True:
            if isInvalidState(player) or moves == 4:
                showEndScreen(player, time_start, info)
                return "Game Over"
            else:
                action = getPlayerAction()
                choice = parse_command(action)
                if choice in ["north","east","south","west"]:
                    player.coords = movement_system.Movementsystem(player.coords,choice)
                    moves += 1 
                    player.gain_points(randint(5, 500))
                    player.lose_hp(randint(1, 35))

                else:
                    print("Please give your direction as 'north', 'east', 'south', 'west'.")
                    player.health = 0 
                    showEndScreen(player, time_start, info)

    except Exception as e:
        print(f"An error occurred: {e}")
        exit()

def isInvalidState(player): 
    return player.health <= 0 or not validCoordinates(player)

def validCoordinates(player):
    if player.coords == movement_system.coordiantes:
        return True
    else:
        return False 

def showEndScreen(player, time_start, Info):
    time_taken = (time.time() - time_start)
    player.time_score = round(time_taken)

    if player.time_score < 5:
        player.gain_points(100)
        print("\n!! Big time bonus applied !! \n")
    elif player.time_score < 10:
        player.gain_points(50)
        print("\n!! Time bonus applied!! \n")
    elif player.time_score < 100:
        player.lose_points(100)
        print("\n!! Time penalty applied !!\n")

    print(Info["EscapeText"])
    if player.health < 1:
        print(f"Player Died!\nHP: {player.health}")
    else:
        print(f"Player Wins!\nHP: {player.health}")
    saveStats(player)

def saveStats(player):
    '''Calculates the time taken to complete the game and creates the timescore.
    Also makes a note of the player's score and time taken in a JSON file named receipts.'''

    try:
        print(f"{player.name}: {player.score} POINTS\nTime taken: {player.time_score}s")
        save_file(f'{player.name}_receipt.json', player.__dict__)
    except Exception as e:
        print(f"An error occurred while saving stats: {e}")

def getPlayerAction():
    return input("Enter your action (Tip: You can use 'go north', 'go south', etc.): ").strip().lower()

def interactionSystem(keywords, player):
    print(f"Interacting with {keywords['type']}")
    saveStats(player)

def getInventory(player, item):
    try:
        inventory = Inventory_System.InventorySystem()
        if item == player.input("Enter the item to take: "):
            if inventory.Used_Up(item):
                print("Item has already been used up.")
            else:
                inventory.Take_From(item)
        else:
            print("Item not found in the current room.")
    except Exception as e:
        print(f"An error occurred while getting inventory: {e}")

class Player:
    '''A class to create a player object, tracking stats such as hp, score, time taken etc.'''
    def __init__(self, name):
        self.name = name 
        self.health = 100
        self.score = 0
        self.time_score = 0 
        self.coords = movement_system.coordiantes
    
    def move(self, direction):
        self.coords = movement_system.Movementsystem(self.coords, direction)
    
    def lose_hp(self, damage):
        self.health -= damage 
        self.score -= damage
    
    def gain_hp(self, heal):
        self.health += heal 
    
    def gain_points(self, points):
        self.score += points 

if __name__ == "__main__":
    print("= GAME START =")
    startGame()




