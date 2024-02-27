# Data Preprocessing Using  Scikit 
In this file you will find various preprocessing techniques that You can perform using Scikit learn.<br>Happy Preprocessing!

# Binarisation
Binarisation in data preprocessing is the technique through which we convert all the values of an array either as 0 or 1.

# How Binarisation works:
It works by setting up a threshold value within the givem range of numbers within the array. Any number above the threshold valus is converted as 1 and any number below the threshold value is converted to 0.

# One-Hot Encoding
One common preprocessing technique is one-hot encoding, which is used to convert categorical variables into a numerical format. Categorical variables are those that represent categories or labels, such as "red," "green," "blue" for a color feature or "cat," "dog," "bird" for an animal type feature.

# How One-Hot Encoding Works:
Let's say we have a categorical variable "Color" with three unique categories: "red," "green," and "blue."
One-hot encoding transforms this single categorical feature into three binary features: "Is Red," "Is Green," and "Is Blue."
If a data point originally had the "red" category, its one-hot encoded representation would be [1, 0, 0]. Similarly, for "green," it would be [0, 1, 0], and for "blue," it would be [0, 0, 1].

# Normalisation
Normalization is a data preprocessing technique that scales numerical features to a standard range, usually between 0 and 1, making them comparable. 

# How Normalisation works:
It involves subtracting the minimum value from each value and dividing by the range of the feature.