# -*- coding: utf-8 -*-
"""Task5-Credit Card Fraud Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/160VTgTG0aMnCf4A6hV-tipx8xXYDQgfX

**Credit Card Fraud Detection**

**Task 05 : Problem Statement**

1.Build a machine learning model to identify fradulent credit card transactions.

2.Preprocess and normalize the transaction data, handle class inbalance issues, and split the dataset into training and testing sets.

3.Train a classification algorithm,such as logistic regression or random forests to classify transactions as fraudelent or genuine.

4.Evaluate the model's performance using metrics like precision, recall, and f1-score and cosider techniques like oversampling or undersampling for improving results.

**Work Flow**

1.Data loading

2.Data pre-processing

3.Exploratory Data analysis

4.Spliting training and test data

5.Model training -Logistic Regression

6.Model Evaluation
"""

# Importig the libraries

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, recall_score , classification_report

# loding the dataset

cc_data= pd.read_csv('/content/creditcard.csv')

# Shows first 5 rows of dataframe
cc_data.head()

cc_data.info()  # to get information about dataset

# Checking the missing values
cc_data.isnull().sum()

# distribution of legit transaction and fradulent transaction

cc_data['Class'].value_counts()
# 0---> normal transaction
# 1---> fradulent transaction

# separating the data

legit=cc_data[cc_data.Class==0]
fraud=cc_data[cc_data.Class==1]

print(legit.shape)
print(fraud.shape)

# Statstical info
legit.Amount.describe()

fraud.Amount.describe()

fraud.Amount.describe()

# Under Sampling -- building a sample dataset containing similar distribution of normal transaction and fradulent transaction.

#number of fradulent transaction = 261


legit_sample=legit.sample(n=261)

# concatenating

new_data=pd.concat([legit_sample, fraud],axis=0)

new_data.tail() # checking bottem columns and rows

new_data['Class'].value_counts() # verifying concatenated data

new_data.groupby('Class').mean()

# Spliting the data into Features and Targets

X=new_data.drop(columns='Class', axis=1)
Y=new_data['Class']

print(X)

print(Y)

"""Spliting data into train and test data"""

# Split the data into train and test

X_train,X_test,Y_train,Y_test=train_test_split (X,Y, test_size=0.2, stratify=Y,random_state=2)

print(X.shape, X_train.shape,X_test.shape)

"""Model Training - Logistic Regression"""

# model training

model=LogisticRegression()

# training the model with training data

model.fit(X_train, Y_train)

"""Model Evaluation"""

# accuracy on training data

X_train_prediction=model.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,Y_train)

print('Accuracy on training data :{:.2f}%'.format(training_data_accuracy*100))

# accuracy on test data

X_test_prediction=model.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction,Y_test)

print('Accuracy on test data :{:.2f}%'.format(test_data_accuracy*100))

print (classification_report(Y_test , model.predict(X_test)))

"""**Conclusion**

The logistic regression algorithm is likely to be a  good model for the given problem to classify transactions as fraudulent or genuine. It has evaluated the model's performance using metrics like precision, recall,and F1-score, and considered techniques like oversampling or
undersampling for improving results.
"""
