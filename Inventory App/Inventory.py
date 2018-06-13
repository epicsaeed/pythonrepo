import sqlite3
import ListOptions

#allows user to select input source
source = input("Please select an input source\n1. Database\n2. Text file: ")
notValid = True
while notValid:
    if source.isdigit():
        if source == '1':
            notValid = False
            source = "DB"
        elif source == '2':
            notValid = False
            source = "TXT"
        else:
            source = input("Please select from the numbers above: ")
    else:
        source = input("Please select from the numbers above: ")

#global variables
productID=[]
name=[]
size=[]
color=[]
inStock=[]
count = 0

#sequence to import from Database
if source == "DB":
    #sets up connection to local database
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    ListOptions.createTable(cursor)#creates a table data if it doesn't exit
    ListOptions.readFromDB(productID,name,size,color,inStock,cursor)#read values in database  
    print("inventory.db has been imported!")
    ListOptions.optionsDB(productID,name,size,color,inStock,cursor,conn)#lists options 
#sequence to import from text file
else:
    import ListOptions 
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    #checks if the DB already exists or no
    if ListOptions.ifDBExists():
        #DB exist so no need to read again.
        ListOptions.readFromDB(productID,name,size,color,inStock,cursor)#read values in database  
        ListOptions.optionsDB(productID,name,size,color,inStock,cursor,conn)
    else:   #this sequence is never executed as 'inventory.db' already exists
        #sequence if DB doesn't exist
        #shows a dialog window for user to select text file
        Tk().withdraw()
        path = askopenfilename() # show an "Open" dialog box and return the path to the selected file

        #opens file and create a list of each line
        with open(path,'r+') as f:
            inventory = list(f)

        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        ListOptions.setListMulti(inventory,productID,name,size,color,inStock)
        ListOptions.createTable(cursor)#creates a table data if it doesn't exit
        #adds items from text file to db(to be ran once)
        count = 0
        while count < len(name):
            ListOptions.addToDB(productID[count],name[count],size[count],color[count],inStock[count],cursor,conn)
            count+=1
        ListOptions.optionsDB(productID,name,size,color,inStock,cursor,conn)