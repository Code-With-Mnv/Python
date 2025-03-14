def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Example usage

num = int(input("Enter a number to compute its factorial: "))
print(f"The factorial of {num} is {factorial(num)}.")
