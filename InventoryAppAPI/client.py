import requests

#functions for GET methods:

def viewAll():
    url = 'http://127.0.0.1:9214/products/'
    getall = requests.get(url)
    print(getall.json())

def viewOne():
    url = 'http://127.0.0.1:9214/products/'
    pid = input("Please enter a PID: ")
    url = url + pid
    getone = requests.get(url)
    if getone.headers['content-length'] == '3':
        print("not found")
    else:
        print(getone.json())

def searchDatabase():
    url = 'http://127.0.0.1:9214/search'
    







def updateOne():
    url = 'http://127.0.0.1/products/'
    pid = input("Please enter a PID: ")
    url = url + pid
    # validStock = False

    #allow user to update all details associated with the item:
    n = input("Update Name: ")
    size = input("Update Size: ")
    color = input("Update color: ")
    instock = input("Update In Stock: ")

    if n == "":
        pass
    if size == "":
        pass
    if color == "":
        pass
    if instock == "":
        pass

    payload = {"name":n,"size":size,"color":color,"in_stock":instock}

    updateone = requests.post(url,json=payload)

    if updateone.status_code == 200:
        print("Item updated successfully.")
        

# def options():
#     print("Please select from the list below: \n1. View All Items\n2. View item\n3. Update Item.\n4. Delete Item.\n5. Add new item.\n6. Search\n7. Exit")
#     notValid = True
#     option = input()
#     while notValid:


# options()
