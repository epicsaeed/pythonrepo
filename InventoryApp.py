
#opens file and create a list of each line
with open('inventory.txt') as f:
    inventory = list(f)

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
        #splits each line by tabs and save in a temp list
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
        print(s)    #for testing
        #clears temp list
        s.clear()
    print("Inventory has been updated!")


def viewList():
    counter = 0
    print("ProductID       Name        Size        Color       inStock")
    print("============================================================")
    while counter < len(inventory)-1:
        print(productID[counter],"      ",name[counter],"      ",size[counter],"      ",color[counter],"      ",inStock[counter])
        counter+=1

def isValid(s): 
    try:
        int(s)
        return True
    except ValueError:
        return False


def addItem():
    print(1)

def delItem():
    print(0)

def exportList():
    print(0)

def options():
    option = input("Please select from the options below:\n1. View Inventory\n2.Add item\n3.Delete item\n4.Export")
    notValid = True
    while notValid:
        if isValid(option):
            option = int(option)
            notValid = False
            if option == 1:
                viewList()
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
#options()
