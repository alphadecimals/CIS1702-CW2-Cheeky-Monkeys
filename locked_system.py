# Dummy inventory for testing
inventory = []

def Locked_system(room_index, direction_index, data):
    # gathers the room info
    sucess= False
    status=  data["Rooms"][room_index]["locked"][direction_index]
    key_needed = data["Rooms"][room_index]["unlockers"][direction_index]
    #checks if the room is locked
    if status == True:
        print("The door seems to be locked and needs ",key_needed," to be opened.")
        # check if you have the key and does the approiate response 
        if key_needed in inventory:
            print("You had the key and unlocked the door and moved through the door.")
            sucess = True
            data["Rooms"][room_index]["locked"][direction_index] = False  
        elif key_needed == "":
            print("You cannot go this way.")        
        else:
            print("You do not have this key yet and are unable to open this door.")
    
    else:
        print("You moved through the door.")
        sucess = True
        data["Rooms"][room_index]["locked"][direction_index] = False 
    return(sucess) 
        
# Example test
def test(data):
    room = 0        # room0
    direction = 0   # first direction

    test = Locked_system(room, direction, data)
    print("moved=", test)

