# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 03:17:04 2015

@author: Evilija
"""

room_students_union = {
    "name": "Students_Union",

    "description":
    """You are sitting in the Students Union lounge while in TV you saw that the best teacher in all Computer Science School
    is arrested and kept in a basement with two metal doors, which have to be open by using TWO KEYS and
    THE BOTTLE OF CHLOROFORM, in order to make very strict guardian to be inactive this time """

    "exits": {"west": "Matt_OFFice","south": "Information_Centre","north": "GP","east": "Support_Centre"},

    "items": []
}


room_info_centre = {
    "name": "Information_Centre",

    "description":
    """ You reach Information Centre where you can find out the reasons of the kidnapping and take some snacks""",

    "exits": {"west": "Magistrate_Courts", "east": "Students_Union_Hall"},

    "items": [burger]

}


room_Hall = {
    "name": "Students_Union_Hall",

    "description":
    """ Now you are standing in one of the Students Union halls full of wires which are like snakes 
    who wants to take your food and waste your energy in order to make you slower.
    Make sure you won't be doing the same mistake again""",

    "exits": {"east": "The_Lounge", "west":"Information_Centre", "south": "Prison_Basament"},

    "items": []

}


room_Lounge = {
    "name": "The_Lounge",

    "description":
    """ Now you can take a rest because this room is the safest place in Students Union.
    So look around and make sure you find out everything that is related with Kirill last visited places
    as one of them should be somewhere close, make sure you do not miss that place""",

    "exits": {"north": "Library", "south": "Students_Union_Hall"},

    "items": []

}


room_Library = {
    "name": "Library",

    "description":
    """ Congratulations you found one of the places where Kirill was before kidnapping,
    now you only have to take the key which will be very important when you will reach Prison""",

    "exits": {"north": "Y_Plas", "south": "The_Lounge", "west":"The_Taf"},

    "items": [key_1]

}


room_Taf = {
    "name": "The_Taff",

    "description":
    """ You are choosing the best ways to escape, keep doing it till the end.
    And make sure you have enough health to finish the game.""",

    "exits": {"south": "Students_Union_Hall", "west": "Support_Centre"},

    "items": [banana]

}


room_Plas = {
    "name": "Y_Plas",

    "description":
    """Oh, that is bad...
    Now you are going to be attacked by the drunkest students in the  world
    which are more similar to zombies than to students... 
    I believe IT WILL TAKE A WHILE to make them inactive """,

    "exits": {"east": "Library","west": "Support_Centre"},

    "items": []

}


room_Support = {
    "name": "Support_Center",

    "description":
    """ You are getting lucky!!!
    Now you are able to get answers in most important questions:
    1. There is four bad rooms which make slower so make sure you won't be going there
    2. There is no way out of prison without Keys and Chloroform, make sure you collect everything before going there""",

    "exits": {"north": "Y_Plas","east": "The_Taf", "west":"GP"},
    "items": []

}


room_GP = {
    "name": "GP",

    "description":
    """Lucky enough to find one more item needed to release your teacher.
    Keep looking around and make sure you choice the best way out """,

    "exits": {"west": "Trevithick_Library","east": "Support_Centre", "south":"Lab2"},

    "items": [Chloroform]

}


room_Lab2 = {
    "name": "Lab2",

    "description":
    """Now you will see that our computers are doing after work:
    you will have to fight if you doesn't want to be eaten by them
    because they have very sharp teeth and very strong and long tales 
    which are moving very fast in order to make you SLOVER AND MORE HARMFUL""",

    "exits": {"north": "GP", "south":"Kirill_Office"},

    "items": []

}


room_Trevithick= {
    "name": "Trevithick_Library",

    "description":
    """ Now you are able to know that Kirill was in one of these offices:
    Kirill Office or Matt Office, 
    but which one you have to choice by yourself, 
    just make sure you make the right choice 
    because you are surounded by Bad rooms in both ways  """,

    "exits": {"west": "Cafeteria","east": "GP", "south":"Lab2"},

    "items": []

}


room_Cafeteria = {
    "name": "Cafeteria",

    "description":
    """ Yay!!!
    You found the place full of food,
    just choice whatever you want and 
    make yourself healthier """,

    "exits": {"east": "Matt_Office", "south":"Kirill_Office"},

    "items": [salad]

}


room_KOffice = {
    "name": "Kirill_Office",

    "description":
    """ You are lucky enough to choice the best rooms ever!
    Now you have to find the Key 
    which will be the most important thing 
    when you will reach Prison.
    Keep hurry, time is going to end""",

    "exits": {"north": "Cafeteria","east": "Lab2", "south":"Starbucks_Coffe"},

    "items": [Key_2]

}


room_Starbucks = {
    "name": "Starbucks_Cofee",

    "description":
    """ You found the most expensive and the strongest coffee ever:
    Just choice the food you want and keep going! """,

    "exits": {"north": "Kirill_Office","east": "Magistrate_Courts"},

    "items": [kebab]

}


room_MOffice = {
    "name": "Matt_Office",

    "description":
    """ Oh, that is horrible!
    All room is destroyed by monster 
    which is coming after you now.
    Make sure you have enough strenght to fight him
    And enough time to reach Kirill""",

    "exits": {"east": "Magistrate_Courts", "south":"Starbucks_Coffe"},

    "items": []

}


room_Courts = {
    "name": "Magistrate_Courts",

    "description":
    """ FANTASTIC!
    Now you are able to know in which cell they are keeping Kirill
    and the best time to use Chloroform against guardian.
    Just keep going!!! """,

    "exits": {"north": "Matt_Office","east": "Prison_Basament"},

    "items": []

}


room_Prison = {
    "name": "Prison_Basament",

    "description":
    """Congratulations!!!!
    You already reached Kirill
    Everything you need to do now
    Is just to use CHLOROFORM against guardian
    And TWO KEYS to Unlock the doors""",

    "exits": {},

    "items": [Key_1, Key_2, Chloroform]

}