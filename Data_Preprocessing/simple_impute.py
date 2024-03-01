from sklearn.impute import SimpleImputer
import numpy as np

# Sample data with missing values
data = np.array([[1, 2], [np.nan, 3], [4, np.nan], [5, 6]])

# Create the imputer object
imputer = SimpleImputer(strategy='mean')

# Fit the imputer on the data and transform the data
imputed_data = imputer.fit_transform(data)

print("Original data:")
print(data)
print("\nImputed data:")
print(imputed_data)
