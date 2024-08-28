def add():
    print("Add")
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    total = num1 + num2
    print(num1, "+", num2, "=", total)
    return repeat()

def sub():
    print("Subtract")
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    total = num1 - num2
    print(num1, "-", num2, "=", total)
    return repeat()

def divide():
    print("Divide")
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    if num2 == 0:
        print("Error: Division by zero")
    else:
        total = num1 / num2
        print(num1, "/", num2, "=", total)
    return repeat()

def multiply():
    print("Multiply")
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    total = num1 * num2
    print(num1, "*", num2, "=", total)
    return repeat()

def repeat():
    choice = input("1. Repeat\n2. Main Menu\nEnter a choice: ")
    if choice == '1':
        return True
    else:
        return False
