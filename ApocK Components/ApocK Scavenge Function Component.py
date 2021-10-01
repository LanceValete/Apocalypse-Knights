# ApocK Scavenging Function Component V1
import random
food = 1
materials = 50

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

        # Update current variable
        food = food + food_gain
        materials = materials + material_gain

        # prints gain and updated variables
        print('You found extra food and materials!')
        print('You obtain {} food and {} materials'.format(food_gain, material_gain))
        print('You now have {} food and {} materials.'.format(food, materials))

    elif random.random() < 0.2:
        # Less loot scenario
        food_gain = 0
        material_gain = 10

        # Update current variable
        food = food + food_gain
        materials = materials + material_gain

        # prints gain and updated variables
        print("You didn't find much loot.")
        print('You obtain {} food and {} materials'.format(food_gain, material_gain))
        print('You now have {} food and {} materials.'.format(food, materials))
    else:
        # Less loot scenario
        food_gain = 1
        material_gain = 15

        # Update current variable
        food = food + food_gain
        materials = materials + material_gain

        # prints gain and updated variables
        print('You found food and materials')
        print('You obtain {} food and {} materials'.format(food_gain, material_gain))
        print('You now have {} food and {} materials.'.format(food, materials))

scavenging()

