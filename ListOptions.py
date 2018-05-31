
import errorCheck

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
    option = input("Please select from the options below:\n1. View Inventory\n2.Add item\n3.Delete item\n4.Export\n5.Exit: ")
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
    x = input("Please enter the number of item you would like to delete: ")
    L = len(productID)
    L = int(L)

    notValid = True
    while notValid:           
        if errorCheck.isValid(x):
            x = int(x)
            
            #checks if user selected 0
            isZero = True
            while isZero:
                if int(x)==0:
                    x = input("0 is not a valid input. Please try again: ")
                else:
                    isZero = False

            #checks if user selected a number too high from the list
            tooHigh = True
            while tooHigh:
                if int(x) > int(L):
                    print("Please choose from the available list (0-",L,"): ")
                    x = input()
                else:
                    tooHigh = False

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

            print("Item No.",x+2," has been deleted.\nPress Return to view updated list")
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
     