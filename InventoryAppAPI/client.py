import requests

#functions for GET methods:

def viewAll():
    url = 'http://127.0.0.1:9214/products/'
    getall = requests.get(url)
    print(getall.json())
    hsppe print(shodlhi)
    sldjvhdk
    something
    
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
    print("Search based on 1.Name\n2.Size\n3.Color\n4.ProductID\n5.In Stock\nENTER PARAMETERS SEPERATED BY A COMMA")
    params = input()
    
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
        

viewAll()
updateOne()