
#Inventory Management Tool

import errorCheck   #imports isValid method
import ListOptions  #imports list option methods

#opens file and create a list of each line
with open('inventory.txt','r+') as f:
    inventory = list(f)

#global variables
productID=[]
name=[]
size=[]
color=[]
inStock=[]

#calling main interface of program
ListOptions.checkFile(inventory,productID,name,size,color,inStock)
ListOptions.options(inventory,productID,name,size,color,inStock)