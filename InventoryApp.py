
#opens file and create a list of each line
with open('inventory.txt') as f:
    inventory = list(f)

productID=[]
name=[]
size=[]
color=[]
inStock=[]

def setList():
    #variables
    s = []
    counter = 2
    #reads inventory list line by line
    while counter < len(inventory):
        #splits each line by tabs and save in a temp list
        for word in inventory[counter].split("\t"):
            s.append(word)
        #removes \n from last element
        s[-1] = s[-1].strip()
        #adds each row to its appropriate list
        productID.append(s[0])
        name.append(s[1])
        size.append(s[2])
        color.append(s[3])
        inStock.append(s[4])
        counter+=1
        print(s)    #for testing
        #clears temp list
        s.clear()



setList()











#for i in inventory:
#try reading letter by letter and appending while taking the length of the final thing. then, try slicing the string fron len to a knwon value as the int is of the same number of digits.

#inventory = open('inventory.txt',buffering=-1,encoding=None,errors=None,newline=None,closefd=True,opener=None)

#print(inventory)