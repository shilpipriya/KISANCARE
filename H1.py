#importing the dataset
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
data_set=pd.read_csv('MODEL_TRAINING.csv')
X=data_set.iloc[:,:-1]
y=data_set.iloc[:,3:4]

#Encoding the categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
y=labelencoder.fit_transform(y)

#Splitting the dataset into training set and test set
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=0)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
X_train=sc_x.fit_transform(X_train)
X_test=sc_x.transform(X_test)

#Applying k-means to the dataset
from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=32,init='k-means++',max_iter=200,n_init=10)
y_kmeans=kmeans.fit_predict(X_train)

#Accuracy
pos=0
neg=0
for i in range(0,576):
    if y_kmeans[i]==y_train[i]:
        pos=pos+1
    else:
        neg=neg+1