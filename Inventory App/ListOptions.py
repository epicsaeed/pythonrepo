import subprocess
import os
import sqlite3
import time

def Testing():
    print("Testing is working")


def ImportTXTorDB():
    x = input("Please select an option below:\n1. Import data from txt file.\n2. Import data from database: ")
    notValid = True
    while notValid:
        if int(x)==1:
            notValid = False

        if int(x)==2:
            notValid = False
        else:
            print("Please insert a valid value: ")
            x = input()

#searches database by name of item
def searchDB(productID,name,size,color,inStock,cursor,conn):
    found = []
    count = 0
    name = input("Please enter a keyword: ")
    cursor.execute("SELECT * FROM data WHERE name LIKE ?",('%'+name+'%',))
    print("Results found for '",name,"': ")
    #adds all search results to a list 'found'
    for row in cursor.fetchall():
        found.append(row)
    if len(found) == 0:
        print("No elements found.")
        return None
    else:
        #prints search results
        print(len(found)," item/s found.")
        print("No.\tName\t\tProduct ID")
        while count < len(found):
            print(count+1,"\t",found[count][1].ljust(10),"\t",found[count][0])
            count+=1
    #options to delete/edit items found in search result
    print("Please select from the options below:\n1. Delete items\n2. Edit items: ")
    select = input()
    notValid = True
    while notValid:
        if select.isdigit() and select == '1' or select == '2':
            notValid = False
            if select == '1':
                item = input("Please enter the number of the item to be deleted: ")
                notValidNumber = True
                while notValidNumber:
                    if int(item) <= len(found):
                        notValidNumber = False
                        item = int(item)
                        ID = found[int(item)-1][0]
                        removeFromDB(ID,cursor,conn)
                        print("'",found[item-1][1], "' has been deleted.")
                    else:
                        item = input("Please enter a valid number")
            else:
                item = input("Please enter the number of the item to be edited: ")
                notValidNumber = True
                while notValidNumber:
                    if int(item) <= len(found):
                        notValidNumber = False
                        item = int(item)
                        pid = found[int(item)-1][0]
                        newInStock = input("Please enter the availability of the item: ")
                        notDigit = True
                        while notDigit:
                            if newInStock.isdigit():
                                notDigit = False
                                oldInStock = found[item-1][4]
                                newInStock = int(newInStock)
                                editInDB(oldInStock,newInStock,pid,cursor,conn)
                            else:
                                newInStock = input("Please enter a valid value: ")
        else:
            select = input("Please select a valid input: ")

#reads all input in database
def readFromDB(productID,name,size,color,inStock,cursor):
    #clears variablse
    # productID.clear()
    # name.clear()
    # size.clear()
    # color.clear()
    # inStock.clear()
    #fills up variables from DB
    cursor.execute('SELECT * FROM data')
    for row in cursor.fetchall():
        productID.append(row[0])
        name.append(row[1])
        size.append(row[2])
        color.append(row[3])
        inStock.append(row[4])

#creates a table if it does not exist
def createTable(curser):
    curser.execute('CREATE TABLE IF NOT EXISTS data(productid INTEGER, name TEXT, size TEXT, color TEXT, instock INTEGER)')

#used to add products into the database
def addToDB(p,n,s,c,stock,cursor,conn):
    cursor.execute("INSERT INTO data VALUES(:productid,:name,:size,:color,:instock)",{'productid':p,'name':n,'size':s,'color':c,'instock':stock})
    conn.commit()

#removed item of passed Product ID
def removeFromDB(p,cursor,conn):
    cursor.execute("DELETE FROM data WHERE  productid =?",(p,))
    conn.commit()

#Edits inStock value
def editInDB(oldInStock,newInStock,pid,cursor,conn):
    cursor.execute("UPDATE data SET instock =? WHERE instock =? AND productid =?",(newInStock,oldInStock,pid))
    conn.commit()

#shows the database
def viewDB(cursor):
    cursor.execute('SELECT * FROM data')
    for row in cursor.fetchall():
        print(row)

#returns true if a database exists
def ifDBExists():
    from pathlib import Path
    db = Path("/Users/saeed/pythonrepo/inventory.db")
    return db.is_file()

#this function allows users to edit product details such as inStock
def edit(productID,name,size,color,inStock,cursor,conn):
    viewList(productID,name,size,color,inStock)
    notValid = True
    L = len(productID)
    x = input("Please select the item you want to edit: ")
    oldInStock = 0
    while notValid:    
        if x.isdigit() and int(x) !=0 and int(x)<=int(L):
            x = int(x)
            oldInStock = inStock[x-1]
            notValid = False
            print("How much is in stock of item '",name[x-1],"' ?: ")
            availability = input()
            notInt = True
            while notInt:
                if availability.isdigit() or int(availability) == 0:
                    notInt = False
                    inStock[x-1] = availability 
                    print(name[x-1]," has been updated to ",availability," in stock.")
                    editInDB(oldInStock,availability,productID[x-1],cursor,conn)
                else:
                    availability = input("Please enter a valid value: ")
        else:
            x = input("Please enter a valid item number: ")

#shows the list of products
def viewList(productID,name,size,color,inStock):
    counter = 0
    #excludes the labels from inventory length
    r = len(productID)
    print("No.\tProductID\tName\t\tSize\tColor\tinStock")
    print('='*80)
    #prints all elements in the list
    while counter < r:
        #print(counter+1,".\t",productID[counter],"\t",name[counter],size[counter],"\t",color[counter],"\t",inStock[counter])
        print(counter+1,".\t",productID[counter],"\t",name[counter].ljust(15),size[counter],"\t",color[counter].ljust(7),"\t",inStock[counter])
        counter+=1
    
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

#function to add items to the list
def addItem(productID,name,size,color,inStock,cursor,conn):
    x = input("Please enter the product ID: ")
    notValid = True
    #checks if product ID is invalid (must be 7 digits)
    while notValid:
        if len(x) == 7 and x.isdigit():
            if int(x) in productID:
                print("Item already exists.")
                return None
            productID.append(x)
            notValid = False
        else:
            x = input("Product ID must be 7 digits: ")

    n = input("Please enter the name of the product: ")
    longName = True
    #ensures users input a valid,short name
    while longName:
        if n == "":
            n = "N/A"
            longName = False
            name.append("N/A")
        elif len(n)>15:
            n = input("Name must be 15 characters or less: ")
        else:
            longName = False
            name.append(n)

    #item size input field
    s = input("Please enter the size of the item: ")
    if s == "":
        s = "N/A"
        size.append("N/A")
    else:
        size.append(s)

    c = input("Please enter the color of the product: ")
    if c == "":
        c = "N/A"
        color.append("N/A")
    else:
        color.append(c)

    iS = input("How many of this item is in stock?: ")
    notValid = True
    while notValid:
        if iS.isdigit():
            inStock.append(iS)
            notValid = False
        else:
            print("Please enter a number: ")
            iS = input()
    addToDB(x,n,s,c,iS,cursor,conn)
    print("Item has been added.")

def mainListDB(productID,name,size,color,inStock,cursor,conn):
    r = input("press return to go to main list")
    if r == "":
        optionsDB(productID,name,size,color,inStock,cursor,conn)

#functions that shows available options for DB input
def optionsDB(productID,name,size,color,inStock,cursor,conn):
    option = input("Please select from the options below:\n1. View Inventory\n2. Add item\n3. Delete item\n4. Export\n5. Edit: \n6. Search:\n0. Exit ")
    notValid = True
    while notValid:
        if option.isdigit() and int(option) < 7:
            option = int(option)
            notValid = False
            if option == 1:
                viewList(productID,name,size,color,inStock)
                mainListDB(productID,name,size,color,inStock,cursor,conn)
            if option == 2:
                addItem(productID,name,size,color,inStock,cursor,conn)
                mainListDB(productID,name,size,color,inStock,cursor,conn)
            if option == 3:
                delItem(productID,name,size,color,inStock,cursor,conn)
                mainListDB(productID,name,size,color,inStock,cursor,conn)
            if option == 4:
                exportList(productID,name,size,color,inStock)
                mainListDB(productID,name,size,color,inStock,cursor,conn)
            if option == 5:
                edit(productID,name,size,color,inStock,cursor,conn)
                mainListDB(productID,name,size,color,inStock,cursor,conn)
            if option == 6:
                searchDB(productID,name,size,color,inStock,cursor,conn)
                readFromDB(productID,name,size,color,inStock,cursor)
                mainListDB(productID,name,size,color,inStock,cursor,conn)
            if option == 0:
                exit()
        else:
            print("Please choose a number from the list above ONLY: ")
            option = input()
            
#function to delete items from the list 
def delItem(productID,name,size,color,inStock,cursor,conn):
    viewList(productID,name,size,color,inStock)
    notValid = True
    L = len(productID)
    if L == 0:
        print("No items available on the list.")
        return None
    x = input("Please enter the number of item you would like to delete: ")       
    while notValid:    
        if x.isdigit() and int(x) !=0 and int(x)<=int(L):
            x = int(x)
            #deletes the selected item no.        
            notValid = False
            x-=1    

            #confirm delete
            print("ARE YOU SURE YOU WANT TO DELETE '",name[x],"' ?\nPRESS RETURN TO CONFIRM")
            sure = input()
            if sure!="":
              break

            ID = productID[x]
            #deleting selected row elements from memory
            del productID[x]
            del name[x]
            del size[x]
            del color[x]
            del inStock[x]

            #deleting row from DB
            removeFromDB(ID,cursor,conn)

            print("Item No.",x+1," has been deleted.\nPress Return to view updated list")
            enter = input()
            if enter == "":
                viewList(productID,name,size,color,inStock) 
        else:
            x = input("Please enter a valid item number: ")

#function that exports the updated list to .csv
def exportList(productID,name,size,color,inStock):
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