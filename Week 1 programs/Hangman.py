
#Hangman game

import random
import time

def isValid(s):             #functions that checks in passed parameter is a letter
    if s.isalpha():
        return True
    return False

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$                                                                              $")
print("$ Welcome to Hangman.This is how the game works: Al is thinking of an 8 letter $")
print("$ word.You are required to guess the word Al is thinking of. Keep in mind that $")
print("$                  that you are only allowed 10 guesses!                       $")
print("$                                                                              $")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("                                                                                ")

LIST = ['newstore', 'python', 'dragon', 'ice cream']     #
word = random.choice(LIST)                  #selects a random word from the list above
counter = 10                                #number of guesses allowed
guessed = []                                #keeps track of correct guessed letters

while counter != 0:                         
    dash = ''                               #initializes an empty string to be used later
    for letter in word:                     #loop for the amount of letters existing in word
        if letter in guessed:                   #(if a letter exists within the guessed word,
            dash = dash + letter                #add it to the displayed dashes.
        else:                                   #otherwise,
            dash = dash + "_"                   #print an underscore in its place).
    if dash == word:                         #checks if what's on display is the correct word
        print("You guessed", word)           
        break                                

    print("Guess a letter: "," ".join(dash)) 
    guess = input()                          
    notLtr = True
    MoreThanOneLtr = True
    while notLtr:                           #checks if input is a letter
        if isValid(guess):
            while MoreThanOneLtr:
                if len(guess) >1:
                    print("Don't cheat. Enter one letter only!: "," ".join(dash))
                    guess = input() 
                else:
                    MoreThanOneLtr = False
            notLtr = False
            guess = str(guess)
        else:
            print("only enter a letter please.")
            time.sleep(2)
            print("Guess a letter: "," ".join(dash))
            guess = input()

    if guess.isupper():                     #converts upper case input to lower case
        guess = guess.lower()

    if guess in guessed:                    #checks if the user repeats inserting a letter
        print("Already guessed")            
    elif guess in word:                     #checks if the inserted letter exists in the word
        counter -=1                         
        print("Correct!", counter," guesses left.")     
        guessed.append(guess)                           #adds the letter to the list of guessed letters.
    else:
        counter -=1                         
        if counter == 0:
            print("You have exceeded all allowed guesses. Game Over!")  
            break 
        print("Try again!", counter," guesses left.")   

if counter:
    print("You guessed the word: ", word)
else:
    print("You didn't get the word: ", word)