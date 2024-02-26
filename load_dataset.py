'''Incase you do not have the sklearn library in your system, install it via command prompt through
the following command - pip install sklearn.

First step is to import the sklearn library. Specifically the datasets.''' 
from sklearn.datasets import load_iris

#Loading the iris dataset 
iris = load_iris()

#Setting the Independant and target variables
X = iris.data
y = iris.target

feature_names = iris.feature_names
target_names = iris.target_names

print("Feature names:", feature_names)
print("Target names:", target_names)
print("\nFirst 10 rows of X:\n", X[:10])