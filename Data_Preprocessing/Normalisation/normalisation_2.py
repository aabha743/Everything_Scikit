import numpy as np
from sklearn import preprocessing

Input_data = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

data_normalised = preprocessing.normalize(Input_data, norm = 'l2')

print("L2 Normalised data:\n",data_normalised)