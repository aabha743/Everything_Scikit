# Data Preprocessing Using  Scikit 
In this file you will find various preprocessing techniques that You can perform using Scikit learn.<br>Happy Preprocessing!
# One-Hot Encoding
One common preprocessing technique is one-hot encoding, which is used to convert categorical variables into a numerical format. Categorical variables are those that represent categories or labels, such as "red," "green," "blue" for a color feature or "cat," "dog," "bird" for an animal type feature.

# How One-Hot Encoding Works:
Let's say we have a categorical variable "Color" with three unique categories: "red," "green," and "blue."
One-hot encoding transforms this single categorical feature into three binary features: "Is Red," "Is Green," and "Is Blue."
If a data point originally had the "red" category, its one-hot encoded representation would be [1, 0, 0]. Similarly, for "green," it would be [0, 1, 0], and for "blue," it would be [0, 0, 1].