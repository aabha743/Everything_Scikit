'''After the first step of loading the dataset, the second step should be to learn
hpw to split the dataset into train and test dataset for training and testing the algorithm
for its accuracy and performance'''


from sklearn.datasets import load_iris
iris = load_iris()

X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split

'''In the below line of code, we are using four variables,
 X_train and  y_train as the raining
 variables and X_text and y_text as the test variables
 to check the accuracy of the algorithm after training'''

X_train, X_test, y_train, y_test = train_test_split(
   X, y, test_size = 0.3, random_state = 1
)

print(X_train.shape)
print(X_test.shape)

print(y_train.shape)
print(y_test.shape)