def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def mod(a, b):
    if b == 0:
        return "Error: Mod by zero!"
    return a%b

def power(a ,b):
    if b==0:
        return 1
    return a**b

#todo: add future operations here in branch called 'adding-{name of operation}-operation'