#This app converts temperature given in Celsius to Fahrenheit.

#function that converts Celsius to Fahrenheit
def convertToF(t):                              
    f = t * 1.8 + 32.0                       
    return f    


#function that converts Fahrenheit to Celsius
def convertToC(t):                              
    f = (t - 32.0 ) * 0.56                    
    return f    

#function that checks if user input is valid (a float)    
def isValid(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False

#function that checks if passed parameter is a letter
def isLetter(s):             
    if s.isalpha():
        return True
    return False

#hello 
optionA = False
optionB = False
notLetter = True

Option = input("Please enter 'A' to convert from Celsius to Fahrenheit\nOr enter 'B' for the opposite.")

#checks user input (A or B)
while notLetter:            #checks user input (A or B)
    if isLetter(Option):
        if Option == 'A' or Option == 'a':
            notLetter = False
            optionA = True
        elif Option == 'B' or Option == 'b':
            notLetter = False
            optionB = True
        else:
            Option = input("Please enter 'A' or 'B':")
    else:
        Option = input("Please enter 'A' or 'B' ONLY:")



def main():   
    if optionA:                                 
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        notValid = True
        C = input("Please the temperature in Celcius: ")   
        while notValid:
            if isValid(C):
                notValid = False
                C = float(C)
            else:
                C = input("Only insert a number please.") 
        print("You have entered ", C, " °C")                            #displays input temperature in °C
        print(C, "°C is equal to ", round(convertToF(C),2), "°F.")                #displays temp in °F
    else:
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        notValid = True
        F = input("Please the temperature in Fahrenheit: ")
        while notValid:
            if isValid(F):
                notValid = False
                F = float(F)
            else:
                F = input("Only insert a number please.") 
        print("You have entered ", F, " °F")                            #displays input temperature in °C
        print(F, "°F is equal to ", round(convertToC(F),2), "°C.")                #displays temp in °F   

main()                                          
