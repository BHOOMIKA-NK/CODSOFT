# -*- coding: utf-8 -*-
"""Task2 Movie Rating Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UQfosiTU3aAPSH-duBfjLh8qRZgHgZcQ

**Movie Rating Prediction Using Python**

**TASK 2 : Problem statement**

1.Build a model that predicts the rating of a movie based on genre, director, and actors. You can use regression techniques to tackle this problem.

2.The goal is to analyze historical movie data and develop a model that accurately estimates the rating given to a movie by users or critics.

3.Movie rating prediction project enables you to explore data analysis, preprocessing, feature engineering and machine learning modeling techniques.It provides insights into the factors that infulence movie ratings and allows you to build a model that can estimate the ratings of movie accurately.
"""

# Importing the libraries

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor

# loading the datasets
movies_data=pd.read_csv('/content/movies.dat', sep='::',engine='python',encoding='latin-1',names=['Movieid','Title','Genres'])

#showing first 5 rows of movies dataframe
movies_data.head()

movies_data.shape

users_data=pd.read_csv('/content/users.dat', sep='::', engine='python', encoding='latin-1',names=['Userid','Gender','Age','Occupation','Zipcode'])

#showing first 5 rows of user dataframe
users_data.head()

users_data.shape

ratings_data=pd.read_csv('/content/ratings.dat', sep='::',engine='python',encoding='latin-1',names=['Userid','Movieid','Ratings','Timestamp'])

#showing first 5 rows of rating dataframe
ratings_data.head()

ratings_data.shape

# merging movie data with respect to ratings data

ratings_data=movies_data.merge(ratings_data,on='Movieid',how='inner')

ratings_data.head()

# merging the ratings data with respect to users data and creating new data set

main_data=ratings_data.merge(users_data,on='Userid',how='inner')

main_data.head()

main_data.shape

main_data.isnull().sum() # checking for null values

main_data.info() # checking the information about the dataset

main_data['Age'].value_counts()

# visual representation

main_data['Age'].value_counts().plot(kind='bar')
plt.title('User age distribution')
plt.xlabel('Age')
plt.ylabel('users accounts')
plt.show()

# user ratings for a movies

movie_rating=main_data[main_data['Title'].str.contains('Toy Story')]
movie_rating

# visual representation

movie_rating.groupby(['Title','Ratings']).size().unstack().plot(kind='bar',stacked=False, legend=True)
plt.show()

movie_rating.groupby(['Age','Ratings']).size().unstack().plot(kind='bar',stacked=False, legend=True)
plt.show()

main_data.head()

main_data.to_csv('main_data.csv', index=False)

df=pd.read_csv('main_data.csv')
df.head()

df.shape

# Splitting the data into features and Targets

X=df.drop(columns=['Title','Genres','Timestamp','Gender','Zipcode','Ratings'],axis=True)

Y=df['Ratings']

print(X)

print(Y)

# spliting the data into test and training sets

X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape,X_train.shape,X_test.shape)

# Logistic Regression model training

model=LogisticRegression()

# Training the model

model.fit(X_train, Y_train)

"""**Model Evaluation**"""

# Accuracy on trainig data
X_train_prediction=model.predict(X_train)

print(X_train_prediction)

training_data_accuracy=accuracy_score(Y_train,X_train_prediction)

print('Accuracy on training data :', training_data_accuracy*100)

# Using Random ForestRegressor model

model_2=RandomForestRegressor(n_estimators=100)
model_2.fit(X_train, Y_train)

model_test_prediction=model_2.predict(X_test)

(model_2.score(X_train,Y_train))*100

accuracy_random_forest = round(model_2.score(X_train, Y_train) * 100, 2)

accuracy_random_forest

# Logistic Regression and Random ForestRegressor model are implemented here

