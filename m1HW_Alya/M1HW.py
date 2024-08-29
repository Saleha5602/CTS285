#Gold (100/100)
import functions as nm
def main():
    choice = 0
    while choice != 5:
        print("Welcome to the calculator program.")
        print("1. Add")
        print("2. Subtract")
        print("3. Divide")
        print("4. Multiply")
        print("5. Exit")
        choice = int(input("Enter a choice: "))
        if choice == 1:
            while nm.add():
                pass
        elif choice == 2:
            while nm.sub():
                pass
        elif choice == 3:
            while nm.divide():
                pass
        elif choice == 4:
            while nm.multiply():
                pass
        elif choice == 5:
            print("Goodbye.")
        else:
            print("Invalid choice")

main()
#Silver (90/100)
# def add():
#     print("Add")
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter a number: "))
#     total = num1 + num2
#     print(num1, "+", num2, "=", total)
    
# def sub():
#     print("Subtract")
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter a number: "))
#     total = num1 - num2
#     print(num1, "-", num2, "=", total)
    

# def divide():
#     print("Divide")
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter a number: "))
#     if num2 == 0:
#         print("Error: Division by zero")
#     else:
#         total = num1 / num2
#         print(num1, "/", num2, "=", total)
    

# def multiply():
#     print("Multiply")
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter a number: "))
#     total = num1 * num2
#     print(num1, "*", num2, "=", total)
    

# def main():
    
#     choice=0
#     while choice != 5:
#         print(" Welcome to the calculator program.")
#         print( " 1. Add")
#         print( " 2. Subtract")
#         print( " 3. Divide ")
#         print( " 4. Multiply")
#         print( " 5. Exit")
#         choice = int(input("enter a chioce: "))
#         if choice ==1:
#              add()
#         elif choice ==2:
#              sub()
#         elif choice ==3:
#             divide()
#         elif choice ==4:
#              multiply()
#         elif choice ==5:
#             print("exit")
           
#         else:
#           print("bad choice")
#               # does not exit
                
        
# main()
#Bronze (80/100):   
# def add():
#     print("Add")
#     num1=int(input("Enter a number: "))
#     num2=int(input("Enter a number: "))
#     total= num1 + num2
#     print(num1, "+" ,num2 ,"=", total)
   
# def sub():
#     print("sub")
#     num1=int(input("Enter a number: "))
#     num2=int(input("Enter a number: "))
#     total= num1 - num2
#     print(num1, "-" ,num2 ,"=", total)
   
# def divide():
#     print("Divide")
#     num1=int(input("Enter a number: "))
#     num2=int(input("Enter a number: "))
#     total= num1 / num2
#     print(num1, "/" ,num2 ,"=", total)
   
# def multiply():
#     print("Multiply")
#     num1=int(input("Enter a number: "))
#     num2=int(input("Enter a number: "))
#     total= num1 * num2
#     print(num1, "*" ,num2 ,"=", total)
# add()
# sub()
# divide()
# multiply()  