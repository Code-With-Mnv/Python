#Pattern like     
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA

def print_triangle_pattern(n):
    for i in range(n):
        # Print leading spaces
        for j in range(n - i - 1):
            print(" ", end="")
        
        # Print the first half of the pattern
        for j in range(i + 1):
            print(chr(65 + j), end="")
        
        # Print the second half of the pattern
        for j in range(i - 1, -1, -1):
            print(chr(65 + j), end="")
        
        # Move to the next line
        print()

# Example usage
print_triangle_pattern(5)