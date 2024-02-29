# Normalisation 

Normalisation is a technique to convert the numerical values in an array to a common scale for further processing or to feed it into an algorithm or model.In this method we make sure that the sum of the values of an array are 1. This is a step that we undertake incase of the values being too varying. By having the values in a common scale, it is easier to work with the data.<br> There are two types of normalisation that we use. They are:<br>1.L1<br>2.L2

# L1 Normalisation Working
It is also called Least Absolute Deviations. It modifies the value in such a manner that the sum of the absolute values remains always up to 1 in each row. You can find the execution of this in the file "normalisation_1.py" 

# L2 Normalisation Working
Also called Least Squares. It modifies the value in such a manner that the sum of the squares remains always up to 1 in each row.You can find the execution of this in the file "normalisation_2.py" 

# Z-Score Normalisation
Z-score normalization, also known as standardization, is a statistical technique that rescales a distribution of values to have a mean of 0 and a standard deviation of 1, making it easier to compare different distributions.

# How does it work
Z-score normalization works by subtracting the mean of the distribution from each value and then dividing by the standard deviation. This centers the distribution at 0 with a spread of 1, preserving the relative differences between values.