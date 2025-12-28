'''This is a potential outline for the main game file, showing the structure and functions needed.
Just a skeleton, no actual code implementation. Helps us plan the overall flow of the game and figure out the logic and to prevent mental breakdowns in the future.''' 

class Player:
    pass 

def main():
    introduction()
    option = validate_input()
    if option == 'Help':
        help()

    rooms, items = load_file('rooms.json'), load_file('items.json')

    cords = [0, 0]
    won = False 
    while not won: 
        room = rooms['cords'][cords]
        won = run_room()

        if player['health'] == 0:
            end_game('LOSS')
    end_game('WON')

def introduction():
    # Greets player, introduces story
    pass 

def help():
    # More information, list of commands
    pass 

def load_file(filename):
    # Loads json file
    pass 

def validate_input(msg, options):
    # Checks input is a part of the options, promting with a custom string
    pass 

def run_room():
    # Gets items from room data, prints details of them and promts user to interact Returns True or False if game is won
    pass

def end_game(win_lose):
    # Saves data, prints message based on won or lost, exits
    pass

if __name__ == "__main__":
    main()