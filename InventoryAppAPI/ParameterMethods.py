
#GLOBAL VARIABLES 
Name = ""
Productid = ""
Size = ""
Color = ""
Instock = 0

#returns true if product ID is valid
def check_id(id):
    id = str(id)
    if id.isdigit():
        if len(id) == 7:
            return True
    return False

#checks if in_stock is valid
def check_stock(instock):
    if str(instock).isdigit():
        return True
    return False

#checks if the passed parameters for POST are valid and returns true if so
def check_POST_json(payload):
    if ("name" or "size" or "color" or "in_stock") not in payload:
        return False
    return True

#checks if the passed parameters for PUT are valid and returs true if so
def check_PUT_json(payload):
    if "product_id" not in payload and "in_stock" not in payload:
        return False
    return True
