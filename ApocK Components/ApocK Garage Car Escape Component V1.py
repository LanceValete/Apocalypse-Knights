# ApocK Garage Component
bike_fixed = 0

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

def Garage_Escape():
    global bike_fixed
    materials = 200

    print('\nYou walk into the garage')
    print('You see the shape of a motorcycle sitting in the corner')
    print('"I wonder if I can fix this..." you wonder\n')
    print("The motorcycle is covered by a tarp")
    print("You pull off the tarp and face palm")
    print("The motorcycle is not a motorcycle")
    print("Its a Vespa 98 Corsa Circuito in bright red")
    print('"Great..." you mutter')

    while True:
        print('\n-------------------------')
        print("\nWhat do you want to do?")
        print('Enter 1 to look at the bike\n')
        print('Enter 2 to repair to repair bike\n')
        print('Enter 3 to go back')
        print('\n-------------------------\n')

        choice = num_check('Enter your choice: ', 0, 3)

        if choice == 1:
            print('You examine the Vespa 98 Corsa Circuito')
            print('The bright red makes you gag a little')
            print("\nYou need 100 materials to repair")

        elif choice == 2:
            if materials >= 100 and bike_fixed != 1:
                materials -= 100
                bike_fixed += 1
                print('You repair the Vespa 98 Corsa Circuito')
                print('You repaired it by kicking it and slapping it with 100 planks of wood')
                print('Very nice..., now you just tonights raid with what materials you have left')
                print('Then you can escape after the horde passes in the night')

            elif bike_fixed == 1:
                print("You already repaired the Vespa...")

            else:
                print("You don't have enough materials")
                print("You need 100 materials and only have", materials, "materials")
                print("Come back when you have enough")

        elif choice == 3:
            break

        else:
            choice = num_check('Enter your choice: ', 0, 3)
    
Garage_Escape()