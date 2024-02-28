import numpy  as np
from sklearn import preprocessing

Input_data = np.array ([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

data_scaling_minmax = preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled = data_scaling_minmax.fit_transform(Input_data)

print("Min Max Scaled array:\n",data_scaled)