# -*- coding: utf-8 -*-
"""Copy of Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dBkK4gYsXeybZsomRwymZGlsIm9OJZkx

Importing the Dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection and Processing"""

#loading the csv data to a Pandas DataFrame
heart_data = pd.read_csv('/content/heart_disease_data.csv')

# print first 5 rows of the dataset
heart_data.head()

#number and rows and coloumn in the dataset
heart_data.shape

#getting some infom about the data
heart_data.info()

#stastical measres of data
heart_data.describe()

#checking the distribution of target variable
heart_data['target'].value_counts()

"""1 --> Defective Heart
0 --> Healthy Heart

Splitting the fetaures and target
"""

X = heart_data.drop(columns='target',axis =1)
Y = heart_data['target']

print(X)

print(Y)

"""Spliiting data into training data and test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify = Y, random_state = 2)

print(X.shape,X_train.shape, X_test.shape)

"""Model Training

Logistic Regression
"""

model = LogisticRegression()

#tarining the LogisticREgression modelwith Training Data
model.fit(X_train, Y_train)

"""Model evaluation

Accuracy Score
"""

#accuracy on traing data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on Training data :', training_data_accuracy)

#accuracy on traing data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on Test data :', test_data_accuracy)

"""Building a PREDICTIVE System"""

input_data =(67,1,0,120,229,0,0,129,1,2.6,1,2,3)

#change the input data to a numpy arrray
input_data_as_numpy_array = np.asarray(input_data)

#reshape the numpy array as we are predicting for only one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The Person does not have a Heart Disease')
else:
  print("The Person has Heart Disease")

