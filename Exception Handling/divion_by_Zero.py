def divide_numbers():
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        
        result = num1 / num2
        print(f"Result: {result:.2f}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Run the function ---
divide_numbers()
