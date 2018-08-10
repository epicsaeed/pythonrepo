import requests

#global variables:
global url
url = 'http://127.0.0.1:9214/products/'

#helper functions:
def validPID(pid):
    try:
        if pid.isdigit():
            return True
    except AttributeError:
        return False

def GETAll():
    getall = requests.get(url)
    # getall.split("\n")
    counter = 0
    for item in getall:
        print(counter,". " ,item)
        counter+=1
    # return(getall.json())

def checkParams(pid, instock):
    if validPID(pid):
        if instock.isdigit():
            return True
    return False


def GETOne(pid):
    pid = str(pid)
    if validPID(pid):
        newurl = url + pid
        getone = requests.get(newurl)
        return getone.json()
    else:
        return "Error. Invalid Product ID"

def searchDatabase():
    newurl = url + 'search'
    print("Search based on \n1.Name\n2.Size\n3.Color\n4.ProductID")
    params = input()
    badParams = True
    while badParams:
        if params == '1':
            badParams = False
            name = input("write a name: ")
            params = {"name":name}
        if params == '2':
            badParams = False
            size = input("write a size: ")
            params = {"size":size}  
        if params == '3':
            badParams = False
            color = input("write a color: ")
            params = {"color":color}  
        if params == '4':
            badParams = False
            pid = input("write a product ID: ")
            params = {"productid":pid}   
    search = requests.get(newurl,params=params)
    if search.status_code == 200:
        print(search.json())
    else:
        print("Error occured when searching")
 
def POSTone(pid):
    newurl = url + str(pid)
    #allow user to update all details associated with the item:
    n = input("Update Name: ")
    size = input("Update Size: ")
    color = input("Update color: ")
    instock = input("Update In Stock: ")

    payload = {"name":n,"size":size,"color":color,"in_stock":instock}

    updateone = requests.post(newurl,json=payload)

    if updateone.status_code == 200:
        print("Item updated successfully.")

def DELETEone(pid):
    if validPID(pid):
        newurl = url + str(pid)
        delete = requests.delete(newurl)
        if delete.status_code == 200:
            return "Item deleted."
        else:
            "Error occured."
    else:
        return "Error. Invalid Product ID"

def PUTone():
    newurl = url + "add"
    name = input("Name: ")
    pid = input("Product ID (7-digit number): ")
    color = input("Color: ")
    size = input("Size: ")
    instock = str(input("InStock: "))
    valid = checkParams(pid,instock)
    if valid:
        params = {"name":name,"product_id":pid,"color":color,"size":size,"in_stock":instock}
        add = requests.put(newurl,json=params)
        if add.status_code == 200:
            return "item Added successfully."
    else:
        return "Error: Invalid parameters."





def Options():
    print("Select from list below:\n1. View All Item\n2. View one item\n3. Add item \n4. Delete Item\n5. Search\n6. Update Item\n7. Exit")
    choice = input()
    choiceNotValid = True
    while choiceNotValid:
        if choice == '1':
            choiceNotValid = False
            GETAll()
        elif choice == '2':
            choiceNotValid = False
            pid = input("Please write the product ID: ")
            print(GETOne(pid))
        elif choice == '3':
            choiceNotValid = False
            PUTone()
        elif choice == '4':
            choiceNotValid = False
            pid = input("Please write the product ID: ")
            DELETEone(pid)
        elif choice == '5':
            choiceNotValid = False
            pass
        elif choice == '6':
            choiceNotValid = False
            pass
        elif choice == '7':
            exit()
            pass
        else:
            choice = input("Please select a valid number")


while True:
    Options()