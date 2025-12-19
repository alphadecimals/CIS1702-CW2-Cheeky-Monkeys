import json 
from input_system import parse_command

class Player:
    def __init__(self, name):
        self.name = name 
        self.hp = 100
        self.score = 0
    
    def lose_hp(self, damage):
        self.hp -= damage 
        self.score -= 5
    
    def gain_hp(self, heal):
        self.hp += heal 
    
    def gain_points(self, points):
        self.score += points 
    

def game_loop():
    print("Game Started.Type'quit' to exit.")
    while True:
        cmd=parse_command(input(">"))
        if cmd is None:
            continue
        if cmd.verb=="quit":
            print("Bye!")
            break
        print(cmd)
#if __name__=="__main__":
#    game_loop()

def main():
    items = load_file("items_test.json")
    rooms = load_file("rooms_test.json")

    player = Player(input("Username: "))
    player.lose_hp(20)
    player.gain_points(200)
    print(f"{player.name}: {player.score} POINTS")

    save_file(f'{player.name}_receipt.json', player.__dict__)

def load_file(filename):
    """Safely attempts to open the specified filepath, returning either the JSON file or an empty list. """
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("!! File not found !! Exiting... ", end="")
    except json.JSONDecodeError:
        print("!! File corrupted !! Exiting... ", end="")
    exit()

def save_file(filename, data):
    print("Attempting to save data... ")
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
        print("Data saved!")

if __name__ == "__main__":
    main()
