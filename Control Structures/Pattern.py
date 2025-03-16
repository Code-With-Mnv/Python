def print_diamond_pattern(n):
    # Print the upper half of the diamond
    for i in range(n):
        # Print leading spaces
        for j in range(n - i - 1):
            print(" ", end="")
        
        # Print stars
        for j in range(2 * i + 1):
            print("*", end="")
        
        # Move to the next line
        print()
    
    # Print the lower half of the diamond
    for i in range(n - 2, -1, -1):
        # Print leading spaces
        for j in range(n - i - 1):
            print(" ", end="")
        
        # Print stars
        for j in range(2 * i + 1):
            print("*", end="")
        
        # Move to the next line
        print()

# Example usage
print_diamond_pattern(int(input("Enter the number of rows for the diamond pattern: ")))