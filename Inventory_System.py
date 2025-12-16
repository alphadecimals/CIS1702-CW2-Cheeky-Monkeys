Inventory = []

def TakeFrom(Container, Item):
    Container["contains"] = "None"
    Inventory.append(Item["ID"])
def UsedUp(Item):
    Inventory.remove(Item["ID"])