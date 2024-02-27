'''This preprocessing technique is used when we need to convert
 our numerical values into Boolean values.'''

import numpy as np
from sklearn import preprocessing

Input_data = np.array([
   [2.1, -1.9, 5.5],
   [-1.5, 2.4, 3.5],
   [0.5, -7.9, 5.6],
   [5.9, 2.3, -5.8]]
)

'''We used threshold value = 0.5 and that is why, 
all the values above 0.5 would be converted to 1, 
and all the values below 0.5 would be converted to 0.'''

data_binarized = preprocessing.Binarizer(threshold=0.5).transform(Input_data)

print("\nBinarized data:\n", data_binarized)