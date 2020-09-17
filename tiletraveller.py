def north():
    position += 0.1

def west():
    position -= 1

def east():
    position += 1

def south():
    position -= 0.1

def invalid():
    print("Not a valid direction!")

def checkPos():
    if position == 1.1 or position == 2.1:
        north = True
        (east, south, west) = (False, False, False)
    elif position == 1.2:
        north, east, south = True
        west = False
    elif position == 1.3:
        east, south = True
        north, west = False
    elif position == 2.2 or position == 3.3:
        south, west = True
        north, east = False
    







north = True
south = False
west = False
east = False
victory = False
position = 1.1

print("You can travel:(N)orth.")
choice = input("Direction:").capitalize
while victory != True:
    checkPos()
    if position == 3.1:
        print("Victory!")
        victory = True
    if choice == "N":
        if north == True:
            north()
        else:
            invalid()
    elif choice == "E":
        if east == True:
            east()
        else:
            invalid()
    elif choice == "W":
        if west == True:
            west()
        else:
            invalid()
    elif choice == "S":
        if south == True:
            south()
        else:
            invalid()