# ApocK Base Code V2
import random

# ApocK Database contains the forest and town hint and encounter text to be used in
# other functions multiple times and to make the random.choice code to run once so
# that the random variable stays the same until run again
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

#___________________________________________________________

# Introduction Section
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

# IntroText function allows for a line of text to be printed 
# then a new line is printed when the user presses <enter>

def IntroText(statement):
    play_again = input(statement).lower()
        
    while play_again != "":
        play_again = input("Press <Enter> to continue...").lower()
    if play_again == "":
            return

# Dialogue function contains the introduction dialogue 

def Intro_Dialogue():
        IntroText("Press <Enter> to continue...\n")
        IntroText("Dust, blood, darkness... ")
        IntroText("You lie amoungst the rubble of room ")
        IntroText("You emerge aching and sore, you look around ")
        IntroText("Destruction all around you... ")
        print()
        IntroText('"Hello...." you yell, but no response ')
        IntroText("Your soul feels heavy as you walk through the flames ")
        IntroText("The floor cold with blood, your memories are foggy ")
        IntroText("You wander outside to witness the damage... ")
        IntroText("Corpses litter the courtyard, charred beyond recognision ")
        print()
        IntroText('"What happened here? What happened to me? ')
        IntroText("Memories start coming back, your base, your name. ")
        print()
        print('Enter your name: ')

        # Name code allows user to choose name, user cannot continue until name is entered

        player_name = input()
        answer = "invalid"

        while answer == "invalid":

                # Invalid Input
                if player_name == "":
                        print('Enter your name to continue: ')
                        player_name = input()
                
                # Valid input
                elif player_name != "":
                        print('\n"My name is, {}"'.format(player_name))
                        print()
                        break
                        

        IntroText("You walk to your base, you find weapons, some food and materials ")
        IntroText("You hear a buzz from your radio, you open the connection. ")
        print()
        IntroText('"Attention Templar Knight Survivors, a helicopter is coming to extract ')
        IntroText('you from the outpost, the helicopter will arrive in 5 days, please wait for us." ')
        IntroText("You now have one mission, survive until extraction. ")
    
# Yes_No function allows text to be answered as question strictly to 
# only two responses "Yes" and "No" and if any other response is given
# then the question given will loop

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

# Instructions Function The Instructions give a small synopsis of the current 
# story and setting, then lists the objectives the player must conduct to continue through the game

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


    return ""

# Starting Info contains the beginning stats of the player
# This is to have a starting point and a function which can 
# be acessed and updated as the game progresses and the stats
# change and can be printed on command by the player when option is given

def player_info():
    global materials
    global food
    global player_hp
    materials = 50
    food = 1
    player_hp = 10

#___________________________________________________________

# Outside Scenario Generator
def num_check(question, low, high):
    error = ("Please enter an whole number between 1 and {}".format(high)) 

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

def town_forest(question):
    # Changed yes_no function to make response only be
    # town, forest and back. Continues only if these inputs
    # are entered
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

def choices():
        global materials
        global player_hp

        # prints options, 1 to lure away enemies, 2 to attack,
        # 3 to sneak, 4 to walk by and 5 to go back to base
        print('\n##############################')
        print('\nEnter 1 to lure away enemies\n')

        print('Enter 2 to Attack\n')

        print('Enter 3 to Sneak\n')

        print('Enter 4 to Walk by\n')

        print('Enter 5 to go back to base\n')
        print('##############################')

        # int makes choice only be an interger
        choice = num_check('Enter your choice: ', 0, 5)
        print()
        
        # Option 1 - Lure away enemies
        if (choice == 1):
            # general statement
            print("You use some materials to lure away the enemies.")

            if random.random() < 0.2:
                # 20% chance for total success
                print('The trap you made worked!')
                print('You were able to salvage the parts')
                print('You can now scavenge\n')
                scavenging()

            elif random.random() < 0.4:
                # 40% chance for success but lost few materials
                materials_lost = 6
                materials = materials - materials_lost
                print('The trap you made worked too well')
                print('The enemies destroyed your trap thinking it was a human')
                print('\nYou lost {} materials'.format(materials_lost))
                print('You now have {} materials.'.format(materials))
                print('You can now scavenge\n')
                scavenging()

            else:
                # Losing scenario
                # 40% chance for faliure and return back to base menu (lose player HP)
                HP_loss = 3
                player_hp = player_hp - HP_loss
                print('You trap failed so badly that the enemies ran straight at you')
                print('You fight them off and are hurt badly')
                print('You run back home wounded')
                print("\nYou were damaged {} HP".format(HP_loss))
                print("You now have {} HP".format(player_hp))

        if (choice == 2):
            # general statement
            print("You attack the enemies with your trusty rifle.")

            if random.random() < 0.2:
                # Success scenario
                # 20% chance for total success
                print("You were able to shoot all the enemies!")
                print("Your rifle comes through once again.")
                print('You can now scavenge\n')
                scavenging()

            elif random.random() < 0.4:
                # Okay scenario
                # 40% chance for success but lost few player HP
                HP_loss = 3
                player_hp = player_hp - HP_loss
                print("You fought wildly and defeated the enemies!")
                print("You were wounded in battle")
                print("\nYou were damaged {} HP".format(HP_loss))
                print("You now have {} HP".format(player_hp))
                print('You can now scavenge\n')
                scavenging()

            else:
                # Losing scenario
                # 40% chance for faliure and return back to base menu (lose materials)
                materials_lost = 6
                materials = materials - materials_lost
                print('You shoot like a madman and dont hit anything')
                print('Enemies start running at you from the dark')
                print('You get you weapon knocked out of your hand')
                print('From fear you run back to your base')
                print('\nYou lost {} materials'.format(materials_lost))
                print('You now have {} materials.'.format(materials))

        if (choice == 3):
            print("You carely sneak by the enemies...")
            if random.random() < 0.5:
                # Success scenario
                # 50% chance for success (no loss)
                print("You were able to sneak past the enemies")
                print("You sly dog...")
                print('You can now scavenge\n')
                scavenging()

            else:
                # Losing scenario
                # 50% chance for faliure and return back to base menu
                materials_lost = 8
                materials = materials - materials_lost
                HP_loss = 4
                player_hp = player_hp - HP_loss
                print('You made so much noise you attracted everything in 1 km radius')
                print('You lost HP and materials')
                print('You run back home in a panic.')
                print('\nYou lost {} materials and {} HP'.format(materials_lost, HP_loss))
                print('You now have {} materials and {} HP.'.format(materials, player_hp))

        if (choice == 4):
            print("\nYou casually walk by the enemies...")
            if forest_event == forest_encounter['2F'] or town_event == town_encounter["1T"]:
                # Success scenario
                # if the player walks by peaceful events
                print("You were able to reach you scavenging destination.")
                print("You can now scavenge\n")
                scavenging()

            else:
                # Losing scenario
                # if the player tries to walk by anything else
                materials_lost = 4
                materials = materials - materials_lost
                HP_loss = 2
                player_hp = player_hp - HP_loss
                print('What were you thinking?')
                print('You were just gunna walk by those enemies, you wish.')
                print('You were attacked and lost materials')
                print('You run home in embrassment')
                print('\nYou lost {} materials and {} HP'.format(materials_lost, HP_loss))
                print('You now have {} materials and {} HP.'.format(materials, player_hp))

        StatsChecker()

        if (choice == 5):
            # go back to menu
            print("\nYou go back to your base")

def scavenging():
    global food
    global materials
    # When the player succeeds in passing the scenario
    # this function will run and determine how much loot
    # the player will obtain

    if random.random() < 0.2:
        # Extra loot scenario
        food_gain = 2
        material_gain = 20
        # prints general statement
        print('You found extra food and materials!')

    elif random.random() < 0.2:
        # Less loot scenario
        food_gain = 0
        material_gain = 10
        # prints general statement
        print("You didn't find much loot.")

    else:
        # Less loot scenario
        food_gain = 1
        material_gain = 15
        # prints general statement
        print('You found food and materials')

    # Update current variable
    food = food + food_gain
    materials = materials + material_gain

    # prints gain and updated variables
    print('You obtain {} food and {} materials'.format(food_gain, material_gain))
    print('You now have {} food and {} materials.'.format(food, materials))

def Outside_Scenario():
    global t_scav_run
    global f_scav_run

    scavenge = town_forest("Would you like to scavenge in the forest or town? \nEnter forest or town, or back to go back to the base menu: ")    
    
    # Outside_Scenario function combines both the choices function
    # and the scavenging function while also utilising the 
    # encounter randomiser and applying the choices function
    # getting an outcome whether good or bad

    # the code will print the town randomised encounter and
    # display the choices
    if scavenge == "town":
        if t_scav_run == 0:     
            print('\n')
            print(town_event)
            print("\nWhat do you?")
            choices()
            t_scav_run += 1
        else:
            print("\nYou already went scavenging there")

    # the code will print the forest randomised encounter and
    # display the choices
    elif scavenge == "forest":
        if f_scav_run == 0:
            print('\n')
            print(forest_event)
            print("\nWhat do you?")
            choices()
            f_scav_run += 1
        else:
            print("\nYou already went scavenging there")

#___________________________________________________________

# Main Code Line
def BaseMenu():
    global run
    global status
    global player_hp
    global turn_counter
    
    ApocK_Database()
    player_info()

    while True:
        print('\n##############################')
        print("\nWhat do you want to do?")

        print('Enter 1 to Open Fridge\n')

        print('Enter 2 to check Base Defenses\n')

        print('Enter 3 turn on MediWatch\n')

        print('Enter 4 to look out on the tower\n')

        print('Enter 5 to go check the forest\n')

        print('Enter 6 to go scavenge outside\n')

        print('Enter 7 to go to Sleep\n')

        print('Enter 8 to quit game\n')
        print('##############################')

        choice = num_check('Enter your choice: ', 0, 8)
        print()
        
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
            Outside_Scenario()

            if status == 'loss' or status == 'Win':
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
            
            if status == 'loss' or status == 'Win':
                break

            else:
                print("\n| Day {} |".format(turn_counter))

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

    elif random.random() < 0.25:
        base_hp_loss = 6
        materials = materials - base_hp_loss
        print('Some zombies attacked your base')

    elif random.random() < 0.25:
        base_hp_loss = 14
        materials = materials - base_hp_loss
        print('A group of zombies attacked your base')

    else:
        base_hp_loss = 24
        materials = materials - base_hp_loss
        print('Your base was surrounded in a horde of zombies')
        
    print("\nThe base was damaged {} HP".format(base_hp_loss))
    print("The base now has {} HP\n".format(materials))

def StatsChecker():
    global food
    global materials
    global player_hp
    global turn_counter
    global shop_escape
    global status

    # Checks if player is still alive and has not pass round 5 or purchased shop_escape
    if food >= 1 and materials > 0 and player_hp > 0 and turn_counter < 5 and shop_escape != 1:
        status = 'normal'

    # Losing scenarios
    elif food < 0:
        # if the player runs out of food before round 5 they lose
        print("You starved to death...")
        print("Game Over")
        status = 'loss'

    elif materials <= 0:
        # if the player runs out of materials before round 5 they lose
        print("Your base was destroyed by zombies...")
        print("Game Over")
        status = 'loss'

    elif player_hp <= 0:
        # if the player runs out of HP before round 5 they lose
        print("You were killed by enemies...")
        print("Game Over")
        status = 'loss'

    #Winning scenarios
    elif turn_counter > 5:
        # if the player passes day 5 without dying they win
        print("You survived the 5 days!")
        print("You Win")
        status = 'loss'

        # if the player purchases the shop escape on day 3 they win
    elif shop_escape == 1:
        print("You payed passage to safety!")
        print("You Win")
        status = 'loss'

def ApocK_Full_Game():
    IntroCard()

    instruct = yes_no("Would you like to read the instructions? ")

    if instruct == "yes":
        instructions()

    Intro = yes_no("Would you see the intro? ")

    if Intro == "yes":
        Intro_Dialogue()

    print("Welcome to your base")
    print("\n| Day {} |".format(turn_counter))
    BaseMenu()

turn_counter = 1
shop_escape = 0
run = 0
x = ""
y = ""
status = ""

ApocK_Full_Game()

