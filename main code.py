from inputSystem import parseCommand
from fileManagement import saveFile

cmd = input("what will you do?  ")
keywords = parseCommand(cmd)

def startGame(player):
    if isInvalidState(player):
        showWinScreen(player)
        saveStats(player)
        return "Game Over"
    else:
        action = getPlayerAction()
        processInput(action, player)

def isInvalidState(player):
    return player.health <= 0 or not validCoordinates(player.coords)

def showWinScreen(player):
    print("Player Wins!")
    print(f"Time: {player.time}, Score: {player.score}, Stats: {player.stats}")

def saveStats(player):
    print("Stats saved.")

def getPlayerAction():
    return input("Enter your action: ").strip().lower()

def interactionSystem(keywords, player):
    print(f"Interacting with {keywords['type']}")
    saveStats(player)

#import will's movement system


player = Player()
start_game(player)



