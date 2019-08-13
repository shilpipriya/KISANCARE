#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the datasets
dataset=pd.read_csv('MODEL4_DATASET_CROPS.csv')
dataset1=pd.read_csv('MODEL4_DATASET_DISTRICT.csv')
dataset=dataset.iloc[:,0:5]
dataset1=dataset1.iloc[:,0:5]

#Converting name into number
for i in range(1,11):
    dataset1.iloc[5*(i-1):5*i,1]=i-1
    
#Converting crop name into number
for i in range(0,32):
    dataset.iloc[i:i+1,0]=i
    
#Predicting measures on the basis of temperature
T=dataset1.iloc[:,4:5]
Tlow=dataset.iloc[:,1:2]
Thigh=dataset.iloc[:,2:3]

#prediction
t_pred={}
#k represents district and j represents crop(input will be taken from user)

j=0 #default input for district
k=0 #default input for crop
         
for i in range(5*k,5*(k+1)):
    if T.iloc[i,0]>Tlow.iloc[j,0]:
         if T.iloc[i,0]<Thigh.iloc[j,0]:
             t_pred[i]=0
         else:
             t_pred[i]=1
    else:
         t_pred[i]=-1

countpos=0
countzero=0
countneg=0
for i in range(0,5):
    if t_pred[i]==1:
        countpos=countpos+1
    elif t_pred[i]==0:
        countzero=countzero+1
    else:
        countneg=countneg+1
if countpos>countzero and countpos>countneg:
    print("Moisture loss will occur due to rise in temperature. Sprinkle water on regular interval for good results!")
elif countneg>countpos and countneg>countzero:
    print("Add sufficient amount of water for better seed germination")
else:
    print("Favourable temperature for crop yeild")
    

#Predicting measures on the basis of rainfall

R=dataset1.iloc[:,3:4]
Rlow=dataset.iloc[:,3:4]
Rhigh=dataset.iloc[:,4:5]

#prediction
r_pred={}
#k represents district and j represents crop(input will be taken from user)

j=0 #default input for district
k=0 #default input for crop
         
for i in range(5*k,5*(k+1)):
    if R.iloc[i,0]>Rlow.iloc[j,0]:
         if R.iloc[i,0]<Rhigh.iloc[j,0]:
             r_pred[i]=0
         else:
             r_pred[i]=1
    else:
         r_pred[i]=-1

countpos=0
countzero=0
countneg=0
for i in range(0,5):
    if r_pred[i]==1:
        countpos=countpos+1
    elif r_pred[i]==0:
        countzero=countzero+1
    else:
        countneg=countneg+1
if countpos>countzero and countpos>countneg:
    print("Less water required for irrigation. And check for water logging!")
elif countneg>countpos and countneg>countzero:
    print("Use more water for irrigation!")
else:
    print("Favourable temperature for crop yeild")
