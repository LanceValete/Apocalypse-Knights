# ApocK Health Menu V1

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

# health menu combines the health statistic and adds another option
# to use materials and change them to player HP

def health_menu():
    while True:

        print('\n-------------------------')
        print("\nWhat do you want to do?")
        print('Enter 1 to view player HP\n')
        print('Enter 2 to convert materials to heal player HP\n')
        print('Enter 3 to go back')
        print('\n-------------------------\n')
    
        choice = num_check('Enter your choice: ', 0, 3)

        if choice == 1:
            print("\nYou have", 10, "Health.")

        elif choice == 2:
            while True:
                print('\n####################################')
                print('How much would you want to convert?')
                print('1. 10 Materials - 1 Player HP')
                print('2. 20 Materials - 2 Player HP')
                print('3. Go back')
                print('####################################')

                choice = num_check('Enter your choice: ', 0, 3)

                if choice == 1:
                    # - 10 materials
                    # + 1 player HP
                    print('You converted 10 materials into 1 player HP')
                        
                elif choice == 2:
                    # - 20 materials
                    # + 2 player HP
                    print('You converted 20 materials into 2 player HP')
                        
                elif choice == 3:
                    break

        elif choice == 3:
            break

        else:
            choice = num_check('Enter your choice: ', 0, 3)


health_menu()