import subprocess
import os
import sqlite3
import DatabaseOptions
import time

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

#reads all input in database
def readFromDB(productID,name,size,color,inStock,cursor):
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
    # cursor.close()
    # conn.close()

#removed item of passed Product ID
def removeFromDB(p,cursor,conn):
    cursor.execute("DELETE FROM data WHERE  productid =?",(p,))
    conn.commit()

#Edits inStock value
def editInDB(oldInStock,newInStock,cursor,conn):
    cursor.execute('UPDATE data SET value =(?) WHERE value =(?)',(newInStock,newInStock))
    conn.commit()

#shows the database
def viewDB(cursor):
    cursor.execute('SELECT * FROM data')
    for row in cursor.fetchall():
        print(row)

#returns true if a database exists
def ifDBExists():
    from pathlib import Path
    db = Path("/Users/saeed/pythonrepo/Inventory App/inventory.db")
    return db.is_file()

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
                    #mainList(inventory,productID,name,size,color,inStock)
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
        print(counter+1,".\t",productID[counter],"\t",name[counter].ljust(15),size[counter],"\t",color[counter],"\t",inStock[counter])
        counter+=1
    

#function to add items to the list
def addItem(productID,name,size,color,inStock,cursor,conn):
    x = input("Please enter the product ID: ")
    notValid = True
    #checks if product ID is invalid (must be 7 digits)
    while notValid:
        if len(x) == 7 and x.isdigit():
            if x in productID:
                print("Item already exists.")
                mainListDB(productID,name,size,color,inStock,cursor,conn)
            productID.append(x)
            notValid = False
        else:
            x = input("Product ID must be 7 digits: ")

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

    #item size input field
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
        if iS.isdigit():
            inStock.append(iS)
            notValid = False
        else:
            print("Please enter a number: ")
            iS = input()
    addToDB(x,n,s,c,iS,cursor,conn)
    print("Item has been added.")
    mainListDB(productID,name,size,color,inStock,cursor,conn)

def mainListDB(productID,name,size,color,inStock,cursor,conn):
    r = input("press return to go to main list")
    if r == "":
        optionsDB(productID,name,size,color,inStock,cursor,conn)

#functions that shows available options for DB input
def optionsDB(productID,name,size,color,inStock,cursor,conn):
    option = input("Please select from the options below:\n1. View Inventory\n2. Add item\n3. Delete item\n4. Export\n5. Edit: \n6. Exit: ")
    notValid = True
    while notValid:
        if option.isdigit() and int(option) < 7 and int(option) != 0:
            option = int(option)
            notValid = False
            if option == 1:
                viewList(productID,name,size,color,inStock)
                mainListDB(productID,name,size,color,inStock,cursor,conn)
            if option == 2:
                addItem(productID,name,size,color,inStock,cursor,conn)
            if option == 3:
                delItem(productID,name,size,color,inStock,cursor,conn)
            if option == 4:
                exportList(productID,name,size,color,inStock)
            # if option == 5:
            #     edit(inventory,productID,name,size,color,inStock)
            # if option == 6:
            #     exit()
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
        mainListDB(productID,name,size,color,inStock,cursor,conn)
    x = input("Please enter the number of item you would like to delete: ")       
    while notValid:    
        if x.isdigit() and int(x) !=0 and int(x)<=int(L):
            x = int(x)
            #deletes the selected item no.        
            notValid = False
            x-=1    

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
    
    mainListDB(productID,name,size,color,inStock,cursor,conn)

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
    #mainListDB(productID,name,size,color,inStock,cursor,conn)
    
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