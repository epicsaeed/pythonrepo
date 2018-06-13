#imports all tkinter methods
from tkinter import *
from tkinter import messagebox
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

#attaches multiple functions to one button
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

#adds item:
def addItem():
    id = idEntry.get()
    notValid = True
    #checks if product ID is invalid (must be 7 digits)
    while notValid:
        if len(id) == 7 and id.isdigit():
            if int(id) in productID:
                messagebox.showerror("Duplicate", "Item already exists")
                return None
            productID.append(id)
            notValid = False
        else:
            messagebox.showerror("Error", "Product ID must be 7 digits.")

    n = nameEntry.get()
    if n == "":
        n = "N/A"
        name.append("N/A")
    else:
        name.append(n)

    #item size input field
    s = sizeEntry.get()
    if s == "":
        s = "N/A"
        size.append("N/A")
    else:
        size.append(s)

    c = colorEntry.get()
    if c == "":
        c = "N/A"
        color.append("N/A")
    else:
        color.append(c)

    iS = instockEntry.get()
    notValid = True
    while notValid:
        if iS.isdigit():
            inStock.append(iS)
            notValid = False
        else:
            messagebox.showerror("Availability Error", "Please enter a number")
    ListOptions.addToDB(productID,name,size,color,inStock,cursor,conn)
    print("Item has been added.")
    messagebox.showerror("Done", "Item has been added")

#displays details of item selected in scroll menu
def viewDetails(N):
    #clearing textfields
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    sizeEntry.delete(0,END)
    colorEntry.delete(0,END)
    instockEntry.delete(0,END)

    #printing details
    index = name.index(N)
    idEntry.insert("end",productID[index])
    nameEntry.insert("end",name[index])
    sizeEntry.insert("end",size[index])
    colorEntry.insert("end",color[index])
    instockEntry.insert("end",inStock[index])

#adding initial names to list box
def addInitialNames():
    count = 0
    while count < len(productID):
        lbox.insert(END,name[count])
        count+=1

#search function
def search():
    SearchBar = Tk()
    SearchBar.title("Search")
    srchBox = Listbox(SearchBar,height=6,width=25)
    srchBox.grid(row=3,column=0,rowspan=4)
    #search = StringVar()
    srchEntry=Entry(SearchBar,textvariable=search)
    srchEntry.grid(row=0,column=0,columnspan=4)
    srchBtn = Button(SearchBar,text="Search",width=20,command=lambda:sAction(srchEntry.get(),srchBox))
    srchBtn.grid(row=1,column=0,columnspan=4)
    vBtn = Button(SearchBar,text="View Details",width=20,command=lambda:viewDetails(srchBox.get(ANCHOR)))
    vBtn.grid(row=2,column=0,columnspan=4)
    exitBtn = Button(SearchBar,text="Close",width=20,command=lambda:SearchBar.destroy())
    exitBtn.grid(row=8,column=0,columnspan=4)
    SearchBar.mainloop()

def sAction(v,srchBox):
    if v != "":
        srchBox.delete('0','end')
        name = str(v)
        found = []
        count = 0
        cursor.execute("SELECT * FROM data WHERE name LIKE ?",('%'+name+'%',))
        #print("Results found for '",name,"': ")
        #adds all search results to a list 'found'
        for row in cursor.fetchall():
            found.append(row)
        if len(found) == 0:
            srchBox.insert(END,"No Elements Found.")
            return None
        else:
            #prints search results
            srchBox.insert(END,"Results Found:")
            while count < len(found):
                srchBox.insert(END,found[count][1])
                count+=1
    else:
        messagebox.showerror("Error", "Please enter a value")

#creates window object
window = Tk()
window.title("Inventory Manager")

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
addInitialNames()

#attaching scrollbar
sbar=Scrollbar(window,orient=VERTICAL)
lbox['yscrollcommand'] = sbar.set
sbar['command'] = lbox.yview
sbar.grid(row=3,column=4,rowspan=4)

#defining buttons
addBtn=Button(window,text="Add new Item",width=20,command=lambda:addBtn)
addBtn.grid(row=1,column=5)

viewBtn=Button(window,text="View Details",width=20,command=lambda:viewDetails(lbox.get(ANCHOR)))
viewBtn.grid(row=2,column=5)

delBtn=Button(window,text="Delete Selected",width=20)
delBtn.grid(row=3,column=5)

editBtn=Button(window,text="Edit Selected",width=20)
editBtn.grid(row=4,column=5)

srchBtn=Button(window,text="Search",width=20,command=lambda:search())
srchBtn.grid(row=5,column=5)

xptBtn=Button(window,text="Export",width=20,command=lambda:ListOptions.exportList(productID,name,size,color,inStock))
xptBtn.grid(row=6,column=5)

exitBtn=Button(window,text="Exit",width=20,command=exit)
exitBtn.grid(row=7,column=5)

window.mainloop()



