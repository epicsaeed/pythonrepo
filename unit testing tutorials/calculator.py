

def validInput(x,y):
    if type(x) is int and type(y) is int:
        return True
    return False


def add(x,y):
    validInput(x,y)
    return x + y

def subtract(x,y):
    validInput(x,y)
    return x - y

def multiply(x,y):
    validInput(x,y)
    return x * y

def divide(x,y):
    validInput(x,y)
    if y == 0:
        return False
    return x / y
