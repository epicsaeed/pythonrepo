
#opens file and create a list of each line
with open('inventory.txt') as f:
    inventory = list(f)

#length of opened file
l = len(inventory)


#variables
productID=[]
name=[]
size=[]
color=[]
inStock=[]

#this function reads opened file and assigns each row to its appropriate value in the lists above.
def setList():  
    
    #variables
    s = []
    counter = 2
    #reads inventory list line by line
    while counter < len(inventory):
        #splits each line by tabs and save in a temp list (s)
        for word in inventory[counter].split("\t"):
            s.append(word)
        #removes \n from last element
        s[-1] = s[-1].strip()

        #replaces empty string in s with 'N/A'
        i = 0
        while i < len(s):
            if s[i]:
                i+=1
            else:
                s[i] = "N/A"

        #adds each row to its appropriate list
        productID.append(s[0])
        name.append(s[1])
        size.append(s[2])
        color.append(s[3])
        inStock.append(s[4])
        counter+=1
        #print(s)    #for testing
        #clears temp list
        s.clear()
    print("Inventory has been updated!")

#takes users to options function
def mainList():
    x = input("press return to go to main list")
    if x == "":
        options()

#shows the list of products
def viewList():
    counter = 0

    #excludes the labels from inventory length
    r = len(productID)
    print(r)
    
    print("No.     ProductID       Name        Size        Color       inStock")
    print("===================================================================")

    while counter < r:
        print(counter+1,".      ",productID[counter],"      ",name[counter],"      ",size[counter],"      ",color[counter],"      ",inStock[counter])
        counter+=1

#checks if a passed parameter is an integer
def isValid(s): 
    try:
        int(s)
        return True
    except ValueError:
        return False

#function to add items to the list
def addItem():
    x = input("Please enter the product ID: ")
    
    notValid = True
    while notValid:
        if len(x) != 7:
            x = input("product ID must be 7 digits: ")
        else:
            productID.append(x)
            notValid = False

    n = input("Please enter the name of the product: ")
    if n == "":
        name.append("N/A")
    else:
        name.append(n)

    s = input("Please enter the size of the item: ")
    if s == "":
        size.append("N/A")
    else:
        size.append(s)

    c = input("Please enter the color of the product: ")
    if c == "":
        color.append("N/A")
    else:
        color.append(c)

    iS = input("How many of this item is in stock?: ")
    notValid = True
    while notValid:
        if isValid(iS):
            inStock.append(iS)
            notValid = False
        else:
            print("Please enter a number: ")
            iS = input()
    print("Item has been added.")

    #updates new list size
    mainList()

#function to delete items from the list 
def delItem():
    viewList()
    x = input("Please enter the number of item you would like to delete: ")
    L = len(productID)
    print("L is",L)
    L = int(L)

    #supposed to chech if input is 9 (not working)
    # notZero = True
    # while notZero:
    #     if x==0:
    #         print("0 is not a valid input. Please enter a valid number: ")
    #     else:
    #         notZero = False

    notValid = True
    while notValid:           
        if isValid(x):
            x = int(x)
            tooHigh = True
            while tooHigh:
                if int(x) > int(L):
                    print("Please choose from the available list (0-",L,"): ")
                    x = input()
                else:
                    tooHigh = False
            notValid = False
            x-=1
            del productID[x]
            del name[x]
            del size[x]
            del color[x]
            del inStock[x]
            del inventory[x]
            print("Item No.",x+1,"has been deleted.\nPress Return to view updated list")
            enter = input()
            if enter == "":
                viewList()
        else:
            x = input("Please enter the number of item you would like to delete: ")
    mainList()

#function that exports the updated list to .csv
def exportList():
    import csv
    exportedFile = "inventory.csv"
    range = len(productID)
    x = 0
    row = []
    with open(exportedFile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        while x < range:
            row.append(productID)
            row.append(name)
            row.append(size)
            row.append(color)
            row.append(inStock)
            writer.writerow(row)
            range-=1

#functions that shows available options
def options():
    option = input("Please select from the options below:\n1. View Inventory\n2.Add item\n3.Delete item\n4.Export: ")
    notValid = True
    while notValid:
        if isValid(option):
            option = int(option)
            notValid = False
            if option == 1:
                viewList()
                mainList()
            if option == 2:
                addItem()
            if option == 3:
                delItem()
            if option == 4:
                exportList()
        else:
            print("Please choose a number from the list above ONLY: ")
            option = input()
            
setList()
options()
#viewList()
