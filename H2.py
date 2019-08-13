#importing the dataset
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
data_set=pd.read_csv('MODEL_TRAINING1.csv')
data_set1=pd.read_csv('MODEL_PREDICT.csv')
X=data_set.iloc[:,:-1]
y=data_set.iloc[:,3:4]
X1=data_set1.iloc[:,2:5]

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

#feature scaling on X1
from sklearn.preprocessing import StandardScaler
sc_x1=StandardScaler()
X1=sc_x1.fit_transform(X1)

#Fitting classifier to the training set
from sklearn.svm import SVC
classifier=SVC(kernel='linear',random_state=0)
classifier.fit(X_train,y_train)

#Predicting the test set results
y_pred=classifier.predict(X_test)

#Confusion Matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

#Accuracy
pos=0
neg=0
for i in range(0,64):
    if y_pred[i]==y_test[i]:
        pos=pos+1
    else:
        neg=neg+1
        
#Prediction
y_pred1=classifier.predict(X1)

#To retrive the category name from categorical data
y_pred2=labelencoder.inverse_transform(y_pred1)

"""y3={}
#To predict the crop appearing maximum number of times
from collections import Counter
for i in range(1,11):
    y2=Counter(y_pred2[45*(i-1):45*i])
    y3[i]=y2.most_common(1)
    print (y2.most_common(1))"""

y3= list()
from collections import Counter
for i in range(1,11):
    y2=Counter(y_pred2[45*(i-1):45*i])
    y3.append(y2.most_common(1))
    print (y2.most_common(1))
