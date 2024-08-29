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
