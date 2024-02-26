# Everything_Scikit
This repository is for anyone who would like to learn Scikit or Sklearn from scratch. I will be pushing all the code that I work and test on.I hope it will help. <br> Happy Learning!<br>
# The First step - Load Dataset
The first file that your should refer to learn basics of sklearn is the "load_dataset.py" file. Through this file we undertsand that there are datasets within the sklearn library that we can use to learn and build algorithms.
# The Second step - Split Dataset
One of the key concepts that come under working with an algorithm or a dataset are to be able to split it into test and train datasets or parts as that would help us in checking the accuracy of the algorithm or on a bigger term, the accuracy of the model. In the second python file, we learn how to use Sklearn to split our dataset. we use the train_test_split function to perform this task.
# The Third Step - Data Preprocessing
The third step is to understand Data Preprocessing and use sklearn to perform data preprocessing.
# One-Hot Encoding
One common preprocessing technique is one-hot encoding, which is used to convert categorical variables into a numerical format. Categorical variables are those that represent categories or labels, such as "red," "green," "blue" for a color feature or "cat," "dog," "bird" for an animal type feature.

# How One-Hot Encoding Works:
Let's say we have a categorical variable "Color" with three unique categories: "red," "green," and "blue."
One-hot encoding transforms this single categorical feature into three binary features: "Is Red," "Is Green," and "Is Blue."
If a data point originally had the "red" category, its one-hot encoded representation would be [1, 0, 0]. Similarly, for "green," it would be [0, 1, 0], and for "blue," it would be [0, 0, 1].