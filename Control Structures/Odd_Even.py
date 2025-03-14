def check_odd_even():
    while True:
        try:
            num = int(input("Enter a number (or type 'exit' to quit): "))
            if num % 2 == 0:
                print(f"{num} is even.")
            else:
                print(f"{num} is odd.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Ask the user if they want to continue
        cont = input("Do you want to check another number? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

# Example usage
check_odd_even()