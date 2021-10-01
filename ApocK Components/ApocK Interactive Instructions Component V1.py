# ApocK Interactive Instructions V1
import random
# The intro text function will be used here as it will allow users to go
# at their own pace and read the instructions one set at a time

def IntroText(statement):
    play_again = input(statement).lower()
        
    while play_again != "":
        play_again = input("Press <Enter> to continue...").lower()
    if play_again == "":
            return

# Allows for yes and no questions to asked
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

# Interactive Instructions combine the introtext to allow the user to 
# read at their own pace and to also inputs tutorial menus to teach how
# to use menus, also has more in depth explaintions for gameplay mechanics

def ApocK_Tutorial():
    IntroText('Press <Enter> to print...\n')
    IntroText('Welcome to Apocalypse Knights')
    IntroText('This games main gameplay mechanics are menus and choice')
    IntroText('This is an example of a game menu')

    print('\n##############################')
    print('\nEnter 1 to look right\n')
    print('Enter 2 to look left\n')
    print('Enter 3 to look down\n')
    print('Enter 4 to look up\n')
    print('Enter 5 to go back\n')
    print('##############################\n')

    IntroText('In the game menu, to interact with a menu enter the number next to the action you want to make')
    IntroText('Example: Entering 1 will cause the player to look right')
    IntroText('Try out this example menu')

    print('\n##############################')
    print('\nEnter 1 to pet imaginary dog\n')
    print('Enter 2 to pet imaginary cat\n')
    print('##############################\n\n')

    answer = "invalid"
    while answer == "invalid":

        choice = input('Enter your choice: ')
            
        if (choice == '1'):
            print("\nYou pet the dog...")
            print("The dog is happy!")
            break

        elif (choice == '2'):
            print("\nYou pet the cat...")
            print("The cat nibbles at your finger!")
            break

        elif (choice != '1' or choice != '2'):
            print("Enter 1 or 2 to continue")

    print('Nice!')    

    IntroText('\nIn the menu when scavenging, your actions will have a chance of success and failure')
    IntroText('Try balance the risks of losing health and materials.')
    IntroText("In the next example there will be a 50/50 chance for a scenario result")

    print('\n##############################')
    print('\nEnter 1 to walk towards dog\n')
    print('##############################\n')
    
    while answer == "invalid":

        choice = input('Enter your choice: ')

        if (choice == '1'):
            print("\nYou approach the dog slowly...")
            if random.random() < 0.5:
                print("The dog licks your ankles, nice!")
                break

            else:
                print('The dog bites your ankles?')
                break

        elif (choice != '1'):
            print("Enter 1 to continue\n")
    
    print('\nThe two different results were:\nThe dog licks your ankles, nice!\nThe dog bites your ankles?')

    IntroText('\nThats how you use the menus in Apocalyspe Knights')

def new_instructions():
    print()
    # This segment of text states the task and setting
    print("How to Play Apocalpyse Knights")
    print("\nApocalpyse Knights is a choices game where you must make")
    print("decisions to survive through the 5 days during a zombie")
    print("apocalypse and wait for a helicopter extraction from your stronghold.\n")

    # This segment of text states the story aspect of the game
    print("Gameplay Component - Story")
    print("You are an Apocalpyse Knight, part of the Templars a group created in")
    print("the future after the rise of the zombie pandemic devoted to defense and chivalry.\n")
    
    # This segment of text states the players health, food amount and base HP when starting a new game
    print("Gameplay Component - Stats and Vitals")
    print("The player will start off with 10HP, 1 days worth of food and 50 Base HP.")
    print("Your vital resources are health, food and materials. Food and materials can be")
    print("gathered through scavenging outside, health can be gained by sleeping (+ 1HP) or")
    print("by turning materials into medical supplies for health\n")

    # This segment of text states the main gameplay component of scavenging to get vital resources
    print("Gameplay Component - Scavenging at the town and forest")
    print("You the player must go out to scavenge for food to continue through the")
    print("days while encountering obstacles to overcome, balancing risk and")
    print("reward with losing health and or food to continue. In the town you can collect")
    print("wood and steel to increase your base's survivability. In the forest you can")
    print("find animals and wood to increase base health and food to continue.\n")
    
    # This segment of text states how the round cycle works for the game and how to win
    print("Gameplay Component - Day + Night Cycle and Extraction")
    print("During the day, you can scavenge your vital supplies.")
    print("During the night, zombies will come out to hunt you in your base,")
    print("and inflict damage depending on the size of the horde.")
    print("If you run out of food or Base HP, you will be overrun of starve.")
    print("In order to survive the 5 days before extraction you must outlast")
    print("the five days through decisions making and risk taking with a bit of luck.\n")

    # This segment of text states another route of escape being the car garage route
    print("Gameplay Component - Garage Escape Option")
    print("One other way to escape safely is to craft your own vehicule, with some luck")
    print("you need to collect 100 materials to escape and craft your getaway in the garage")
    print("during the day allowing you to escape during the night\n")

    print('Good Luck and Happy Hunting!')

    return ""

instruct = yes_no("Would you like to read the instructions? ")

if instruct == "yes":
    new_instructions()

tutorial = yes_no("Would you like do the tutorial? ")

if tutorial == "yes":
    ApocK_Tutorial()


