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

# Scaling
Scaling is the process through which we bring the values of an array or feature vectors to be within a particular range. Scaling of feature vectors is important, because the features should not be synthetically large or small.

# How does scaling work:
MinMax scaling is a data normalization technique used in machine learning to scale numeric features to a specific range, typically between 0 and 1.<br>
Imagine you have a bunch of numbers that represent different things, like test scores ranging from 0 to 100. MinMax scaling is like squishing those numbers so they all fit between 0 and 1, no matter how big or small they were originally.<br>

Here's how it works:<br>

1.You find the smallest number in your group (let's say it's 60) and call it the minimum.<br>
2.You find the biggest number in your group (let's say it's 90) and call it the maximum.<br>
3.Then, for each number in your group (like 75, 80, 85, etc.), you do a little math to make it a new number between 0 and 1.<br>
For example, if you want to scale the number 75:<br>
Scaled_75=(75−60)/(90−60)=15/30=0.5<br>

So, the number 75 would become 0.5 after MinMax scaling. This helps make sure all the numbers are easier to compare, no matter what range they started in.

# Mean Removal
This technique is used to eliminate the mean from feature vector so that every feature centered on zero.

# How does Mean Removal Work:
Mean removal is a process used to center data around zero by subtracting the mean value of a dataset from each data point. This helps in removing any bias or trend from the data, making it easier to compare different datasets or analyze their relationships.