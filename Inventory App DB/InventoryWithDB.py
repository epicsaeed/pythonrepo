import sqlite3
import ListOptionsWithDB

#sets up connection to local database
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

#global variables
productID=[]
name=[]
size=[]
color=[]
inStock=[]
count = 0

ListOptionsWithDB.createTable(cursor)
ListOptionsWithDB.readFromDB(productID,name,size,color,inStock,cursor)
#adds items from text file to db(to be ran once)
# while count < len(name):
#     ListOptions.addToDB(productID[count],name[count],size[count],color[count],inStock[count],c,conn)
#     count+=1
# ListOptions.restore(productID,name,size,color,inStock)
ListOptionsWithDB.optionsDB(productID,name,size,color,inStock,cursor,conn)