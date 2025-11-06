from operations import add, subtract, multiply, divide, mod
def main():
    print("Welcome to the Python Calculator!")
    a = 10
    b = 5
    print("Add:", add(a, b))
    print("Subtract:", subtract(a, b))
    print("Multiply:", multiply(a, b))
    print("Divide:", divide(a, b))
    print("Modulus:", mod(a, b))

if __name__ == "__main__":
    main()
