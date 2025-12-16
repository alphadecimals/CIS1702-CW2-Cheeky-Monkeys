coordiantes = [0,0] 


def Movementsystem(coords):
    direction= input("you are able to move north, south, east or west. where do you want to move") #ask user where they want to move
    #  updates the coordianted depending on their answer
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



coordiantes = Movementsystem(coordiantes)
print(coordiantes)
