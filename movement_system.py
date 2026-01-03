from locked_system import Locked_system
from locked_system import test
from file_management import load_file

coordiantes = [0,0]  #just for testing remove when using in final program
index = 0 

# gets the index of the room
data = load_file('testrooms.json')
while data["Rooms"][index]["gridpos"] != coordiantes:
    index = index + 1


def Movementsystem(coords):
    direction= input("you are able to move north, south, east or west. where do you want to move? ").strip() #ask user where they want to move
    
    '''Moves the player in the specified direction by updating their coordinates based on their inputs.
    Returns the updated coordinates after movement to the main program.'''
    if direction == "north":
        direction = 0
        possible = Locked_system(index,direction, data)
        if possible == True:
            coords[1] = coords[1] + 1
            print("you move north")

    elif direction[1] == "south":
        direction = 2
        possible = Locked_system(index,direction, data)
        if possible == True:
            coords = coords[1] - 1
            print("you move south")
    
    elif direction[0] == "east":
        direction = 1
        possible = Locked_system(index,direction, data)
        if possible == True:
            coords = coords[0] - 1
            print("you move east")
    elif direction[0] == "west":
        direction = 4
        possible = Locked_system(index,direction, data)
        if possible == True: 
            coords = coords[0] + 1
            print("you move west")
    else:
        print("not a valid movement option") 
    return (coords)


#just for testing remove when using in final program
coordiantes = Movementsystem(coordiantes)
print(coordiantes)

test(data)

