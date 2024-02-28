import numpy as np
from sklearn import preprocessing

Input_data = np.array([
   [2.1, -1.9, 5.5],
   [-1.5, 2.4, 3.5],
   [0.5, -7.9, 5.6],
   [5.9, 2.3, -5.8]]
)

#Displaying the mean
print("Mean = ", Input_data.mean(axis=0))
#Displaying the Standard Deviation
print("Standard deviation = ",Input_data.std(axis=0))

data_scaling = preprocessing.scale(Input_data)
print("Mean Removed = ", data_scaling.mean(axis=0))
print("Deviation removed = ",data_scaling.std(axis=0))