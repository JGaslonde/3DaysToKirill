
from map import rooms
from items import *
from food import *
from player import *
from punctuation import *
import sys
import time

time_left = 72


def intro():
    """This function prints the introduction to the game when it is first loaded.
    Each line is delayed by a command of 2 seconds.
    """

    print("You are sitting in the Students Union lounge whilst watching TV...")
    time.sleep(2)
    print("when suddenly you see that Kirill has been kidnapped...")
    time.sleep(2)
    print("and without him around, you will never get the grade to progress in life.")
    time.sleep(2)


def list_of_items(items):
    """This function takes a list of items and returns a comma-separated list 
    of item names. For example:

    >>> list_of_items([item_key_1, item_key_2])
    'the 1st key, the 2nd key'

    >>> list_of_items([item_chloroform])
    'a bottle of chloroform'

    >>> list_of_items([])
    ''

    """

    return ", ".join([i['name'] for i in items])


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Cafeteria"])
    There is a salad, a cookie, a banana, a burger here.
    <BLANKLINE>

    >>> print_room_items(rooms["Library"])
    There is the 1st key here.
    <BLANKLINE>

    >>> print_room_items(rooms["Y-Plas"])

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
    You have a banana.
    <BLANKLINE>

    """
    if items:
        print("You have " + list_of_items(inventory) + ".")
        print()


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. The name of the room is printed in all capitals and 
    framed by blank lines. Then follows the description of the room and a 
    blank line again. If there are any items in the room, the list of items 
    is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Library"])
    <BLANKLINE>
    LIBRARY
    <BLANKLINE>
    Congratulations you found one of the places where Kirill 
    was before he was arrested, now you only have to take the key which 
    will be very important when you will reach Prison.
    <BLANKLINE>
    There is the 1st key here.
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

    >>> exit_leads_to(rooms["Students Union"]["exits"], "south")
    'Information Centre'
    >>> exit_leads_to(rooms["Hall"]["exits"], "east")
    'The Lounge'
    >>> exit_leads_to(rooms["The Taf"]["exits"], "west")
    'Support Centre'
    """

    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "the library")
    GO EAST to the library.
    >>> print_exit("south", "the students union")
    GO SOUTH to the students union.
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

    For example, the menu of actions available at the Taf may look like this:

    You can:
    GO WEST to the support centre.
    GO SOUTH to the students union.
    TAKE BURGER to take a burger.


    What do you want to do?
    """

    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))  
    print()

    # Iterate over available room items.
    for item in room_items:
        # Print the option to take each item.
        print("TAKE " + item["id"].upper() + " to take " + item["name"] + ".")
    
    if room_items != []:
        print()

    # Iterate over each item in the players inventory.
    for item in inv_items:
        # Print the option to drop each item.
        print("DROP " + item["id"].upper() + " to drop " + item["name"] + ".")
    
    if inv_items != []:
        print()

    # Iterate over each item in the food inventory.
    for food in food_items:
        if food in inventory:
        # Print the option to eat each item.
            print("EAT " + food["id"].upper() + " to eat " + food["name"] + ".")
    
    if food_items != []:
        print()
    
    # Iterate over each food in the room items.
    for food in room_items:
        if food in food_items and room_items:
            # Print the option to buy each item.
            print("BUY " + food["id"].upper() + " to buy " + food["name"] + " for £" + str(food["cost"]) + ".")

    if room_items != []:
        print()

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Students Union"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Students Union"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["The Lounge"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Hall"]["exits"], "east")
    True
    """

    return chosen_exit in exits


def calculate_time():
    """This function calculates how much time the player has left to complete the game.
    Each time the player moves to a room, the counter decrements by 1.
    """
    global time_left
    time_left -= 1
    
    return time_left


def calculate_hunger():
    """This function calcluates the hunger off player each time they move between rooms.
    The player's hunger will decrease by 5 each time they move between rooms.
    """
    
    player["hunger"] -= 5
    
    if player["hunger"] < 0:
        player["hunger"] = 0

    return player["hunger"]


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


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). This function also will call the calculate_hunger() and 
    calculate_time() functions which will reduce the hunger of the player
    and reduce the time to complete the game each time they move rooms. 
    Otherwise, it prints "You cannot go there."
    """

    global current_room

    if direction in current_room["exits"]:            
            current_room = move(current_room["exits"], direction)
            calculate_hunger()
            calculate_time()
            return current_room
    else:
        print("You cannot go there.")


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. If the item the player
    is trying to take is a food item, then outro(3) is called which ends the game for 
    stealing. However, if there is no such item in the room, this function prints
    "You cannot take that."
    """

    # If there is no items in the current room display said message.
    if not (current_room["items"]):
        print("There is nothing here to take")
    else:    
        for item in current_room["items"]:
            # If there are items in the current room and it matches the players input:
            if item["id"] == item_id:
                # Call the outro function if the item in question is a food item.
                if item in food:
                    outro(3)
                else:
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
    """This function takes a food_item as an argument and removes this item from
    the player's inventory and adds the value of the food_item to the player's health.
    If no such item exist in the player's inventory, then the function prints, 
    "You cannot eat that." 
    """

    # If there is nothing in inventory display said message.
    if not (inventory):
        print("You have nothing to eat!")
    else: 
        for food in inventory:
            # If there are items in the inventory and it matches the players input:
            if food["id"] == food_item:
                # Remove from inventory and add the hunger value of the food to the hunger of the player.
                inventory.remove(food)
                player["hunger"] += food["hunger"]
                # Set the hunger to a maximum of 100 not matter how much food is consummed.
                if player["hunger"] > 100:
                    player["hunger"] = 100
                # Print the description of the food and return the new value of the hunger.
                print(food["description"])
                return player["hunger"]

        if food_item not in (food["id"]):
            # If there items in the inventory, but the input does not match any of them, print said message.
            print("You cannot eat that item")


def execute_buy(food_item):
    """This function takes a food_item as an argument and first checks if the player
    is in the rooms where food and then checks if the player has enough money. If so, 
    then the cost of the item is removed from the player's money. If not, then the function 
    prints, "You don't have enough money to buy that." 
    """
    # Check if the current room is the only rooms assigned with food items.
    if current_room == rooms["Cafeteria"] or rooms["The Taf"] or rooms["Starbucks Coffee"]:
        for food in current_room["items"]:
            # For the FOOD that the food the player wants to buy.
            if food["id"] == food_item:
                # Check if there is enough money to buy it.
                if player["money"] >= food["cost"]:
                    # Add to player's inventory.
                    inventory.append(food)
                    # Subtract cost from money.
                    player["money"] -= food["cost"]
                    return player["money"]
                else:
                    print("You do not have enough money to buy that.")
    else:
        print("There is nothing to buy here.")


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", "drop", or "buy"), executes either execute_go,
    execute_take, execute_drop, or execute_buy, supplying the second word as 
    the argument.
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

    elif command[0] == "buy":
        if len(command) > 1:
            execute_buy(command[1])
        else:
            print("Buy what?")
    
    elif command[0] == "exit":
        execute_exit()

    elif command[0] == "win":
        win()

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

    >>> move(rooms["Students Union"]["exits"], "south") == rooms["Information Centre"]
    True
    >>> move(rooms["Students Union"]["exits"], "east") == rooms["Support Centre"]
    True
    >>> move(rooms["Students Union"]["exits"], "west") == rooms["Y-Plas"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


def bad_room_health():
    """This function determines if the room the player is in a bad room, in which they will
    lose health everytime they are in that room.
    """

    if current_room["Bad Room"] == True:
        player["health"] -= 15

    return player["health"]


def lose():
    """This function is only active when the player has either run out of time or 
    their health reaches zero. In each case a outro runs.
    """
    if(time_left == 0):

        print("And so, as you have so valiantly tried, alas... ")
        time.sleep(2)
        print("You have run out of time. Kirill is trapped...")
        time.sleep(2)
        print("and you will never get a good grade...")
        time.sleep(2)
        print("maybe you should work harder next time instead of playing video games.")
        sys.exit()

    elif(alive(player["health"])) == False:

        print("And so, as you have so valiantly tried, alas... ")
        time.sleep(2)
        print("You have died. Kirill is trapped...")
        time.sleep(2)
        print("and you will never get a good grade...")
        time.sleep(2)
        print("maybe you should work harder next time instead of playing games.")
        sys.exit()


def alive(health):
    """This function takes the player's health as an argument and checks if the 
    health is 0. If so then the function will return that the player is dead and
    the game is over. 

    >>> alive(10)
    True
    >>> alive(0)
    False
    >>> alive(-10)
    False
    """

    if health <= 0:
        return False
    else: 
        return True


def legit_win():
    """This function defines the winning condition of the game. Once the winning
    conditions have been met. The choice() function is run to get an ending. 
    """
    if item_key_1 in rooms["Prison"]["items"]:
        if item_key_2 in rooms["Prison"]["items"]:
            if item_chloroform in rooms["Prison"]["items"]:
                print("With all the keys and the chloroform located inside the prison...")
                print()
                time.sleep(2)
                print("you free Kirill? ")
                print()
                choice()


def choice():
    """This function gives the player an option as the end of the game if they really
    want to free Kirill. No matter if they say yes or no, they are asked to confirm 
    their decision. Depending on their final decision will depend on which outro they get.  
    """

    print("Now that you have all the items required to free Kirill...")
    print()
    time.sleep(2)
    print("do you really want to free him?")
    time.sleep(2)
    print("I mean, do you really want the grade? can you be sure he will")
    print()
    print("give the grade to you after you free him?")
    time.sleep(2)
    print("Will freeing him from a prison even matter towards your grade?")
    print()
    print("What do you say? Do you want to free Kirill or not? Yes or No?")
    time.sleep(2)
   
    while True:
        answer = input("> ")
        if answer == "yes":
            outro(1)
        
        elif answer == "no":
            outro(2)

        else:
            print("Try again")


def outro(value):
    """This displays an outro of the game depending on what value is entered into
    this function.
    """
    # Value executes in choice()
    if value == 1:
        print("Congrats!, You managed to free Kirill in under 3 days")
        sys.exit()
    
    # Value executes in choice()
    elif value == 2:
        print("Well fine then. Now you will never get the grade")
        sys.exit()
    
    # Value executes in execute_take()
    elif value == 3:
        print("You get caught taking an item without paying for it.")
        time.sleep(2)
        print("You are sent to prison...where you see Kirill...")
        time.sleep(2)
        print("...and soap...")
        time.sleep(4)
        print("THE IRONY")
        sys.exit()


def arrested():
    """This function checks if the player has the item_guard_outfit in order to get into 
    the prison. If they do not have it, they are sent back to the student union.
    """

    global current_room
    if ((current_room == rooms["Prison"]) and (item_guard_outfit not in inventory)):
        print("You are not supossed to be here go back to the student union")
        current_room = rooms["Students Union"]
        time_left -= 20
        inventory = []

        return current_room


def execute_exit():
    """This function simplely creates an exit from the program."""
    # Exit the game.
    sys.exit()


def win():
    """This is a cheat way to win the game...only if the code is known.
    (see execute_command() for command)"""
    # Cheat way to win the game.
    print("Congrats you win, cheat")
    sys.exit()


# This is the entry point of the program
def main():
    # First run the intro to start the game.
    intro()
    # Main game loop
    while True:

        # Check if current room is "bad" room in order to decrease health.
        bad_room_health()

        # Check if the player's health or time is zero in order to call function.
        lose()

        print("-------------------------------------------------------------------------------")
        # Display game status (room description, inventory, hunger, health, etc.)
        print_room(current_room)
        print_inventory_items(inventory)
        print("Your health is: " + str(player["health"]))
        print("You have " + str(time_left) + " hours left")
        print("You have £" + str(player["money"]))
        # Display hunger of player.
        hunger()
        print()

        # If not, show the menu with possible actions and ask the player what to do next.
        command = menu(current_room["exits"], current_room["items"], inventory, food)

        # Execute the player's command
        execute_command(command)

        # Check if the player can be in the prison and has the necessary items.
        arrested()

        # Check if player has won the game. 
        legit_win()


# If we are running as a script, execute main function.
if __name__ == "__main__": 
    main()
