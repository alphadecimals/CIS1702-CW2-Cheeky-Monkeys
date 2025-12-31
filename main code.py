import time
from input_system import parse_command
from main import save_file
from main import load_file

cmd = input("what will you do?  ")
keywords = parse_command(cmd)

def startGame(player):
    time_start = time.time() # Start time tracking

    if isInvalidState(player):
        showWinScreen(player)
        saveStats(player, time_start)
        return "Game Over"
    else:
        action = getPlayerAction()
        parse_command(action)

def isInvalidState(player):
    return player.health <= 0 or not validCoordinates(player.coords)

def showWinScreen(player):
    print("Player Wins!")
    print(f"Time: {player.time}, Score: {player.score}, Stats: {player.stats}")

def saveStats(player, time_start):
    '''Calculates the time taken to complete the game and creates the timescore.
    Also makes a note of the player's score and time taken in a JSON file named receipts.'''

    time_taken = f"{((time.time()) - time_start):.2f} s"
    player.time_score = time_taken

    print(f"{player.name}: {player.score} POINTS\nTime taken: {time_taken}")
    save_file(f'{player.name}_receipt.json', player.__dict__)

def getPlayerAction():
    return input("Enter your action: ").strip().lower()

def interactionSystem(keywords, player):
    print(f"Interacting with {keywords['type']}")
    saveStats(player)

#import will's movement system
class Player:
    '''A class to create a player object, tracking stats such as hp, score, time taken etc.'''
    def __init__(self, name):
        self.name = name 
        self.hp = 100
        self.score = 0
        self.time_score = 0 
    
    def lose_hp(self, damage):
        self.hp -= damage 
        self.score -= damage
    
    def gain_hp(self, heal):
        self.hp += heal 
    
    def gain_points(self, points):
        self.score += points 

player = Player()
startGame(player)



