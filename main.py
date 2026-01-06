import time
from input_system import parse_command
import Inventory_System
from file_management import save_file
from file_management import load_file
import movement_system

def startGame():
    try:
    # Load files before starting the timer, so it doesn't affect the player's score
        file = load_file('testrooms.json')
        items, rooms = file['Objects'], file['Rooms']

        time_start = time.time() 
        username = input("Username: ")
        player = Player(name = username)

        """IN CASE OF EMERGENCY, REMOVE HASH (If we don't fix the interaction bug, consider returning early with the part that works)
        If do, include a comment before, explaining the WHY.)"""
        # return showWinScreen(player, time_start)

        if isInvalidState(player):
            showWinScreen(player, time_start)
            return "Game Over"
        else:
            action = getPlayerAction()
            parse_command(action)
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

def showWinScreen(player, time_start):
    print("Player Wins!")
    print(f"Time: {player.time_score}, Score: {player.score}, HP: {player.health}")
    saveStats(player,time_start)

def saveStats(player, time_start):
    '''Calculates the time taken to complete the game and creates the timescore.
    Also makes a note of the player's score and time taken in a JSON file named receipts.'''

    try:
        time_taken = f"{((time.time()) - time_start):.2f} s"
        player.time_score = time_taken

        print(f"{player.name}: {player.score} POINTS\nTime taken: {time_taken}")
        save_file(f'{player.name}_receipt.json', player.__dict__)
    except Exception as e:
        print(f"An error occurred while saving stats: {e}")

def getPlayerAction():
    return input("Enter your action (Tip: You can use 'go north', 'up', etc.): ").strip().lower()

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
    
    def health(self, damage):
        self.health -= damage 
        self.score -= damage
    
    def health(self, heal):
        self.health += heal 
    
    def gain_points(self, points):
        self.score += points 

if __name__ == "__main__":
    print("= GAME START =")
    startGame()



