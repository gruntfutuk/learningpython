def intro():
    print("""
Welcome to Coffee Run!

You wake up at a local tavern the day after a long adventure. After such a perilous journey you could really use a strong cup of coffee.

To your dismay the innkeeper regretfully informs you that the bag of coffee beans has been possessed by an evil spirit turning it into a Coffee Monster!

In order to defeat the spirit keeping you from the dark elixir you need to kick-start your day:

You will need to gather 6 items from throughout the tavern to help you in your battle.

Possible movements are: North, South, East, and West

To view your currently held items, type "Inventory"

To take an item: type "get"

To quit the game, enter quit

"""

def setup():
    inventory = []
    directions = ["north", "south", "east", "west"]
    rooms = {
        "Great Room": {
            "Name": "Great Room",
            "east": "Bar",
            "south": "Kitchen",
            "west": "Tavernkeepers Room",
            "north": "Library",
            "stuff": [],
            "Description": "A Great Room: Many travelers have spent time here \nA Bar lies to the East, the Kitchen is to the South, the Tavernkeepers Room is to the West, and the Library is to the North",
        },
        "Tavernkeepers Room": {
            "Name": "Tavernkeepers Room",
            "east": "Great Room",
            "stuff": ["Coffeemaker"],
            "Description": "The Tavernkeepers Room. The host is known to have the best equipment to brew some coffee. \nThe Great Room is to the East",
        },
        "Kitchen": {
            "Name": "Kitchen",
            "north": "Great Room",
            "east": "Pantry",
            "stuff": ["Apron"],
            "Description": "The Kitchen: Whether looking to make a drink or some food, this is where you want to be.Surely something of use can be found here. \nThe Great Room lies to the North, and the Pantry lies to the East",
        },
        "Pantry": {
            "Name": "Pantry",
            "west": "Kitchen",
            "stuff": ["Sugar"],
            "Description": "The Pantry: The best place to find condiments. \nThe Kitchen is to the west",
        },
        "Storage Closet": {
            "Name": "Storage Closet",
            "east": "Library",
            "stuff": ["Filter"],
            "Description": "The Storage Closet...maybe something is on the shelf. \nThe Library is to the East",
        },
        "Parlour": {
            "Name": "Parlour",
            "west": "Library",
            "Description": "The Parlour, The Coffee Monster is here!",
        },
        "Bar": {
            "Name": "Bar",
            "west": "Great Room",
            "stuff": ["Stirrer"],
            "Description": "The Bar: A lot of tools here could be useful for making coffee. \nThe Great Room is to the West",
        },
        "Library": {
            "Name": "Library",
            "south": "Great Room",
            "west": "Storage Closet",
            "east": "Parlour",
            "stuff": ["Grinder"],
            "Description": "The Library: A lot of equipment is displayed on top of bookcases. \nThe Great Room is to the South, the Storage Closet is to the West "
            "and the overwhelming scent of Coffee is coming from the Parlour to the East",
        },
    }
    return inventory, directions, rooms

def status():
    print('\nYou are in the {current_location["Name"]}.\n')
    print(current_location["Description"])
    if current_location["stuff"]:
    print('Looking around the room you see a(n) {", ".join(current_location["stuff"]}')

inventory, directions, rooms = setup()
current_location = rooms["Great Room"]
look = current_location["stuff"]

while True:
    status()
    
    player_move = input(
        "\nWhat do you want to do?"
    ).strip()  # get movement input from user
    if player_move in directions:  # wcheck validity from directions list
        if player_move.lower() in current_location:  # check values
            current_location = rooms[current_location[player_move]]
        else:  # if movement not possible
            print("\n OUCH! You bump into a wall. Try another direction.")
    elif player_move.lower() in ("quit"):  # if input is quit
        print("You have exited the game.")
        break
    elif player_move.lower() in ("get"):  # user input to pick up item
        item = (
            input("What would you like to get?").split()[-1].capitalize()
        )  # user specifies item to pick up
        if item in current_location["stuff"]:  # check if item in current room
            current_location["stuff"].remove(item)  # remove item from room
            inventory.append(item)  # add to user inventory
        else:
            print("That item isn't here!")  # if item not in current location item pool
    elif player_move.lower() in ("inventory"):  # if input is inventory
        print("You currently have:")
        print(" ".join(inventory))  # print current items
    elif player_move.lower() in ("look"):  # check items in current room
        print("Looking around you see:")
        print(current_location["stuff"])  # return result of items in room
    elif len(inventory) == 6:
        print(
            "You have collected all the items to defeat the Coffee Monster! You head to the Parlour and brew up some liquid relaxation."
        )
        break
    else:  # what to do if input is not valid
        print("Invalid Entry")

intro()
