import os

def perform_calculation():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please choose from +, -, *, /.")
            return

        equation = f"{num1} {operation} {num2} = {result}"
        print("Result:", result)

        with open("equations.txt", "a") as file:
            file.write(equation + "\n")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

def print_equations():
    if not os.path.exists("equations.txt"):
        print("No previous equations found.")
        return

    with open("equations.txt", "r") as file:
        equations = file.readlines()

    if equations:
        print("\nPrevious Equations:")
        for eq in equations:
            print(eq.strip())
    else:
        print("Equations file is empty.")

def main():
    while True:
        print("\nSimple Calculator App")
        print("1. Perform a calculation")
        print("2. View previous equations")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            perform_calculation()
        elif choice == '2':
            print_equations()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
