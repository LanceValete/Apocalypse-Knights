# ApocK Outside Function V2
import random

# placeholder for food and materials
food = 5
materials = 50
player_hp = 10

# generates hint configuration for day
forest_hints =['1F', '2F', '3F', '4F']
town_hints = ['1T', '2T', '3T', '4T'] 

t_random_array_item = random.choice(town_hints)
f_random_array_item = random.choice(forest_hints)
town_encounter = {"1T": 'You spot a party of scavengers...\nThey seem friendly.\nOne says to you "We dont want any trouble"', 
                  "2T": 'You see a group of raiders robbing some scavengers.\nA man screams "Help us please!"',
                  "3T": 'You spot a gang of heavily armoured raiders.\nThey are killing scavengers.\nThey dont show mercy',
                  "4T": 'The town is filled with zombies.\nYou sneak carefully until you accidentilly hit one\n"Uh oh" you mutter.'}

forest_encounter = {"1F": 'You get to forest to find no zombies?\nThings are going to well...',
                    "2F": 'You spot a medium sized horde...\nThey seem to docile.\nIf you sneak correctly you should be fine',
                    "3F": 'You see a couple of zombies in the forest.\nYou should be able to kill them',
                    "4F": 'You arrive at the forest to find a huge horde engulf the forest'}

# events strings are generated and can be used in functions
town_event =  town_encounter[t_random_array_item]
forest_event = forest_encounter[f_random_array_item]

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

def choices():
        global materials
        global player_hp

        # prints options, 1 to lure away enemies, 2 to attack,
        # 3 to sneak, 4 to walk by and 5 to go back to base
        print('\n------------------------------')
        print('\nEnter 1 to lure away enemies\n')

        print('Enter 2 to Attack\n')

        print('Enter 3 to Sneak\n')

        print('Enter 4 to Walk by\n')

        print('Enter 5 to go back to base\n')
        print('------------------------------')

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

        # put stats here

        if (choice == 5):
            # go back to menu
            print("\nYou go back to your base")

def Outside_Scenario():
    # location function combines both the choices function
    # and the scavenging function while also utilising the 
    # encounter randomiser and applying the choices function
    # getting an outcome whether good or bad

    # the player is asked where they would want to scavenge
    # player can only respond with town, forest or back
    scavenge = town_forest("Would you like to scavenge in the forest or town? \nEnter forest or town, or back to go back to the base menu: ")

    # the code will print the town randomised encounter and
    # display the choices
    if scavenge == "town":
        print()
        print(town_event)
        print("\nWhat do you?")
        choices()

    # the code will print the forest randomised encounter and
    # display the choices
    elif scavenge == "forest":
        print()
        print(forest_event)
        print("\nWhat do you?")
        choices()

    else:
        print('\nYou return to your base')

# all code is run in one function calling all other two
Outside_Scenario()



