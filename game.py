
from map import rooms
from items import *
from food import *
from player import *
from punctuation import *
import sys
import time

time_left = 72

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    return ", ".join([i['name'] for i in items])


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Student Union"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    """
    if room["items"]:
        print("There is " + list_of_items(room["items"]) + " here.")
        print()


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    if items:
        print("You have " + list_of_items(inventory) + ".")
        print()


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE HALLWAY
    <BLANKLINE>
    DESCRIPTION HERE.
    <BLANKLINE>
    ANY ITEMS.
    <BLANKLINE>
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)


def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items, food_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    # Iterate over available room items.
    for item in room_items:
        # Print the option to take each item.
        print("TAKE " + item["id"].upper() + " to take " + item["name"] + ".")
    # Iterate over each item in the players inventory.
    for item in inv_items:
        # Print the option to drop each item.
        print("DROP " + item["id"].upper() + " to drop your " + item["name"] + ".")
    # Iterate over each item in the food inventory.
    for food in food_items:
        if food in inventory:
        # Print the option to eat each item.
            print("EAT " + food["id"].upper() + " to eat " + food["name"] + ".")
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    # If the direction the user input is in the exits dictionary, return True, else return False.
    global current_room
    if direction in current_room["exits"]:            
            current_room = move(current_room["exits"], direction)
            calculate_hunger()
            time_left()
            return current_room
    else:
        print("You cannot go there.")


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    # If there is no items in the current room display said message.
    if not (current_room["items"]):
        print("There is nothing here to take")
    else:    
        for item in current_room["items"]:
            # If there are items in the current room and it matches the players input:
            if item["id"] == item_id:
                # Remove from the current room and add to the inventory list of items.
                current_room["items"].remove(item)
                inventory.append(item)
                break

        if item_id not in (item["id"]):
            # If there items in the current room, but the input does not match any of them, print said message.
            print("You cannot take that item!")

        
def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    # If there is nothing in inventory display said message.
    if not (inventory):
        print("You have nothing to drop!")
    else: 
        for item in inventory:
            # If there are items in the inventory and it matches the players input:
            if item["id"] == item_id:
                # Remove from inventory and add to the current rooms list of items.
                inventory.remove(item)
                current_room["items"].append(item)
                break

        if item_id not in (item["id"]):
            # If there items in the inventory, but the input does not match any of them, print said message.
            print("You cannot drop that item")


def execute_eat(food_item):
    """This function takes an food_item as an argument and removes this item from
    the player's inventory and adds the value of the food_item to the player's health.
    If no such items exist in the player's inventory, then the function prints, 
    "You cannot eat that." 
    """
    # If there is nothing in inventory display said message.
    if not (inventory):
        print("You have nothing to eat!")
    else: 
        for food in inventory:
            # If there are items in the inventory and it matches the players input:
            if food["id"] == food_item:
                # Remove from inventory and add to the current rooms list of items.
                inventory.remove(food)
                player["hunger"] = 100
                print(food["description"])
                break

        if food_item not in (food["id"]):
            # If there items in the inventory, but the input does not match any of them, print said message.
            print("You cannot eat that item")
     

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "eat":
        if len(command) > 1:
            execute_eat(command[1])
        else:
            print("Eat what?")
    
    elif command[0] == "exit":
        execute_exit()

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items, food_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.
    """

    # Display menu
    print_menu(exits, room_items, inv_items, food_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


def final_boss():
    """This function determines if the player has all the necessary items in
    order to progress to the final room.
    """
    pass


def win():
    """This function defines the winning condition of the game. Once the winning
    conditions have been met. The player wins the game. 
    """
    pass


def hunger():
    """This function prints the hunger of the player each time they move between rooms.
    If the player's health is 0 or lower, print a message telling the player to eat 
    soon or they will starve as this function will also decrease the players health by
    10.
    """
    print("Your hunger is: " + str(player["hunger"]))

    if player["hunger"] == 0:
        print("Get food quick or you will starve.")
        player["health"] -= 10
        print()


def calculate_hunger():
    """This function calcluates the hunger off player each time they move between rooms.
    The player's health will decrease by 5 each time they move between rooms.
    """
    
    player["hunger"] -= 5
    
    if player["hunger"] < 0:
        player["hunger"] = 0

    return player["hunger"]


def calculate_health():
    if current_room["Bad Rooms"] == True:
        player["health"] -= 15

#ADD BATTLE SHIT HERE


def alive(health):
    """This function takes the player's health as an argument and checks if the 
    health is 0. If so then the function will return that the player is dead and
    the game is over. 

    >>> alive(10):
    True
    >>> alive(0):
    False
    >>> alive(-10):
    False
    """
    if health <= 0:
        return False


def intro():
    print("You are sitting in the Students Union lounge whilst watching TV...")
    time.sleep(3)
    print("...when suddenly you see that Kirill has been kidnapped...")
    time.sleep(3)
    print("...and without him around, you will never stuff... ")


# This is the entry point of our program
def main():
    intro()
    # Main game loop
    while True:
        # Display game status (room description, inventory, hunger, health, etc.)
        print("---------------------------------------------------")
        print_room(current_room)
        print_inventory_items(inventory)
        # Check if the player has won the game.
        hunger()
        alive(player["health"])
        print("Your health is: " + str(player["health"]))
        print("You have " + str(time_left) + " hours left")
        print()
        # If not, show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory, food)

        # Execute the player's command
        execute_command(command)

        
def execute_exit():
    # Exit the game.
    sys.exit()


def win():
    # Cheat way to win the game.
    print("Congrats you win, cheat")
    sys.exit()

def time_left():
    time_left -= 1
    return time_left


# If we are running as a script, execute main function.
if __name__ == "__main__":
    main()
