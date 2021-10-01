# Zombie Attack Component V2

import random
# materials used as placeholder as materials will have changed over the course of the game
materials = 50

def ZombieAttack():
    global materials
    # materials is base hp
    # global variable calls materials to be changed and updated through this function
    # Array contains the scenarios for zombie attacks with coresponding base damage

    # Each event has an equal chance of 25% to occur on any nights

    if random.random() < 0.25:
        # Base Attack Scenario 1
        # Base is not attacked at all

        base_hp_loss = 0
        materials = materials - base_hp_loss

        # Code prints damage taken and new base_hp
        print('The night was calm')
        print("The base was remained quiet")
        print("The base now has {} HP".format(materials))

    elif random.random() < 0.25:
        # Base Attack Scenario 2
        # Base is attacked 6 damage

        base_hp_loss = 6
        materials = materials - base_hp_loss

        # Code prints damage taken and new base_hp
        print('Some zombies attacked your base')
        print("The base was damaged {} HP".format(base_hp_loss))
        print("The base now has {} HP".format(materials))

    elif random.random() < 0.25:
        # Base Attack Scenario 3
        # Base is attacked 14 damage

        base_hp_loss = 14
        materials = materials - base_hp_loss

        # Code prints damage taken and new base_hp
        print('A group of zombies attacked your base')
        print("The base was damaged {} HP".format(base_hp_loss))
        print("The base now has {} HP".format(materials))

    else:
        # Base Attack Scenario 4
        # Base is attacked 24 damage

        base_hp_loss = 24
        materials = materials - base_hp_loss

        # Code prints damage taken and new base_hp
        print('Your base was surrounded in a horde of zombies')
        print("The base was damaged {} HP".format(base_hp_loss))
        print("The base now has {} HP".format(materials))

ZombieAttack()