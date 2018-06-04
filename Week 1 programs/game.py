import time

#makes sure the user enterd a valid value 
def checkChoice(choice):
    inValid = True
    while inValid:
        if choice == 'A' or choice == 'a':
            inValid = False
            return 'A'
        elif choice == 'B' or choice == 'b':
            inValid = False
            return 'B'
        else:
            choice = input("Please select A or B: ") 

#starting\welcome text of the game
def StartUp():
    print("Welcome to The Forest")
    #time.sleep(3)
    print("                    ")
    print("The last thing you remember is walking home at night\nafter having dinner with your friends.")
    #time.sleep(3)
    print("                    ")
    print("You have now opened your eyes to realiye you are laying down in the middle of a forest.")
    #time.sleep(3)
    print("                    ")
    print("Now, you must get out before it is too late!")
    #time.sleep(3)
    print("                    ")
    play = input ("HIT ENTER TO PLAY:")
    if play == "":
        print("WELCOME!")
        #time.sleep(3)

#Waking up
def Level1(name):
    N = name
    called = False
    print("You stood up. Now, what should you do?")
    time.sleep(2)
    choice1 = input("A. reach for my phone in my pocket\nB. scream for help: ")
    if checkChoice(choice1) == 'A':#if user decided to check the phone
        print("Oh No! my battery is at 10% and there's no signal!\n ")
        time.sleep(3)
        choice2A = input("A. Turn flashlight on and see what's around me\nB. Save battery and get up to find a signal: \n ")
        if checkChoice(choice2A) == 'A': #if user chose to turn flash light on
            print("Nothing but tall trees around me..\n ")
            time.sleep(2)
            print("Maybe I should walk around for a bit.\n ")
            time.sleep(2)
            print("*walking*")
            time.sleep(2)
            print("You found a cabin.... It is not visible much because the flash light is weak but it seems empty.\n ")
            time.sleep(2)
            choice3A = input("A. Investigate the cabin.\nB. Ignore it and keep walking: \n ")
            if checkChoice(choice3A) == 'A':
                Level2(N)
            else:
                print("I just heard some movement around me. I think it's best that I enter that cabin \n ")
                enter = input("PRESS RETURN TO ENTER THE CABIN: \n ")
                if enter == "":
                    Level2(N)
                else:
                    print("Good Bye.")
                    exit()

        else:#if user chose to save battery and find a signal
            called = True
            print("you been walking around searching for a signal. You managed to get a weak bar.\n Instantly, you called the emergencies. Strange enough, nobody replied and suddnely the phone died.\n ")
            print("*walking...*\n ")
            time.sleep(5)
            print("You have reached a mysterious cabin. Perhabs you should go in to investigate.\n ")
            time.sleep(3)
            enter = input("PRESS RETURN TO ENTER THE CABIN: \n ")
            if enter == "":
                Level2(N)
            else:
                print("Good Bye.")
                exit()
    else:#if user chose to scream for help
        print("HELP! HELP!...... Ok... there's no point\n ")
        time.sleep(2)
        print("No... wait! There's a light coming from a distance!\n ")
        time.sleep(2)
        choice2B = input("A. Walk towards the light\nB. Scream louder for the light source to notice me.\n ")
        if checkChoice(choice2B) == 'A':#if user decided to walk towards light
            print("As your're walking, you realize that the light was the moon reflection on a window of a cabin.\n ")
            time.sleep(2)
            print("Let me go inside.... perhabs there's a phone or a radio I could use.\n ")
            enter = input("PRESS RETURN TO ENTER THE CABIN: \n ")
            if enter == "":#entering house
                Level2(N)
            else:
                print("Good Bye.")
                exit()
        else:#if user decided to scream louder
            print("HEEEEELP!! HEEEELP! \n")
            time.sleep(3)
            print("Suddenly, the light source stopps and you start hearing movement around you.\nIt appears to be a group of coyotes have responded to your screams. ")
            time.sleep(5)
            print("You are now dead.")
            exit()

#investigating cabin
def Level2(called):
    print("You have now entered the cabin. \n ")
    choice1 = input("")

def main():
    StartUp()
    Name = input("Please state your name: ")
    print("Welcome, ",Name)
    time.sleep(3)
    Level1(Name)

main()
