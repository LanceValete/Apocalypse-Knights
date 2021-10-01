# ApocK Stats Checker

# These statistics are placeholders for the real variables in the base component
# They can be changed over the course of the game and can be changed here to 
# see the different outcomes

food = 1
materials = 50
health = 10
turn_counter = 0
shop_escape = 0

def StatsChecker():

    # Checks if player is still alive and has not pass round 5 or purchased shop_escape
    if food >= 1 and materials > 0 and health > 0 and turn_counter < 5 and shop_escape != 1:
        print('Alive')

    # Losing scenarios
    elif food <= 0:
        # if the player runs out of food before round 5 they lose
        print("You starved to death...")
        print("Game Over")
        print('Dead')

    elif materials <= 0:
        # if the player runs out of materials before round 5 they lose
        print("Your base was destroyed by zombies...")
        print("Game Over")
        print('Dead')

    elif health <= 0:
        # if the player runs out of HP before round 5 they lose
        print("You were killed by enemies...")
        print("Game Over")
        print('Dead')

    #Winning scenarios
    elif turn_counter > 5:
        # if the player passes day 5 without dying they win
        print("You survived the 5 days!")
        print("You Win")
        print('Win')

        # if the player purchases the shop escape on day 3 they win
    elif shop_escape == 1:
        print("You payed passage to safety!")
        print("You Win")
        print('Win')

StatsChecker()