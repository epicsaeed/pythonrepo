
#checks if a passed parameter is an integer
def isValid(s): 
    try:
        int(s)
        return True
    except ValueError:
        return False