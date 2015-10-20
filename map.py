from items import *


room_Students_Union = {
    "name": "Students Union",

    "description":
    """You are sitting in the Students Union lounge while in TV you saw that 
the best teacher in all Computer Science School is arrested and kept in a 
basement with two metal doors, which have to be open by using TWO KEYS and
THE BOTTLE OF CHLOROFORM, in order to make very strict guardian to be inactive 
this time """,

    "exits": {"west": "Matt Office", "south": "Information Centre", "north": "GP", "east": "Support Centre"},

    "items": []
}


room_Info_Centre = {
    "name": "Information Centre",

    "description":
    """You reach Information Centre where you can find out the reasons of the 
kidnapping and take some snacks""",

    "exits": {"west": "Courts", "east": "Students Union"},

    "items": [food_burger]

}


room_Hall = {
    "name": "Students Union Hall",

    "description":
    """Now you are standing in one of the Students Union halls full of wires
which are like snakes who wants to take your food and waste your energy in 
order to make you slower. Make sure you won't be doing the same mistake again""",

    "exits": {"east": "The Lounge", "west": "Information Centre", "south": "Prison"},

    "items": []

}


room_Lounge = {
    "name": "The Lounge",

    "description":
    """Now you can take a rest because this room is the safest place in 
Students Union. So look around and make sure you find out everything that 
is related with Kirill last visited places as one of them should be 
somewhere close, make sure you do not miss that place""",

    "exits": {"north": "Library", "south": "Students Union"},

    "items": []

}


room_Library = {
    "name": "Library",

    "description":
    """Congratulations you found one of the places where Kirill was before kidnapping,
now you only have to take the key which will be very important when you will reach Prison""",

    "exits": {"north": "Y-Plas", "south": "The Lounge", "west": "The Taf"},

    "items": [item_key_1]

}


room_Taf = {
    "name": "The Taf",

    "description":
    """ You are choosing the best ways to escape, keep doing it till the end.
And make sure you have enough health to finish the game.""",

    "exits": {"south": "Students Union", "west": "Support Centre"},

    "items": [food_banana]

}


room_Plas = {
    "name": "Y Plas",

    "description":
    """Oh, that is bad...
    Now you are going to be attacked by the drunkest students in the world
which are more similar to zombies than to students... 
I believe IT WILL TAKE A WHILE to make them inactive """,

    "exits": {"east": "Library", "west": "Support Centre"},

    "items": []

}


room_Support = {
    "name": "Support Centre",

    "description":
    """ You are getting lucky!!!
Now you are able to get answers in most important questions:
1. There is four bad rooms which make slower so make sure you won't be going 
there
2. There is no way out of prison without Keys and Chloroform, make sure you 
collect everything before going there""",

    "exits": {"north": "Y-Plas", "east": "The Taf", "west": "GP"},
    "items": []

}


room_GP = {
    "name": "GP",

    "description":
    """Lucky enough to find one more item needed to release your teacher.
Keep looking around and make sure you choice the best way out """,

    "exits": {"west": "Trevithick Library", "east": "Support Centre", "south": "Lab 2"},

    "items": []

}


room_Lab2 = {
    "name": "Lab 2",

    "description":
    """Now you will see that our computers are doing after work:
you will have to fight if you doesn't want to be eaten by them
because they have very sharp teeth and very strong and long tales 
which are moving very fast in order to make you SLOVER AND MORE HARMFUL""",

    "exits": {"north": "GP", "south": "Kirill Office"},

    "items": []

}


room_Trevithick = {
    "name": "Trevithick Library",

    "description":
    """Now you are able to know that Kirill was in one of these offices:
Kirill Office or Matt Office, but which one you have to choice by yourself, 
just make sure you make the right choice because you are surounded 
by Bad rooms in both ways""",

    "exits": {"west": "Cafeteria", "east": "GP", "south": "Lab 2"},

    "items": []

}


room_Cafeteria = {
    "name": "Cafeteria",

    "description":
    """Yay!!!
You found the place full of food, just choice whatever you want and 
make yourself healthier""",

    "exits": {"east": "Matt Office", "south": "Kirill Office"},

    "items": [food_salad]

}


room_KOffice = {
    "name": "Kirill Office",

    "description":
    """ You are lucky enough to choice the best rooms ever!
Now you have to find the Key which will be the most important thing 
when you will reach Prison. Keep hurry, time is going to end""",

    "exits": {"north": "Cafeteria", "east": "Lab 2", "south": "Starbucks Coffee"},

    "items": [item_key_2]

}


room_Starbucks = {
    "name": "Starbucks Coffee",

    "description":
    """ You found the most expensive and the strongest coffee ever:
Just choice the food you want and keep going! """,

    "exits": {"north": "Kirill Office", "east": "Courts"},

    "items": [food_kebab] 

}


room_MOffice = {
    "name": "Matt Office",

    "description":
    """ Oh, that is horrible!
All room is destroyed by monster which is coming after you now.
Make sure you have enough strenght to fight him
And enough time to reach Kirill""",

    "exits": {"east": "Courts", "south": "Starbucks Coffee"},

    "items": []

}


room_Courts = {
    "name": "Magistrate Courts",

    "description":
    """ FANTASTIC! 
Now you are able to know in which cell they are keeping Kirill and 
the best time to use Chloroform against guardian. Just keep going!!! """,

    "exits": {"north": "Matt Office", "east": "Prison"},

    "items": []

}


room_Prison = {
    "name": "Prison Basament",

    "description":
    """Congratulations!!!!
You already reached Kirill Everything you need to do now
Is just to use CHLOROFORM against guardian 
And TWO KEYS to Unlock the doors""",

    "exits": {},

    "items": []

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