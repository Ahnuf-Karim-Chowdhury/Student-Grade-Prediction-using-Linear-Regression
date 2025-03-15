import pandas as pd 
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

# Load the dataset
data = pd.read_csv("student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

# Define the column to predict (target variable)
predict = "G3"

a = np.array(data.drop([predict], axis=1))

b = np.array(data[predict])
a_train, a_test, b_train, b_test = sklearn.model_selection.train_test_split(a, b, test_size=0.1)

test =0

# Training the Model Part
""" for _ in range(201):
     # Split the data into training and test sets
     a_train, a_test, b_train, b_test = sklearn.model_selection.train_test_split(a, b, test_size=0.1)

     # Create a LinearRegression model
     linear = linear_model.LinearRegression()

     # Train the model with the training data
     linear.fit(a_train, b_train)

     # Evaluate the model with the test data
     opt = linear.score(a_test, b_test)

     print("Model score:", opt)
     print(f"Accuracy : {opt}")
     
     if opt > test:
          test=opt
          with open("student-model.pickle","wb") as f :
               pickle.dump(linear, f)    """

pickle_in = open("student-model.pickle","rb")
linear = pickle.load(pickle_in)

print("Co-efficient : ",linear.coef_)
print("Intercept : ", linear.intercept_)

predictions = linear.predict(a_test)

for _ in range(len(predictions)):
     print(predictions[_],a_test[_],b_test[_])

p = "absences"
style.use("ggplot")
pyplot.scatter(data[p],data["G3"])
pyplot.xlabel("Final Grade")
pyplot.show()

