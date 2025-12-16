import json 
from input_system import parse_command

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
if __name__=="__main__":
    game_loop()

def main():
    # Testing file management with dummy jsons 
    items = load_inventory("items_test.json")
    rooms = load_inventory("rooms_test.json")
    
    print(f"Items: {items}")
    print(f"Room1 original name: {rooms[1]['name']}")

    rooms[1]['name'] = 'PartyRoom!'
    save_inventory('changes_testing.json', rooms)
    new_file = load_inventory('changes_testing.json')

    print(f"Altered room name: {new_file[1]['name']}")
    

def load_inventory(filename):
    """Safely attempts to open the specified filepath, returning either the JSON file or an empty list. """
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("!! File not found !! Returning empty... ", end="")
    except json.JSONDecodeError:
        print("!! File corrupted !! Returning empty... ", end="")
    return []

def save_inventory(filename, data):
    print("Attempting to save data... ")
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
        print("Data saved!")

if __name__ == "__main__":
    main()
