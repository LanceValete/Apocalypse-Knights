import random


hints_forest = {"1F": 'You see a horde wandering through the woods', "2F": 'You see the woods are eeirely empty', "3F": 'You see a few zombies around the woods', "4F": 'The woods are swallowed in an ocean of zombies'} 
hints_town = {"1T": 'Smoke can be seen rising from the town', "2T": 'You hear screams from the town, this concerns you.', "3T": 'You hear gunshots in the town', "4T": 'You see a horde going through the town'}
forest_hints =['1F', '2F', '3F', '4F']
town_hints = ['1T', '2T', '3T', '4T'] 
       
t_random_array_item = random.choice(town_hints)
f_random_array_item = random.choice(forest_hints)
forest_current_hint = hints_forest[f_random_array_item]

run = 0

def myfunc():
  global x
  x = forest_current_hint

print("Base Time")
print("What do you want to do?")

n = int(input('Please enter the number of iterations: \n'))

for i in range(0,n):

    print('Enter 1 to Open Fridge\n')

    print('Enter 2 to check Base Defenses\n')

    print('Enter 3 turn on MediWatch\n')

    print('Enter 4 to look out on the tower\n')

    print('Enter 5 to go check the forest\n')

    print('Enter 6 to go to Sleep\n')

    print('Enter 7 to go back to menu\n')

choice = int(input('Enter your choice: '))

if (choice == 1):

            if run == 0:
                myfunc()
                run + 1
                print(x)

            elif run > 0:
                print(x)

if (choice == 2):

        print("rigged from the start")








