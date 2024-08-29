import calculations_functions as cal
def get_numbers(operation):
    ''' For this function I had the idea in my mind but I had 
    difficulty writing it so I used chatgbt.''' 
    print(operation)
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    return num1, num2

def add():
    #num1 = int(input("Enter a number: "))
    #num2 = int(input("Enter a number: "))
    num1, num2 = get_numbers("Add")
    total= cal.cal_add(num1, num2)
    print(num1, "+", num2, "=", total)
    return repeat_operation()

def sub():
    num1, num2 = get_numbers("Subtract")
    total= cal.cal_subtract(num1, num2)
    print(num1, "-", num2, "=", total)
    return repeat_operation()

def divide():
    num1, num2 = get_numbers("Divide")
    total = cal.cal_divide(num1, num2)
    print(num1, "/", num2, "=", total)
    return repeat_operation()

def multiply():
    num1, num2 = get_numbers("Multiply")
    total =cal.cal_multiply(num1, num2)
    print(num1, "*", num2, "=", total)
    return repeat_operation()

def repeat_operation():
    choice = input("1. Repeat\n2. Main Menu\nEnter a choice: ")
    if choice == '1':
        return True
    else:
        return False
