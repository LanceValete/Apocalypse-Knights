# ApocK Starting Info V2

# Starting Info contains the beginning stats of the player
# This is to have a starting point and a function which can 
# be acessed and updated as the game progresses and the stats
# change and can be printed on command by the player when option is given

def startinginfo():
    player_hp = 10
    food = 2
    base_hp = 100
    return player_hp, food, base_hp
    
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
    print("Press <enter> to continue\n")


    return ""

# user is asked question for instructions

instruct = yes_no("Would you like to read the instructions? ")

# if user responds yes instructions are printed
if instruct == "yes":
    instructions()

print()