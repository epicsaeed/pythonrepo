
#Inventory Management Tool

import errorCheck   #imports isValid method
import ListOptions  #imports list option methods
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#shows a dialog window for user to select text file
Tk().withdraw()
path = askopenfilename() # show an "Open" dialog box and return the path to the selected file

#opens file and create a list of each line
with open(path,'r+') as f:
    inventory = list(f)

#global variables
productID=[]
name=[]
size=[]
color=[]
inStock=[]

#calling main interface of program
ListOptions.setListMulti(inventory,productID,name,size,color,inStock)
ListOptions.restore(productID,name,size,color,inStock)
ListOptions.options(inventory,productID,name,size,color,inStock)