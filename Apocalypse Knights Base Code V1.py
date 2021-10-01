# ApocK Base Code V1
import random

def IntroCard():
    print("\n\n")
    print("""    __________________________________________________________________________________________________________
    |                                                                                                        |
    |        "The critically acclaimed gaming masterpiece...                      / \                        |
    |          ___                             _                                  |.|                        |
    |         / _ \                           | |                                 |.|                        |
    |        / /_\ \ _ __    ___    ___  __ _ | | _   _  _ __   ___   ___         |.|                        |
    |        |  _  || '_ \  / _ \  / __|/ _` || || | | || '_ \ / __| / _ \        |:|     __                 |
    |        | | | || |_) || (_) || (__| (_| || || |_| || |_) |\__ \|  __/      ,_|:|_,  /  )                |
    |        \_| |_/| .__/  \___/  \___|\__,_||_| \__, || .__/ |___/ \___|        (Oo   / _I_                |
    |         _   __| |     _         _      _     __/ || |                        +\ \   || __|             |
    |        | | / /|_|    (_)       | |    | |   |___/ |_|                           \ \ ||___|             |
    |        | |/ /  _ __   _   __ _ | |__  | |_  ___                                   \ /.:.\-\            |
    |        |    \ | '_ \ | | / _` || '_ \ | __|/ __|                                   |.:. /-----\        |
    |        | |\  \| | | || || (_| || | | || |_ \__ \     "E" - Ryder G"EE"             |___|::oOo::|       |
    |        \_| \_/|_| |_||_| \__, ||_| |_| \__||___/                                   /   |:<_T_>:|       |
    |                           __/ |                      "NA" - Mr Cajita             |_____\ ::: /        |
    |                          |___/                                                      | |  \ \:/         |
    |                                                                                     | |   | |          |
    |    "Astounding gameplay depth" - IGN         "Breathtaking" - Leo Wang              \ /   | \___       |
    |                                                                                     / |   \_____\      | 
    |     By: Lance Valete         "Challenging and detailed" - E3 Gaming                 `-'                | 
    |________________________________________________________________________________________________________|""")
    
    print("\n")

def flippy(statement):
    play_again = input(statement).lower()
        
    if play_again == "":
            print()
            return
            
    else:
        play_again = input("Press <Enter> to continue...").lower()
    
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n": 
            response = "no"
            return response

        else:
            print("Please answer yes / no")

def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10"

    vaild = False
    while not vaild:
        try:
            response = int(input(question))

            if low < response <= high:
                return response
                
            else:
                print(error)

        except ValueError:
            print(error)

def instructions():
    print()
    print("How to Play Apocalpyse Knights")
    print("\nApocalpyse Knights is a story choices game where you must make")
    print("decisions to survive through the 5 days during a zombie")
    print("apocalypse and wait for a helicopter extraction from your stronghold.\n")
    print("You are an Apocalpyse Knight, part of the Templars a group created in")
    print("the future after the rise of the zombie pandemic devoted to defense and chivalry.")
    print("The player will start off with 10HP, 1 days worth of food and 50 Base HP\n")
    print("You the player must go out to scavenge for food to continue through the")
    print("days while encountering obstacles to overcome, balancing risk and")
    print("reward with losing health and or food to continue. In the town you can collect")
    print("wood and steel to increase your base's survivability. In the forest you can")
    print("find animals and wood to increase base health and food to continue.")
    print("During the night, zombies will come out to hunt you in your base,")
    print("and inflict damage depending on the size of the horde.")
    print("If you run out of food or Base HP, you will be overrun of starve.\n")
    print("In order tp survive the 5 days before extraction you must outlast")
    print("the five days through decisions making and risk taking or take the more")
    print("challenging route and try to buy your way out with the surviver traders")
    print("in their truck to the a safe haven at an expensive cost.\n")
    print("Press <enter> to continue\n")


    return ""

def IntroText():
        flippy("Dust, blood, darkness...")
        flippy("You lie amoungst the rubble of room")
        flippy("You emerge aching and sore, you look around")
        flippy("Destruction all around you...")
        print()
        flippy('"Hello...." you yell, but no response')
        flippy("Your soul feels heavy as you walk through the flames")
        flippy("The floor cold with blood, your memories are foggy")
        flippy("You wander outside to witness the damage...")
        flippy("Corpses litter the courtyard, charred beyond recognision")
        print()
        flippy('"What happened here? What happened to me?')
        flippy("Memories start coming back, your base, your name.")

        x = input('Enter your name: ')
        if x == "":
            x = input('Enter your name to continue: ')
        elif x != "":
                print()
        print('"My name is, {}"'.format(x))
        print()

        flippy("You walk to your base, you find weapons, some food and materials")
        flippy("You hear a buzz from your radio, you open the connection.")
        print()
        flippy('"Attention Templar Knight Survivors, a helicopter is coming to extract')
        flippy('you from the outpost, the helicopter will arrive in 5 days, please wait for us."')
        flippy("You now have one mission, survive until extraction.")

def town_forest(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "town" or response == "t":
            response = "town"
            return response

        elif response == "forest" or response == "f": 
            response = "forest"
            return response

        elif response == "back" or response == "b":
            response = "back"
            return response

        else:
            print("Please answer forest/f, town/t or back/b")

def ApocK_Database():
    global t_random_array_item
    global f_random_array_item
    global x
    global y
    global town_event
    global forest_event
    global forest_encounter
    global town_encounter
    global t_scav_run
    global f_scav_run
    global run
    hints_forest = {"1F": 'You see a horde wandering through the woods', "2F": 'You see the woods are eeirely empty',
                "3F": 'You see a few zombies around the woods', "4F": 'The woods are swallowed in an ocean of zombies'} 

    hints_town = {"1T": 'Smoke can be seen rising from the town', "2T": 'You hear screams from the town, this concerns you.',
                    "3T": 'You hear gunshots in the town', "4T": 'You see a horde going through the town'}

    forest_hints =['1F', '2F', '3F', '4F']
    town_hints = ['1T', '2T', '3T', '4T'] 
            
    t_random_array_item = random.choice(town_hints)
    f_random_array_item = random.choice(forest_hints)
    forest_current_hint = hints_forest[f_random_array_item]
    town_current_hint = hints_town[t_random_array_item]

    y = forest_current_hint
    x = town_current_hint

    t_scav_run = 0
    f_scav_run = 0

    town_encounter = {"1T": 'You spot a party of scavengers...\nThey seem friendly.\nOne says to you "We dont want any trouble"', 
                  "2T": 'You see a group of raiders robbing some scavengers.\nA man screams "Help us please!"',
                  "3T": 'You spot a gang of heavily armoured raiders.\nThey are killing scavengers.\nThey dont show mercy',
                  "4T": 'The town is filled with zombies.\nYou sneak carefully until you accidentilly hit one\n"Uh oh" you mutter.'}

    town_event =  town_encounter[t_random_array_item]

    forest_encounter = {"1F": 'You spot a medium sized horde...\nThey seem to docile.\nIf you sneak correctly you should be fine',
                        "2F": 'You get to forest to find no zombies?\nThings are going to well...',
                        "3F": 'You see a couple of zombies in the forest.\nYou should be able to kill them',
                        "4F": 'You arrive at the forest to find a huge horde engulf the forest'}

    forest_event = forest_encounter[f_random_array_item]

def scavenging():
    global food
    global materials
    
    if random.random() < 0.2:
        food_gain = 2
        material_gain = 20
        food = food + food_gain
        materials = materials + material_gain
        print('You found extra food and materials!')
        print('You obtain {} food and {} materials'.format(food_gain, material_gain))
        print('You now have {} food and {} materials.'.format(food, materials))

    elif random.random() < 0.2:
        food_gain = 0
        material_gain = 10
        food = food + food_gain
        materials = materials + material_gain
        print("\nYou didn't find much loot.")
        print('You obtain {} food and {} materials'.format(food_gain, material_gain))
        print('You now have {} food and {} materials.\n'.format(food, materials))

    else:
        food_gain = 1
        material_gain = 15
        food = food + food_gain
        materials = materials + material_gain
        print('You found food and materials')
        print('You obtain {} food and {} materials'.format(food_gain, material_gain))
        print('You now have {} food and {} materials.'.format(food, materials))
        
    
    return food, materials

def StatsChecker():
    global food
    global materials
    global player_hp
    global turn_counter
    global shop_escape
    global status

    if food > 0 and materials > 0 and player_hp > 0 and turn_counter < 5:
        print("normal")
        status = 'normal'

    # Losing scenarios
    elif food < 0:
        print("You starved to death...")
        print("Game Over")
        status = 'loss'

    elif materials <= 0:
        materials == 0
        print("Your base was destroyed by zombies...")
        print("Game Over")
        status = 'loss'


    elif player_hp <= 0:
        player_hp == 0
        print("You were killed by enemies...")
        print("Game Over")
        status = 'loss'

    #Winning scenarios
    elif turn_counter > 5:
        print("You survived the 5 days!")
        print("You Win")
        status = 'loss'

    elif shop_escape == 1:
        print("You payed passage to safety!")
        print("You Win")
        status = 'loss'

    return status

def BaseMenu():
    global run
    global status
    global player_hp
    global turn_counter
    ApocK_Database()
    player_info()
    while True:
        print("\nWhat do you want to do?")

        print('Enter 1 to Open Fridge\n')

        print('Enter 2 to check Base Defenses\n')

        print('Enter 3 turn on MediWatch\n')

        print('Enter 4 to look out on the tower\n')

        print('Enter 5 to go check the forest\n')

        print('Enter 6 to go scavenge outside\n')

        print('Enter 7 to go to Sleep\n')

        print('Enter 8 to quit game\n')

        choice = num_check('Enter your choice: ', 0, 8)
        
        if (choice == 1):
            print("\nYou have",food, "days worth of food.")

        if (choice == 2):
            print("\nYou have",materials,"Base HP.")

        if (choice == 3):
            print("\nYou have",player_hp, "Health.")    

        if (choice == 4):
            print("\nYou use binoculars to look at the town")
            if run == 0:
                run + 1
                print(x)

            elif run == 1:
                print(x)


        if (choice == 5):
            print("\nYou investigate the forest")
            if run == 0:
                run + 1
                print(y)

            elif run > 0:
                print(y)

        if (choice == 6):
            location()

            if status == 'loss' or status == 'win':
                    break

        if (choice == 7):
            turn_counter += 1
            print("You go to sleep...")
            print("The Zombies are coming")
            ApocK_Database()
            if player_hp < 10 and player_hp != 0:
                player_hp = player_hp + 1

            ZombieAttack()
            StatsChecker()
            
            if status == 'loss' or status == 'win':
                break

            else:
                print("Day {}\n".format(turn_counter))

        if status == 'loss':
                    break

        if choice == 8:
            break
        
def ZombieAttack():
    global materials
    global food
    # Array contains the scenarios for zombie attacks with coresponding base damage
    food = food - 1

    if random.random() < 0.25:
        base_hp_loss = 0
        materials = materials - base_hp_loss
        print('The night was calm')
        print("The base was remained quiet")
        print("The base now has {} HP".format(materials))

    elif random.random() < 0.25:
        base_hp_loss = 6
        materials = materials - base_hp_loss
        print('Some zombies attacked your base')
        print("The base was damaged {} HP".format(base_hp_loss))
        print("The base now has {} HP".format(materials))

    elif random.random() < 0.25:
        base_hp_loss = 14
        materials = materials - base_hp_loss
        print('A group of zombies attacked your base')
        print("The base was damaged {} HP".format(base_hp_loss))
        print("The base now has {} HP".format(materials))

    else:
        base_hp_loss = 24
        materials = materials - base_hp_loss
        print('Your base was surrounded in a horde of zombies')
        print("The base was damaged {} HP".format(base_hp_loss))
        print("The base now has {} HP".format(materials))

def location():
    global t_scav_run
    global f_scav_run
    scavenge = town_forest("Would you like to scavenge in the forest or town? \nEnter forest or town, or back to go back to the base menu: ")    
    if scavenge == "town":
        if t_scav_run == 0:     
            print()
            print(town_event)
            print("\nWhat do you?")
            choices()
            t_scav_run += 1
        else:
            print("You already went scavenging there")

    elif scavenge == "forest":
        if f_scav_run == 0:
            print()
            print(forest_event)
            print("\nWhat do you?")
            choices()
            f_scav_run += 1
        else:
            print("You already went scavenging there")

def choices():
        global materials
        global player_hp
        
        print('Enter 1 to lure away enemies\n')

        print('Enter 2 to Attack\n')

        print('Enter 3 to Sneak\n')

        print('Enter 4 to Walk by\n')

        print('Enter 5 to go back to base\n')

        choice = int(input('Enter your choice: '))
        
        if (choice == 1):
            print("You use some materials to lure away the enemies.")
            if random.random() < 0.2:
                print('The trap you made worked!')
                print('You were able to salvage the parts')
                print('You can now scavenge')
                scavenging()

            elif random.random() < 0.4:
                materials_lost = 6
                materials = materials - materials_lost
                print('The trap you made worked too well')
                print('The enemies destroyed your trap thinking it was a human')
                print('You lost {} materials'.format(materials_lost))
                print('You now have {} materials.'.format(materials))
                print('You can now scavenge')
                scavenging()

            else:
                # Losing scenario
                HP_loss = 3
                player_hp = player_hp - HP_loss
                print('You trap failed so badly that the enemies ran straight at you')
                print('You fight them off and are hurt badly')
                print('You run back home wounded')
                print("You were damaged {} HP".format(HP_loss))
                print("You now have {} HP".format(player_hp))

        if (choice == 2):
            print("You attack the enemies with your trusty rifle.")
            if random.random() < 0.2:
                # Success scenario
                print("You were able to shoot all the enemies!")
                print("Your rifle comes through once again.")
                print('You can now scavenge')
                scavenging()
            elif random.random() < 0.4:
                # Okay scenario
                HP_loss = 3
                player_hp = player_hp - HP_loss
                print("You fought wildly and defeated the enemies!")
                print("You were wounded in battle")
                print("You were damaged {} HP".format(HP_loss))
                print("You now have {} HP".format(player_hp))
                print('You can now scavenge')
                scavenging()
            else:
                # Losing scenario
                materials_lost = 6
                materials = materials - materials_lost
                print('You shoot like a newbie and end up missing all.')
                print('You get you weapon knocked out of your hand')
                print('From fear you run back to your base')
                print('You lost {} materials'.format(materials_lost))
                print('You now have {} materials.'.format(materials))

        if (choice == 3):
            print("You carely sneak by the enemies...")
            if random.random() < 0.5:
                # Success scenario
                print("You were able to sneak past the enemies")
                print("You sly dog...")
                print('You can now scavenge')
                scavenging()
            else:
                # Losing scenario
                materials_lost = 8
                materials = materials - materials_lost
                HP_loss = 4
                player_hp = player_hp - HP_loss
                print('You made so much noise you attracted everything in 1 km radius')
                print('You lost HP and materials')
                print('You run back home in a panic.')
                print('You lost {} materials and {} HP'.format(materials_lost, HP_loss))
                print('You now have {} materials and {} HP.'.format(materials, player_hp))

        if (choice == 4):
            print("\nYou casually walk by the enemies...")
            if forest_event == forest_encounter['2F'] or town_event == town_encounter["1T"]:
                # Success scenario
                print("You were able to reach you scavenging destination.")
                print("You can now scavenge")
                scavenging()
            else:
                # Losing scenario
                materials_lost = 4
                materials = materials - materials_lost
                HP_loss = 2
                player_hp = player_hp - HP_loss
                print('What were you thinking?')
                print('You were just gunna walk by those enemies, you wish.')
                print('You were attacked and lost materials')
                print('You run home in embrassment')
                print('You lost {} materials and {} HP'.format(materials_lost, HP_loss))
                print('You now have {} materials and {} HP.'.format(materials, player_hp))
        
        StatsChecker()

        if (choice == 5):
            print("\nYou go back to your base")

def player_info():
    global materials
    global food
    global player_hp
    materials = 50
    food = 1
    player_hp = 10

def ApocK_Full_Game():
    IntroCard()

    instruct = yes_no("Would you like to read the instructions? ")

    if instruct == "yes":
        instructions()

    Intro = yes_no("Would you see the intro? ")

    if Intro == "yes":
        IntroText()

    print("Welcome to your base")
    print("Day {}\n".format(turn_counter))
    BaseMenu()

turn_counter = 1
shop_escape = 0
run = 0
x = ""
y = ""
status = ""

ApocK_Full_Game()

