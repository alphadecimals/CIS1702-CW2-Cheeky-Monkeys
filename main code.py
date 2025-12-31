from inputSystem import parseCommand
from fileManagement import saveFile

def startGame(player):
    if isInvalidState(player):
        showWinScreen(player)
        saveStats(player)
        return "Game Over"
    else:
        action = getPlayerAction()
        processInput(action, player)

def isInvalidState(player):
    return player.health <= 0 or not valid_coordinates(player.coords)

def showWinScreen(player):
    print("Player Wins!")
    print(f"Time: {player.time}, Score: {player.score}, Stats: {player.stats}")

def saveStats(player):
    print("Stats saved.")

def getPlayerAction():
    return input("Enter your action: ").strip().lower()

def processInput(action, player):
    keywords = extract_keywords(action)     
    if keywords["type"] == "object" or keywords["type"] == "verb":
        interaction_system(keywords, player)
    elif keywords["type"] == "direction":
        navigationSystem(keywords, player)
    else:
        handleError(keywords)

def extractKeywords(action):
    
    if action in ["take", "use", "open"]:
        return {"type": "verb"}
    elif action in ["door", "key", "sword"]:
        return {"type": "object"}
    elif action in ["north", "south", "east", "west"]:
        return {"type": "direction"}
    else:
        return {"type": "unknown"}

def interactionSystem(keywords, player):
    print(f"Interacting with {keywords['type']}")
    saveStats(player)

def navigationSystem(keywords, player):
    print(f"Navigating {keywords['type']}")
    saveStats(player)

def handle_error(keywords):
    if keywords["type"] == "object":
        print("Error: With what?")
    elif keywords["type"] == "verb":
        print("Error: Do what with it?")
    elif keywords["type"] == "direction":
        print("Error: Which way?")
    else:
        print("Error: Can you rephrase?")

def valid_coordinates(coords):
    return coords in ["A1", "B2", "C3"]


player = Player()
start_game(player)

