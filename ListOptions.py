
import errorCheck

#this functions checks if input file has one tab or multiple tabs and calls set list accordingly
def checkFile(inventory,productID,name,size,color,inStock):
    temp = []
    for word in inventory[2].split("\t"):
        temp.append(word)
    if '' in temp:
        setListMulti(inventory,productID,name,size,color,inStock)
    else:
        setList(inventory,productID,name,size,color,inStock)

#this function reads opened file and assigns each row to its appropriate value in the lists above.(for unknown tabs)
def setListMulti(inventory,productID,name,size,color,inStock):  
    #variables 
    s = []
    counter = 2

    #reads inventory list line by line
    while counter < len(inventory) :
        #removes all spaces from each line in inventory and saves it in a temp list 's'
        s = list(filter(None,inventory[counter].split("\t")))

        #removes \n from last element
        s[-1] = s[-1].strip()

        #if list(s) contains 4 elements only, it means that an empty name was deleted and
        #it should be replaced with an N/A
        if len(s) == 4:
            name.append("N/A")
        else:
            productID.append(s[0])
            name.append(s[1])
            size.append(s[2])
            color.append(s[3])
            inStock.append(s[4])

        #incr. counter
        counter+=1

        #clears temp list
        s.clear()
    print("\n\nInventory_updated.txt has been Imported!")
    print(productID)

#this function reads opened file and assigns each row to its appropriate value in the lists above.(for single tabs)
def setList(inventory,productID,name,size,color,inStock):  
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

        #clears temp list
        print(s)
        s.clear()
    print("\nInventory.txt has been Imported!")

#shows the list of products
def viewList(productID,name,size,color,inStock):
    counter = 0
    #excludes the labels from inventory length
    r = len(productID)
    print(r)
    
    print("No.     ProductID       Name        Size        Color       inStock")
    print("===================================================================")
    #prints all elements in the list
    while counter < r:
        print(counter+1,".      ",productID[counter],"      ",name[counter],"      ",size[counter],"      ",color[counter],"      ",inStock[counter])
        counter+=1

#function to add items to the list
def addItem(inventory,productID,name,size,color,inStock):
    x = input("Please enter the product ID: ")
    notValid = True
    update = "" #temp string

    #checks if product ID is invalid
    while notValid:
        if len(x) != 7:
            x = input("product ID must be 7 digits: ")
        else:
            productID.append(x)
            notValid = False
    update=update+x+'\t'    #updates temporary string

    n = input("Please enter the name of the product: ")
    if n == "":
        name.append("N/A")
    else:
        name.append(n)
    update=update+n+'\t'

    s = input("Please enter the size of the item: ")
    if s == "":
        size.append("N/A")
    else:
        size.append(s)
    update=update+s+'\t'

    c = input("Please enter the color of the product: ")
    if c == "":
        color.append("N/A")
    else:
        color.append(c)
    update=update+c+'\t'

    iS = input("How many of this item is in stock?: ")
    notValid = True
    while notValid:
        if errorCheck.isValid(iS):
            inStock.append(iS)
            notValid = False
        else:
            print("Please enter a number: ")
            iS = input()
    update=update+iS+'\n'

    print("Item has been added.")
    inventory.append(update)    #appends opened list with temp string
    backup(inventory)
    mainList(inventory,productID,name,size,color,inStock)

def mainList(inventory,productID,name,size,color,inStock):
    r = input("press return to go to main list")
    if r == "":
        options(inventory,productID,name,size,color,inStock)

def backup(inventory):
    with open('inventoryBackup.txt','r+') as b:
            b.writelines(["%s\n" % item  for item in inventory])

#functions that shows available options
def options(inventory,productID,name,size,color,inStock):
    option = input("Please select from the options below:\n1. View Inventory\n2. Add item\n3. Delete item\n4. Export\n5. Exit: ")
    notValid = True
    while notValid:
        if errorCheck.isValid(option) and int(option) < 6 and int(option) != 0:
            option = int(option)
            notValid = False
            if option == 1:
                viewList(productID,name,size,color,inStock)
                mainList(inventory,productID,name,size,color,inStock)
            if option == 2:
                addItem(inventory,productID,name,size,color,inStock)
            if option == 3:
                delItem(inventory,productID,name,size,color,inStock)
            if option == 4:
                exportList(inventory,productID,name,size,color,inStock)
            if option == 5:
                exit()
        else:
            print("Please choose a number from the list above ONLY: ")
            option = input()

#function to delete items from the list 
def delItem(inventory,productID,name,size,color,inStock):
    viewList(productID,name,size,color,inStock)
    notValid = True
    L = len(productID)
    x = input("Please enter the number of item you would like to delete: ")       
    while notValid:    
        if errorCheck.isValid(x) and int(x) !=0 and int(x)<int(L):
            x = int(x)
            #deletes the selected item no.        
            notValid = False
            x-=1
            #creating temp backup
            del inventory[x+2]  
            backup(inventory)    
            #deleting selected row elements
            del productID[x]
            del name[x]
            del size[x]
            del color[x]
            del inStock[x]

            print("Item No.",x+1," has been deleted.\nPress Return to view updated list")
            enter = input()
            if enter == "":
                viewList(productID,name,size,color,inStock) 
        else:
            x = input("Please enter a valid item number: ")

    mainList(inventory,productID,name,size,color,inStock)

#function that exports the updated list to .csv
def exportList(inventory,productID,name,size,color,inStock):
    import csv
    exportedFile = "inventory.csv"
    data = createListForExport(productID,name,size,color,inStock)
    with open(exportedFile, "w",newline = '') as output:
        a = csv.writer(output,delimiter=',')
        headline = [['Product ID','Name','Size','Color','Availability'],]
        a.writerows(headline)
        a.writerows(data)
    mainList(inventory,productID,name,size,color,inStock)

#creates a list fot exporting
def createListForExport(productID,name,size,color,inStock):
    L = len(name)
    count = 0
    list = [[]]
    while count < L:
        list = list + [[productID[count],name[count],size[count],color[count],inStock[count]]]
        count+=1
    return list
