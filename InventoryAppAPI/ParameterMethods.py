
#returns true if product ID is valid
def check_id(id):
    id = str(id)
    if id.isdigit():
        if len(id) == 7:
            return True
    return False


#checks if the passed parameters for POST are valid and returns true if so
def valid_POST_json(payload):
    if ('name' or 'size' or 'color' or 'in_stock') in payload:
        return True
    else:
        return False

#checks if the passed parameters for PUT are valid and returs true if so
def check_PUT_json(payload):
    if "product_id" in payload and "in_stock" in payload:
        return True
    return False