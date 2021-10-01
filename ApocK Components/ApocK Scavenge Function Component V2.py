# ApocK Scavenge Function V2
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
    
scavenging()