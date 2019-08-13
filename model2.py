#importing python module
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing dataset
dataset=pd.read_csv('Model2.csv')

#Calculating the number of feedbacks

import array  
arr=array.array('i',[])
brr=array.array('i',[])

c1=0
c2=0
c3=0
c4=0
c5=0

for i in range(0,19):
    if dataset.iloc[i,0]==1:
        c1=c1+1
    if dataset.iloc[i,0]==2:
        c2=c2+1
    if dataset.iloc[i,0]==3:
        c3=c3+1
    if dataset.iloc[i,0]==4:
        c4=c4+1
    if dataset.iloc[i,0]==5:
        c5=c5+1
        
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)
brr.append(c1)
brr.append(c2)
brr.append(c3)
brr.append(c4)
brr.append(c5)


