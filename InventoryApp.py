
#Inventory Management Tool

import errorCheck   #imports isValid method
import ListOptions  #imports list option methods

#opens file and create a list of each line
with open('inventory.txt','r+') as f:
    inventory = list(f)

productID=[]
name=[]
size=[]
color=[]
inStock=[]

#this function reads opened file and assigns each row to its appropriate value in the lists above.
def setList():  
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
        name.append(s[1])
        size.append(s[2])
        color.append(s[3])
        inStock.append(s[4])
        counter+=1
        #clears temp list
        s.clear()
    print("\nInventory.txt has been Imported!")

setList()
ListOptions.options(inventory,productID,name,size,color,inStock)
#length of opened file
#l = len(inventory)
