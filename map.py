from items import *
from food import *


room_Students_Union = {
    "name": "Students Union",

    "description":
    """You are sitting in the Students Union lounge while on TV you see that 
your favourite lecturer in Computer Science has been arrested and is being
kept in Prison under high securitiy. There are two secure doors, which have 
to be opened by using TWO KEYS. You will also need something in order to
knock out the guard at the entrance""",

    "exits": {"west": "Matt Office", "south": "Information Centre", "north": "GP", "east": "Support Centre"},

    "items": [],

    "Bad Room": False
}


room_Info_Centre = {
    "name": "Information Centre",

    "description":
    """You are at the Information Centre, there are a few members of staff
discussing the arrest of Kirill. On the counter there is food.""",

    "exits": {"west": "Courts", "north": "Students Union"},

    "items": [],

    "Bad Room": False

}


room_Hall = {
    "name": "Students Union Hall",

    "description":
    """Now you are standing in one of the Students Union halls which is full of wires
which are like snakes who wants to take your food and waste your energy in 
order to make you slower. Make sure you won't be doing the same mistake again""",

    "exits": {"east": "The Lounge", "west": "Information Centre", "south": "Prison"},

    "items": [],

    "Bad Room": True

}


room_Lounge = {
    "name": "The Lounge",

    "description":
    """Now you can take a rest because this room is the safest place of the game. 
So look around and make sure you find out everything that is related with 
Kirill's last visited areas as one of them should give some clues.""",

    "exits": {"north": "Library", "south": "Students Union"},

    "items": [],

    "Bad Room": False

}


room_Library = {
    "name": "Library",

    "description":
    """Congratulations you found one of the places where Kirill 
was before he was arrested, now you only have to take the key which 
will be very important when you will reach Prison.""",

    "exits": {"north": "Y-Plas", "south": "The Lounge", "west": "The Taf"},

    "items": [item_key_1],

    "Bad Room": False

}


room_Taf = {
    "name": "The Taf",

    "description":
    """You are plotting the best way to help Kirill escape, keep doing this until the end.
Also make sure you have enough health to finish the game.""",

    "exits": {"south": "Students Union", "west": "Support Centre"},

    "items": [food_burger],

    "Bad Room": False

}


room_Plas = {
    "name": "Y-Plas",

    "description":
    """Oh, this is bad...
Now you are going to be attacked by the drunkest students you have ever
seen! They are like zombies! IT WILL TAKE A WHILE to get past these. """,

    "exits": {"east": "Library", "west": "Support Centre"},

    "items": [],

    "Bad Room": True

}


room_Support = {
    "name": "Support Centre",

    "description":
    """You are getting lucky!!!
You have recieved more information about where Kirill is being held. 
There is no way in or out of prison without the Two Keys AND Chloroform, make sure you 
collect everything before going there!""",

    "exits": {"north": "Y-Plas", "east": "The Taf", "west": "GP"},

    "items": [],

    "Bad Room": False

}


room_GP = {
    "name": "GP",

    "description":
    """You have reached the GP office. It is unsure why but there
is a bottle of Chloroform on the table, this may come in handy!""",

    "exits": {"west": "Trevithick Library", "east": "Support Centre", "south": "Lab 2"},

    "items": [item_chloroform],

    "Bad Room": False

}


room_Lab2 = {
    "name": "Lab 2",

    "description":
    """Something bad is happening in the lab!
The room has become infested with little bald ugly creatures which are
tearing appart the room and strangling students with cables!
This could potentially cause a fire hazard?
I wonder where the Health and Safety officer is...
You must fight your way through and get out quick!""",

    "exits": {"north": "GP", "south": "Kirill Office"},

    "items": [],

    "Bad Room": True

}


room_Trevithick = {
    "name": "Trevithick Library",

    "description":
    """Now you know that Kirill was in one of these offices:
Kirill's Office or Matt's Office, but which one? You will have to find out yourself, 
just make sure you make the right choice because you are surounded 
by Bad rooms in both ways""",

    "exits": {"west": "Cafeteria", "east": "GP", "south": "Lab 2"},

    "items": [],

    "Bad Room": False

}


room_Cafeteria = {
    "name": "Cafeteria",

    "description":
    """Yay!!!
You found the cafeteria which is full of food, just chose whatever you want to eat
when you're feeling hungry. You need to stay healthy to complete your mission!""",

    "exits": {"east": "Matt Office", "south": "Kirill Office"},

    "items": [food_salad, food_cookie, food_banana, food_burger],

    "Bad Room": False

}


room_KOffice = {
    "name": "Kirill Office",

    "description":
    """You are lucky enough to choice the best rooms ever!
Now you have to find the Key which will be the most important thing 
when you will reach Prison. Keep hurry, time is going to end""",

    "exits": {"north": "Cafeteria", "east": "Lab 2", "south": "Starbucks Coffee"},

    "items": [item_key_2],

    "Bad Room": False

}


room_Starbucks = {
    "name": "Starbucks Coffee",

    "description":
    """You found the most expensive and the strongest coffee ever.
There are also a few snacks here, can you really afford it?
Just choose the food you want and keep going! """,

    "exits": {"north": "Kirill Office", "east": "Courts"},

    "items": [food_cookie, food_banana],

    "Bad Room": False

}


room_MOffice = {
    "name": "Matt Office",

    "description":
    """Oh, that is horrible!
All room is destroyed by the same creatures from the lab!
Their attention is on you, they run at you as you panic!
Make sure you have enough strenght to fight them...
Do you really have time for this??""",

    "exits": {"east": "Courts", "south": "Starbucks Coffee"},

    "items": [],

    "Bad Room": True

}


room_Courts = {
    "name": "Magistrate Courts",

    "description":
    """FANTASTIC! You're nearly there.
Now you are able to find out in which cell they are keeping Kirill and 
the best time to use the Chloroform on the guard. Just keep going!!! """,

    "exits": {"north": "Matt Office", "east": "Prison"},

    "items": [item_guard_outfit],

    "Bad Room": False

}


room_Prison = {
    "name": "Prison",

    "description":
    """Congratulations!!!!
    
You have found Kirill.
All you need to do is knockout the guard and free Kirill
Use CHLOROFORM to knock him out and use the TWO KEYS to unlock the doors""",

    "exits": {},

    "items": [],

    "Bad Room": False

}


rooms = {
    "Students Union": room_Students_Union,
    "Information Centre": room_Info_Centre,
    "Hall": room_Hall,
    "The Lounge": room_Lounge,
    "Library": room_Library,
    "The Taf": room_Taf,
    "Y-Plas": room_Plas,
    "Support Centre": room_Support,
    "GP": room_GP,
    "Lab 2": room_Lab2,
    "Trevithick Library": room_Trevithick,
    "Cafeteria": room_Cafeteria,
    "Kirill Office": room_KOffice,
    "Starbucks Coffee": room_Starbucks,
    "Matt Office": room_MOffice,
    "Courts": room_Courts,
    "Prison": room_Prison

}