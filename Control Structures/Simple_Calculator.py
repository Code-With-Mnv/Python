def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        operation = input("Enter the operation (+, -, *, /): ").strip()

        if operation == '+':
            print(f"The result is: {add(num1, num2)}")
        elif operation == '-':
            print(f"The result is: {subtract(num1, num2)}")
        elif operation == '*':
            print(f"The result is: {multiply(num1, num2)}")
        elif operation == '/':
            print(f"The result is: {divide(num1, num2)}")
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")
            continue

        # Ask the user if they want to perform another calculation
        cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

# Example usage
calculator()