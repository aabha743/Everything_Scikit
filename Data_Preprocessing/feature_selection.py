from sklearn.feature_selection import SelectKBest, f_classif
import numpy as np

# Sample data
X = np.array([[1, 2, 3, 4], [4, 3, 2, 1], [2, 4, 3, 1], [3, 1, 4, 2]])
y = np.array([0, 1, 0, 1])

# Feature selection
selector = SelectKBest(score_func=f_classif, k=3)
selected_features = selector.fit_transform(X, y)

print("Original data shape:", X.shape)
print("Selected data shape:", selected_features.shape)
print("Selected features:")
print(selected_features)
