#imports all tkinter methods
from tkinter import *
import ListOptions
import sqlite3

#global variables
productID=[]
name=[]
size=[]
color=[]
inStock=[]
count = 0

#sets up connection to local database
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()
ListOptions.createTable(cursor)#creates a table data if it doesn't exit
ListOptions.readFromDB(productID,name,size,color,inStock,cursor)#read values in database  
print("inventory.db has been imported!")

#creates window object
window = Tk()
window.title("Inventory Manager")

def setUpMM():
    #defining title lables id,name,size,color,instock
    id = Label(window, text="Product ID")
    id.grid(row=0,column=0)

    nameLbl = Label(window, text="Name")
    nameLbl.grid(row=1,column=0)

    sizeLbl = Label(window,text="Size")
    sizeLbl.grid(row=0,column=2)

    colorLbl = Label(window,text="color")
    colorLbl.grid(row=1,column=2)

    instockLbl = Label(window,text="Availablity")
    instockLbl.grid(row=0,column=4)

    #defining text fields of id,name,size,color,instock
    id_field=StringVar()
    idEntry=Entry(window,textvariable=id_field)
    idEntry.grid(row=0,column=1)

    name_field=StringVar()
    nameEntry=Entry(window,textvariable=name_field)
    nameEntry.grid(row=1,column=1)

    size_field=StringVar()
    sizeEntry=Entry(window,textvariable=size_field)
    sizeEntry.grid(row=0,column=3)

    color_field=StringVar()
    colorEntry=Entry(window,textvariable=color_field)
    colorEntry.grid(row=1,column=3)

    instock_field=StringVar()
    instockEntry=Entry(window,textvariable=instock_field)
    instockEntry.grid(row=0,column=5)

    #defining listbox
    lbox = Listbox(window,height=6,width=50)
    lbox.grid(row=3,column=0,rowspan=5,columnspan=4)

    #attaching scrollbar
    sbar=Scrollbar(window,orient=VERTICAL)
    lbox['yscrollcommand'] = sbar.set
    sbar['command'] = lbox.yview
    sbar.grid(row=3,column=4,rowspan=4)

    #defining buttons
    createBtn=Button(window,text="Add Item",width=20)
    createBtn.grid(row=1,column=5)

    delBtn=Button(window,text="Delete Selected",width=20)
    delBtn.grid(row=3,column=5)

    editBtn=Button(window,text="Edit Selected",width=20)
    editBtn.grid(row=4,column=5)

    srchBtn=Button(window,text="Search",width=20)
    srchBtn.grid(row=5,column=5)

    xptBtn=Button(window,text="Export",width=20,command=lambda:ListOptions.exportList(productID,name,size,color,inStock))
    xptBtn.grid(row=6,column=5)

    exitBtn=Button(window,text="Exit",width=20,command=exit)
    exitBtn.grid(row=7,column=5)

    #adding values to list box
    count = 0
    while count < len(productID):
        lbox.insert(END,name[count])
        count+=1
    
setUpMM()
window.mainloop()
