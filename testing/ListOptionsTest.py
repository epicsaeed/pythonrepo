import subprocess
import os



#this function allows users to edit product details such as inStock
def edit(inventory,productID,name,size,color,inStock):
    viewList(productID,name,size,color,inStock)
    notValid = True
    L = len(productID)
    x = input("Please select the item you want to edit: ")
    while notValid:    
        if x.isdigit() and int(x) !=0 and int(x)<=int(L):
            x = int(x)
            notValid = False
            print("How much is in stock of item '",name[x-1],"' ?: ")
            availability = input()
            notInt = True
            while notInt:
                if availability.isdigit() or int(availability) == 0:
                    notInt = False
                    inStock[x-1] = availability 
                    print(name[x-1]," has been updated to ",availability," in stock.")
                    mainList(inventory,productID,name,size,color,inStock)
                else:
                    availability = input("Please enter a valid value: ")
        else:
            x = input("Please enter a valid item number: ")

#this functions restores any changes (add/del) performed in the previous run
def restore(productID,name,size,color,inStock):
    added = []
    addedID = []
    deleted = []
    path = '/Users/saeed/pythonrepo/Inventory App/inventoryBackup.txt'
    file = open(path, 'r')
    #adds the product ID's of items added/deleted to a list
    for line in file:
        if line[0] == 'A':
            added.append(line[1:].rstrip())
            addedID.append(line[1:8])
        elif line[0] == 'D':
            deleted.append(line[1:8])
    print("\nProduct ID of items added on the last run: ",addedID)
    print("\nProduct ID of items deleted on the last run: ",deleted,"\n")
    print("Would you like to add these changes to the current inventory list?")
    x = input()
    notValid = True
    while notValid:
        if x == 'y' or x == 'Y':
            print("Inventory List has been updated!")
            notValid = False
            #update deleted items
            count = 0
            while count < len(deleted):
                index = productID.index(deleted[count])
                del productID[index]
                del name[index]
                del size[index]
                del color[index]
                del inStock[index]
                count+=1
            #update added items
            count = 0
            a = []
            while count < len(added):
                a = added[count].split("\t")
                #print("A is ",a)
                productID.append(a[0])
                name.append(a[1])
                size.append(a[2])
                color.append(a[3])
                inStock.append(a[4])
                count+=1
        elif x == 'n' or x == 'N':
            notValid = False
        else:
            x = input("Please select Y or N: ")

#this function reads opened file and assigns each row to its appropriate value in the lists above.(for unknown tabs)
def setListMulti(inventory,productID,name,size,color,inStock):  
    #variables 
    s = []
    counter = 2

    #reads inventory list line by line till the last line
    while counter < len(inventory) :
        #removes all spaces from each line in inventory and saves it in a temp list 's'
        s = list(filter(None,inventory[counter].split("\t")))

        #removes \n from last element
        s[-1] = s[-1].strip()

        #if list(s) contains 4 elements only, it means that an empty name was deleted and
        #it should be replaced with an N/A
        if len(s) == 4:
            productID.append(s[0])
            name.append("N/A")
            size.append(s[1])
            color.append(s[2])
            inStock.append(s[3])
        else:
            productID.append(s[0])
            n = s[1]    
            name.append(n[:10]) #take only 10 characters of the name
            size.append(s[2])
            color.append(s[3])
            inStock.append(s[4])

        #incr. counter
        counter+=1

        #clears temp list
        s.clear()
    print("\nInventory.txt has been Imported!\nNote: All names of items have been shortened for formatting")

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
        n = s[1]
        name.append(n[:10]) #take only 10 characters of the name
        size.append(s[2])
        color.append(s[3])
        inStock.append(s[4])
        counter+=1

        #clears temp list
        s.clear()
    print("\nInventory.txt has been Imported!\nNote: All names of items have been shortened for formatting")

#shows the list of products
def viewList(productID,name,size,color,inStock):
    counter = 0
    #excludes the labels from inventory length
    r = len(productID)
    print(r)
    
    print("No.\tProductID\tName\t\tSize\tColor\tinStock")
    print('='*80)
    #prints all elements in the list
    while counter < r:
        #print(counter+1,".\t",productID[counter],"\t",name[counter],size[counter],"\t",color[counter],"\t",inStock[counter])
        print(counter+1,".\t",productID[counter],"\t",name[counter].ljust(15),size[counter],"\t",color[counter],"\t",inStock[counter])
        counter+=1

#function to add items to the list
def addItem(inventory,productID,name,size,color,inStock):
    x = input("Please enter the product ID: ")
    notValid = True
    update = "" #temp string
    adding = True
    #checks if product ID is invalid (must be 7 digits)
    while notValid:
        if len(x) == 7 and x.isdigit():
            if x in productID:
                print("Item already exists.")
                mainList(inventory,productID,name,size,color,inStock)
            productID.append(x)
            notValid = False
        else:
            x = input("Product ID must be 7 digits: ")

    update=update+x+'\t'    #updates temporary string

    n = input("Please enter the name of the product: ")
    longName = True
    #ensures users input a valid,short name
    while longName:
        if n == "":
            longName = False
            name.append("N/A")
        elif len(n)>15:
            n = input("Name must be 15 characters or less: ")
        else:
            longName = False
            name.append(n)
    update=update+n.ljust(15)+'\t\t'

    #item size input field
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
        if iS.digit():
            inStock.append(iS)
            notValid = False
        else:
            print("Please enter a number: ")
            iS = input()
    update=update+iS+'\n'
    print("Item has been added.")
    inventory.append(update)    #appends opened list with temp string
    backup(x,adding,productID,name,size,color,inStock)
    mainList(inventory,productID,name,size,color,inStock)

#functions that performs as a home button
def mainList(inventory,productID,name,size,color,inStock):
    r = input("press return to go to main list")
    if r == "":
        options(inventory,productID,name,size,color,inStock)

#function that creates temp .txt backup file
def backup(item,adding,productID,name,size,color,inStock):
    with open('inventoryBackup.txt','a') as b:
        if adding:
            index = productID.index(item)
            #x=b.read()+'A'+item+'\n'
            x='\n'+'A'+item+'\t'+name[index]+'\t'+size[index]+'\t'+color[index]+'\t'+inStock[index]
            #b.flush()
            b.write(x)
        else:
            #x=b.read()+'D'+item+'\n'
            #b.flush()
            x='\n'+'D'+item
            b.write(x)

#functions that shows available options
def options(inventory,productID,name,size,color,inStock):
    option = input("Please select from the options below:\n1. View Inventory\n2. Add item\n3. Delete item\n4. Export\n5. Edit: \n6. Exit: ")
    notValid = True
    while notValid:
        if option.isdigit() and int(option) < 7 and int(option) != 0:
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
                edit(inventory,productID,name,size,color,inStock)
            if option == 6:
                exit()
        else:
            print("Please choose a number from the list above ONLY: ")
            option = input()

#function to delete items from the list 
def delItem(inventory,productID,name,size,color,inStock):
    viewList(productID,name,size,color,inStock)
    notValid = True
    adding = False
    L = len(productID)
    if L == 0:
        print("No items available on the list.")
        mainList(inventory,productID,name,size,color,inStock)
    x = input("Please enter the number of item you would like to delete: ")       
    while notValid:    
        if x.isdigit() and int(x) !=0 and int(x)<=int(L):
            x = int(x)
            #deletes the selected item no.        
            notValid = False
            x-=1
            #creating temp backup
            del inventory[x+2]  
            backup(productID[x],adding,productID,name,size,color,inStock)    
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
        headline = [["No.",'Product ID','Name','Size','Color','Availability'],]
        a.writerows(headline)
        a.writerows(data)
    print("'inventory.csv' has been exported.\n")
    runFile("inventory.csv")
    mainList(inventory,productID,name,size,color,inStock)
    
#creates a list fot exporting
def createListForExport(productID,name,size,color,inStock):
    L = len(name)
    count = 0
    list = [[]]
    while count < L:
        list = list + [[count+1,productID[count],name[count],size[count],color[count],inStock[count]]]
        count+=1
    return list

#opens exported csv file with default application 
def runFile(filename):
    try:
        os.startfile(filename)
    except AttributeError:
        subprocess.call(['open', filename])