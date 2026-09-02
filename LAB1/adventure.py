"""
Name: 
Last updated: 
Description: 
"""

def adventure():
    """ This function runs one session of a choose your own adventure.
        Arguments: None
        Returns: None (Printed text is not returned)
    """

    print()

    print("Welcome, worthy adventurer, to The Swamp,")
    print("home to Ally the Golden Gator and sourdough bread!")

    print()

    player_name, player_class = create_player()

    print()
    
    if player_class == "Warrior":
        health = 100
        mana = 50
        print("A brave warrior, ready to confront any challenge.")
    elif player_class == "Mage":
        health = 50
        mana = 100
        print("A cunning mage, capable of outwitting the strongest foe.")
    else:
        health = 75
        mana = 75
        print("A unique specialty I do not recognize! Intriguing...")

    print()

    print("Here are your beginning stats:")
    print("Health: {}".format(health))
    print("Mana: {}".format(mana))

    print()

    print(player_name, "your quest is to rescue Ally from the Spartans")
    print("who hold her captive.")
    print("Let us begin...")

    print()

    # Add branches to the adventure here!

    return 0


def create_player():
    """ Prompts the user for their name and class.
        Arguments: None
        Returns:
            - player_name (string): Name of the player
            - player_class (string): Class of the player
    """

    player_name = input("Before we begin, what should I call you? ")
    player_class = input("What is your specialty? [Warrior / Mage] ")

    return player_name, player_class

win = 0
while win == 0:
    win = adventure()