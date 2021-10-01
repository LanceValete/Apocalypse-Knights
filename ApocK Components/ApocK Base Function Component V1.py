# V1 Base Menu Function
import random

# player_info contains basic stats of player in dictionary
def player_info():
    xyz = { 'Base HP': 50, 'food': 1, 'player_hp': 10}
    return xyz

# assignment of stats to variable
pl = player_info()

turn_counter = 1

# dictionaries hints_forest and hints_town contain the hints for the
# scenario that will occur and is chosen through coresponding list which
# is randomly chosen to apply to the dictonary to get the randomised hint

hints_forest = {"1F": 'You see a horde wandering through the woods',
                "2F": 'You see the woods are eeirely empty',
                "3F": 'You see a few zombies around the woods', 
                "4F": 'The woods are swallowed in an ocean of zombies'} 

hints_town = {"1T": 'Smoke can be seen rising from the town', 
              "2T": 'You hear screams from the town, this concerns you.',
              "3T": 'You hear gunshots in the town', 
              "4T": 'You see a horde going through the town'}

# Set option array
forest_hints =['1F', '2F', '3F', '4F']
town_hints = ['1T', '2T', '3T', '4T'] 

# randomise hint for round
t_random_array_item = random.choice(town_hints)
f_random_array_item = random.choice(forest_hints)
forest_current_hint = hints_forest[f_random_array_item]
town_current_hint = hints_town[t_random_array_item]

# stating variable
run = 0
x = ""
y = ""


# number checker checks if the user has entered a valid number within a set range
def num_check(question, low, high):
    error = ("Please enter an whole number between 1 and 7") 

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

# myfunc make forest and town hint a global variable which then
# can be used to inside another function (BaseMenu)
def myfunc():
  global x
  global y
  y = forest_current_hint
  x = town_current_hint


# BaseMenu contains 7 options, 1 to check food amount
# 2 to check the material amount, 3 to check the player
# HP, 4 to print the town hint, 5 to print the forest hint,
# 6 to sleep, and 7 to go back to the menu

def BaseMenu():
    turn_counter = 1
    for _ in iter(int, 1):
        # prints options before and after an option is picked
        print("\nWhat do you want to do?")

        print('Enter 1 to Open Fridge\n')

        print('Enter 2 to check Base Defenses\n')

        print('Enter 3 turn on MediWatch\n')

        print('Enter 4 to look out on the tower\n')

        print('Enter 5 to go check the forest\n')

        print('Enter 6 to go to Sleep\n')

        print('Enter 7 to go back to menu\n')

        choice = num_check('Enter your choice: ', 1, 7)
        
        if (choice == 1):
            # print food amount
            print("\nYou have",pl['food'], "days worth of food.")

        if (choice == 2):
            # print material amount
            print("\nYou have",pl['Base HP'],"Base HP.")

        if (choice == 3):
            # print HP amount
            print("\nYou have",pl['player_hp'], "Health.")    

        if (choice == 4):
            # print town hint
            print("\nYou use binoculars to look at the town")
            # prints randomised town hint
            if run == 0:
                myfunc()
                run + 1
                print(x)

            # prints same hint until new round
            elif run > 0:
                print(x)

        if (choice == 5):
            # print forest hint
            print("\nYou investigate the forest")
            # prints randomised forest hint
            if run == 0:
                myfunc()
                run + 1
                print(y)

            # prints same hint until new round
            elif run > 0:
                print(y)

        if (choice == 6):
            # sleeps and continues to new day
            turn_counter += 1
            print("You go to sleep...")
            print("The Zombies are coming")
            # put zombie attack function here
            print("\nDay {}".format(turn_counter))

        if (choice == 7):
            # breaks loop to go back to menu selection
            break

print("Welcome to your base")
print("Day {}".format(turn_counter))
BaseMenu()

         
