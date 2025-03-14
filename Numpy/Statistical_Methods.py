import numpy as np

# Sample data: You can change this array to any dataset you want to analyze
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Calculate mean
mean = np.mean(data)
print("Mean:", mean)

# Calculate median
median = np.median(data)
print("Median:", median)

# Calculate standard deviation
std_dev = np.std(data)
print("Standard Deviation:", std_dev)

# Calculate variance
variance = np.var(data)
print("Variance:", variance)

# Calculate correlation coefficients
# For correlation, we need at least two datasets. Here, we create a second dataset.
data2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
correlation_coefficient = np.corrcoef(data, data2)[0, 1]
print("Correlation Coefficient between data and data2:", correlation_coefficient)