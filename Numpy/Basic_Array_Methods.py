import numpy as np

# Create a 1D NumPy array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Reshape 1D to 2D (1 row, 5 columns)
array_2d_from_1d = array_1d.reshape(1, 5)
print("Reshaped 1D to 2D:", array_2d_from_1d)

# Slice the 1D array
sliced_1d = array_1d[1:4]
print("Sliced 1D Array:", sliced_1d)

# Create a 2D NumPy array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:", array_2d)

# Indexing the 2D array
element_2d = array_2d[1, 2]
print("Element at (1, 2) in 2D Array:", element_2d)

# Reshape 2D to 1D
reshaped_1d_from_2d = array_2d.flatten()
print("Reshaped 2D to 1D:", reshaped_1d_from_2d)

# Create a 3D NumPy array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", array_3d)

# Indexing the 3D array
element_3d = array_3d[1, 0, 1]
print("Element at (1, 0, 1) in 3D Array:", element_3d)

# Slicing the 3D array
sliced_3d = array_3d[:, 1, :]
print("Sliced 3D Array (all depths, row 1):\n", sliced_3d)

# Reshape 3D to 2D
reshaped_2d_from_3d = array_3d.reshape(4, 2)
print("Reshaped 3D to 2D:\n", reshaped_2d_from_3d)