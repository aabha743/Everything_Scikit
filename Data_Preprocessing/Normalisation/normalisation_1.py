import numpy as np
from sklearn import preprocessing

Input_data = np.array([
    [1.5,2.0,3.5],
    [4.5,5.0,6.0],
    [0.4,8.0,7.5]
])

data_normalised = preprocessing.normalize(Input_data, norm="l1")

print("Normalised data :\n",data_normalised)