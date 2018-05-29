#Speed Converter App

def isFloat(s):             #function that checks if passed parameter is float
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False

def isLetter(s):             #function that checks if passed parameter is a letter
    return s.isalpha()

optionA = False
optionB = False
notLetter = True

Option = input("Please enter 'A' to convert from km/h to m/h\nOr enter 'B' to convert from m/h to km/h:")

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

if optionA:
    notFloat = True
    K = input("Please enter the speed in Km/h: ")       
    while notFloat:             #checks if user input is valid
        if isFloat(K):
            notFloat = False
            K = float(K)
            break
        else:
            K = input("Please enter a number only: ")    
    M = K * 0.6213711                                       
    print("Entered speed in Km/h: ",K)                                  
    print("Speed in Miles/h: ",round(M,2))  #displays speed in m/h while rounding it to 2 decimal places
else:
    notFloat = True
    M = input("Please enter the speed in m/h: ")       
    while notFloat:             #checks if user input is valid
        if isFloat(M):
            notFloat = False
            M = float(M)
            break
        else:
            M = input("Please enter a number only: ")    
    K = M * 1.609344                                           
    print("Entered speed in m/h: ",M)                                  
    print("Speed in Km/h: ",round(K,2))  #displays speed in m/h while rounding it to 2 decimal places

