coordiantes = [0,0]  #just for testing remove when using in final program


def Movementsystem(coords):
    direction= input("you are able to move north, south, east or west. where do you want to move") #ask user where they want to move
    
    '''Moves the player in the specified direction by updating their coordinates based on their inputs.
    Returns the updated coordinates after movement to the main program.'''
    if direction == "north":
        coords[1] = coords[1] + 1
        print("you move north")
    elif direction[1] == "south":
        coords = coords[1] - 1
        print("you move south")
    elif direction[0] == "east":
        coords = coords[0] - 1
        print("you move east")
    elif direction[0] == "west": 
        coords = coords[0] + 1
        print("you move west")
    else:
        print("not a valid movement option") 
    return (coords)


#just for testing remove when using in final program
coordiantes = Movementsystem(coordiantes)
print(coordiantes)

