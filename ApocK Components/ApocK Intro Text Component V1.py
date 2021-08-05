# ApocK Intro Text V2

# IntroText function allows for a line of text to be printed 
# then a new line is printed when the user presses <enter>

def IntroText(statement):
    play_again = input(statement).lower()
        
    while play_again != "":
        play_again = input("Press <Enter> to continue...").lower()
    if play_again == "":
            return

# Dialogue function contains the introduction dialogue 

def Intro_Dialogue():
        IntroText("Dust, blood, darkness... ")
        IntroText("You lie amoungst the rubble of room ")
        IntroText("You emerge aching and sore, you look around ")
        IntroText("Destruction all around you... ")
        print()
        IntroText('"Hello...." you yell, but no response ')
        IntroText("Your soul feels heavy as you walk through the flames ")
        IntroText("The floor cold with blood, your memories are foggy ")
        IntroText("You wander outside to witness the damage... ")
        IntroText("Corpses litter the courtyard, charred beyond recognision ")
        print()
        IntroText('"What happened here? What happened to me? ')
        IntroText("Memories start coming back, your base, your name. ")
        print()
        print('Enter your name: ')

        # Name code allows user to choose name, user cannot continue until name is entered

        player_name = input()
        answer = "invalid"

        while answer == "invalid":

                # Invalid Input
                if player_name == "":
                        print('Enter your name to continue: ')
                        player_name = input()
                
                # Valid input
                elif player_name != "":
                        print('\n"My name is, {}"'.format(player_name))
                        print()
                        break
                        

        IntroText("You walk to your base, you find weapons, some food and materials ")
        IntroText("You hear a buzz from your radio, you open the connection. ")
        print()
        IntroText('"Attention Templar Knight Survivors, a helicopter is coming to extract ')
        IntroText('you from the outpost, the helicopter will arrive in 5 days, please wait for us." ')
        IntroText("You now have one mission, survive until extraction. ")
        return player_name

Intro_Dialogue()
