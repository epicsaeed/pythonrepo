#imports all tkinter methods
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
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

def delete(lbox):
    index = name.index(lbox.get(ANCHOR))
    ID = productID[index]
    s = str(name[index]) + " has been deleted."
    #Delete from boxlist
    lbox.delete(ANCHOR)

    #delete from variables
    del productID[index]
    del name[index]
    del size[index]
    del color[index]
    del inStock[index]

    #delete fro DB
    ListOptions.removeFromDB(ID,cursor,conn)
    
    messagebox.showerror("Delete",s)

def addWindow():
    addwin= Tk()
    addwin.title("Add Item")

    #setting up labels
    name = Label(addwin, text="NAME")
    name.grid(row=0,column=0)

    id = Label(addwin, text="PRODUCT ID")
    id.grid(row=1,column=0)

    sizeLbl = Label(addwin,text="SIZE")
    sizeLbl.grid(row=2,column=0)

    colorLbl = Label(addwin,text="COLOR")
    colorLbl.grid(row=3,column=0)

    instockLbl = Label(addwin,text="AVAILABILITY")
    instockLbl.grid(row=4,column=0)

    #setting up text fields
    name_field=StringVar()
    nameEntry=Entry(addwin,textvariable=name_field)
    nameEntry.grid(row=0,column=1)

    id_field=StringVar()
    idEntry=Entry(addwin,textvariable=id_field)
    idEntry.grid(row=1,column=1)

    size_field=StringVar()
    sizeEntry=Entry(addwin,textvariable=size_field)
    sizeEntry.grid(row=2,column=1)

    color_field=StringVar()
    colorEntry=Entry(addwin,textvariable=color_field)
    colorEntry.grid(row=3,column=1)

    instock_field=StringVar()
    instockEntry=Entry(addwin,textvariable=instock_field)
    instockEntry.grid(row=4,column=1)

    #set up button
    aBtn = Button(addwin,text="Add Item",width=30,command=lambda:Add(nameEntry.get(),idEntry.get(),sizeEntry.get(),colorEntry.get(),instockEntry.get(),addwin))
    aBtn.grid(row=5,column=0,columnspan=4)

    addwin.mainloop()

#clears text fields
def clear():
    #enabling textfields for writing
    idEntry.configure(state="normal")
    sizeEntry.configure(state="normal")
    colorEntry.configure(state="normal")
    instockEntry.configure(state="normal")

    idEntry.delete(0,END)
    sizeEntry.delete(0,END)
    colorEntry.delete(0,END)
    instockEntry.delete(0,END)

    #disabling textfields for writing
    idEntry.configure(state="readonly")
    sizeEntry.configure(state="readonly")
    colorEntry.configure(state="readonly")
    instockEntry.configure(state="readonly")

#attaches multiple functions to one button
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def Add(n,ID,s,c,instock,win):
    Valid = True
    if len(ID) == 7 and ID.isdigit():
        if int(ID) in productID:
            messagebox.showerror("Duplicate", "Item already exists")
            win.destroy()
        elif n in name:
            messagebox.showerror("Duplicate", "Item of this name already exists")
            win.destroy()
        elif instock=="":
            messagebox.showerror("Error", "Please enter a value for availability")
            win.destroy()
        else:
            Valid = False
    else:
        messagebox.showerror("Error", "Product ID must be 7 digits")
        win.destroy()
        
    if n=="":
        n="N/A"

    if s=="":
        s="N/A"

    if c=="":
        c="N/A"
    if Valid:
        #add to boxlist
        lbox.insert(END,n)

        #add details to variables
        productID.append(ID)
        name.append(n)
        size.append(s)
        color.append(c)
        inStock.append(instock)

        #add to DB
        ListOptions.addToDB(ID,n,s,c,instock,cursor,conn)
        messagebox.showerror("Done", "Item has been added")
        win.destroy()

#displays details of item selected in scroll menu
def viewDetails(N):

    #enabling textfields for writing
    idEntry.configure(state="normal")
    sizeEntry.configure(state="normal")
    colorEntry.configure(state="normal")
    instockEntry.configure(state="normal")

    #clearing textfields
    idEntry.delete(0,END)
    sizeEntry.delete(0,END)
    colorEntry.delete(0,END)
    instockEntry.delete(0,END)

    #printing details
    index = name.index(N)
    idEntry.insert("end",productID[index])
    sizeEntry.insert("end",size[index])
    colorEntry.insert("end",color[index])
    instockEntry.insert("end",inStock[index])

    #disabling textfields for writing
    idEntry.configure(state="readonly")
    sizeEntry.configure(state="readonly")
    colorEntry.configure(state="readonly")
    instockEntry.configure(state="readonly")

#adding initial names to list box
def addInitialNames():
    count = 0
    while count < len(productID):
        lbox.insert(END,name[count])
        count+=1
    s = str(len(name)) + " Items have been imported from inventory.db"
    messagebox.showerror("Import",s)

#search window
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

#search logic
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

def EditWin(selectedItem):
    
    i = name.index(selectedItem)

    editWin = Tk()
    editWin.title("Edit Item")

    NameLbl = Label(editWin,text="Name:")
    NameLbl.grid(row=0,column=0)

    name_field=StringVar()
    NameEntry = Entry(editWin,textvariable=name_field)
    NameEntry.grid(row=0,column=1)
    NameEntry.insert(END,selectedItem)
    

    editLbl = Label(editWin,text="Availability:")
    editLbl.grid(row=1,column=0)

    edit_field=StringVar()
    editEntry = Entry(editWin,textvariable=edit_field)
    editEntry.grid(row=1,column=1)

    EditBtn = Button(editWin,text="Apply Changes",command=lambda:Edit(i,editEntry))
    EditBtn.grid(row=2,column=0,columnspan=2)

    NameEntry.configure(state="disabled")    
    
def Edit(i,editEntry):
    
    new = int(editEntry.get())
    old = inStock[i]

    #edit in variables
    inStock[i]=new

    #edit in DB
    ListOptions.editInDB(old,new,productID[i],cursor,conn)
    messagebox.showerror("Done", "Item has been Edited")

#creates window object
window = Tk()
window.title("INVENTORY MANAGER")


#defining title lables id,name,size,color,instock
id = Label(window, text="PRODUCT ID")
id.grid(row=0,column=0)

sizeLbl = Label(window,text="SIZE")
sizeLbl.grid(row=0,column=2)

colorLbl = Label(window,text="COLOR")
colorLbl.grid(row=1,column=2)

instockLbl = Label(window,text="AVAILABILITY")
instockLbl.grid(row=1,column=0)

#defining text fields of id,name,size,color,instock
id_field=StringVar()
idEntry=Entry(window,textvariable=id_field)
idEntry.grid(row=0,column=1)
idEntry.configure(state="readonly")

size_field=StringVar()
sizeEntry=Entry(window,textvariable=size_field)
sizeEntry.grid(row=0,column=3)
sizeEntry.configure(state="readonly")

color_field=StringVar()
colorEntry=Entry(window,textvariable=color_field)
colorEntry.grid(row=1,column=3)
colorEntry.configure(state="readonly")

instock_field=StringVar()
instockEntry=Entry(window,textvariable=instock_field)
instockEntry.grid(row=1,column=1)
instockEntry.configure(state="readonly")

#defining listbox
lbox = Listbox(window,height=6,width=50)
lbox.grid(row=3,column=0,rowspan=7,columnspan=4)
addInitialNames()

#attaching scrollbar
sbar=Scrollbar(window,orient=VERTICAL)
lbox['yscrollcommand'] = sbar.set
sbar['command'] = lbox.yview
sbar.grid(row=3,column=4,rowspan=4)

#defining buttons
clrBtn=Button(window,text="Clear Fields",width=20,command=lambda:clear())
clrBtn.grid(row=1,column=5)

addBtn=Button(window,text="Add new Item",width=20,command=lambda:addWindow())
addBtn.grid(row=0,column=5)

viewBtn=Button(window,text="View Details",width=20,command=lambda:viewDetails(lbox.get(ANCHOR)))
viewBtn.grid(row=2,column=5)

delBtn=Button(window,text="Delete Selected",width=20,command=lambda:delete(lbox))
delBtn.grid(row=3,column=5)

editBtn=Button(window,text="Edit Selected",width=20,command=lambda:EditWin(lbox.get(ANCHOR)))
editBtn.grid(row=4,column=5)

srchBtn=Button(window,text="Search",width=20,command=lambda:search())
srchBtn.grid(row=5,column=5)

xptBtn=Button(window,text="Export",width=20,command=lambda:ListOptions.exportList(productID,name,size,color,inStock))
xptBtn.grid(row=6,column=5)

exitBtn=Button(window,text="Exit",width=20,command=exit)
exitBtn.grid(row=7,column=5)

window.mainloop()



