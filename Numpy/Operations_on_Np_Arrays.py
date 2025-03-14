import numpy as np

# Create two arrays of the same shape
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])

# Element-wise operations
addition = array1 + array2
subtraction = array1 - array2
multiplication = array1 * array2
division = array1 / array2

# Display results of element-wise operations
print("Array 1:\n", array1)
print("Array 2:\n", array2)
print("Element-wise Addition:\n", addition)
print("Element-wise Subtraction:\n", subtraction)
print("Element-wise Multiplication:\n", multiplication)
print("Element-wise Division:\n", division)

# Define two vectors for dot and cross product
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Calculate dot product
dot_product = np.dot(vector1, vector2)

# Calculate cross product
cross_product = np.cross(vector1, vector2)

# Display results of dot and cross products
print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("Dot Product:", dot_product)
print("Cross Product:", cross_product)