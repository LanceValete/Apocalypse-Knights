# V2 Base Menu Function
import random

# player_info contains basic stats of player using global variable
def player_info():
    global materials
    global food
    global player_hp
    materials = 50
    food = 1
    player_hp = 10

# assignment of stats to variable
turn_counter = 1
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


# BaseMenu contains 7 options, 1 to check food amount
# 2 to check the material amount, 3 to check the player
# HP, 4 to print the town hint, 5 to print the forest hint,
# 6 to sleep, and 7 to go back to the menu

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
            # put scavenging menu here
            print('Scavenge Menu')

        if (choice == 7):
            turn_counter += 1
            print("You go to sleep...")
            print("The Zombies are coming")
            ApocK_Database()
            if player_hp < 10 and player_hp != 0:
                player_hp = player_hp + 1

            # Put zombie attack and stats checker here

            else:
                print("\n| Day {} |".format(turn_counter))

        if choice == 8:
            break

print("Welcome to your base")
print("Day {}".format(turn_counter))
BaseMenu()

         
