import requests
from helpers import * 

#functions for GET methods:
global url
url = 'http://127.0.0.1:9214/products/'

def GETAll():
    getall = requests.get(url)
    print(getall.json())

def GETOne(pid):
    if not helpers.pid_is_valid(pid):
        return 400
    newurl = url + pid
    getone = requests.get(newurl)
    return getone.json()

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
        
def Options():
    print("Select from list below:\n1. View All Item\n2. View one item\n3. Update item\n4. Delete Item\n5. Search\n6. Exit")
    

print(GETOne(1234567))