# Prompt the user to enter the first number
num1 = float(input("Enter the first number: "))

# Prompt the user to enter the second number
num2 = float(input("Enter the second number: "))

# Perform addition
addition = num1 + num2

# Perform subtraction
subtraction = num1 - num2

# Perform multiplication
multiplication = num1 * num2

# Perform division
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (division by zero)"

# Perform modulus
if num2 != 0:
    modulus = num1 % num2
else:
    modulus = "undefined (division by zero)"

# Display the results
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
print(f"Modulus: {num1} % {num2} = {modulus}")