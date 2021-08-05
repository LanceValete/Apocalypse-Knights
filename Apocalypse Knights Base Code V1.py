# HKN Base Code V1

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

def startinginfo():
    player_hp = 10
    food = 1
    money = 20
    
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

IntroCard()


instruct = yes_no("Would you like to read the instructions? ")

if instruct == "yes":
    instructions()

Intro = yes_no("Would you see the intro? ")

if Intro == "yes":
    IntroText()






