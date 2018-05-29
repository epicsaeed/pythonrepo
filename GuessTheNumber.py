
import random

def isValid(s): 
    try:
        int(s)
        return True
    except ValueError:
        return False
def Intro():
    #Guess The Number App
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$                                                                              $")
    print("$ Welcome to Guess The Number. This is how the game works: Al is thinking of a $")   
    print("$ number between 1 and 20. You are required to guess that number. Keep in mind $")   
    print("$                  that you are only allowed 5 guesses!                        $")   
    print("$                                                                              $")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

Intro()
NotValid = True
Start = input("                 Ready to play? (Y: for yes, N: for no):")   #asks if user ready to play
Playing = True
while Playing:
    if Start.lower() == "n": #Start == "N" or Start == "n":            #quits program if user chose N (not to play)
        print("GoodBye!")
        exit()
    elif Start == "Y" or Start == "y":
        Playing = False          
        Al = random.randint(1, 20)      #generates a random number between 1 and 20 (to be guessed)
        count = 5                       # number of guesses allowed
        while count !=0:                
            notInt = True
            guess = input("Please enter your guess:")  #takes user guesses
            while notInt:                              #checks if user input is an integer
                if isValid(guess):
                    notInt = False
                    guess = int(guess)
                else:
                    guess = input("Only insert a number please:") 
            count -=1                                       #decrements allowed guesses by 1
            if guess < Al:                                  
                print("too low!")
                print("You have ", count, " Guesses left!") 
            elif guess == Al:                               
                print("Awesome!, Al was thinking of", Al)
                print("GoodBye!")
                exit()
            else:                                           
                print("too high!")
                print("You have ", count, " Guesses left!")
    else:
        while NotValid:                                #checks if user input is valid
            Start = input("Only choose Y/y or N/n please:")
            if Start == "N" or Start == "n" or Start == "y" or Start == "Y":
                NotValid = False
