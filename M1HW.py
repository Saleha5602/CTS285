#Bronze (80/100):   
def add():
    print("Add")
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))
    total= num1 + num2
    print(num1, "+" ,num2 ,"=", total)
   
def sub():
    print("sub")
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))
    total= num1 - num2
    print(num1, "-" ,num2 ,"=", total)
   
def divide():
    print("Divide")
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))
    total= num1 / num2
    print(num1, "/" ,num2 ,"=", total)
   
def multiply():
    print("Multiply")
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))
    total= num1 * num2
    print(num1, "*" ,num2 ,"=", total)
add()
sub()
divide()
multiply()  