from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data
data = np.array([[1, 2], [3, 4], [5, 6]])

# Create a StandardScaler object
scaler = StandardScaler()

# Fit the scaler to the data and transform the data
standardized_data = scaler.fit_transform(data)

print("Original data:")
print(data)
print("\nStandardized data:")
print(standardized_data)
