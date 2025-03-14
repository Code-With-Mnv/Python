# Prompt the user to enter the principal amount
principal = float(input("Enter the principal amount: "))

# Prompt the user to enter the rate of interest
rate = float(input("Enter the rate of interest: "))

# Prompt the user to enter the time period in years
time = float(input("Enter the time period in years: "))

# Calculate the simple interest
simple_interest = (principal * rate * time) / 100

# Display the result
print(f"The simple interest is: {simple_interest}")