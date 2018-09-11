# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 14:50:24 2018

@author: Ashish Jha
"""
import numpy as np
import pandas as pd
import sklearn
df=pd.read_csv('car.data.csv',sep=",",names = ["Cost", "maintenace", "door", "person","Luggage Boot","Safety","CarClass"])
print(df.head())

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
for i in df.columns:
    df[i]=le.fit_transform(df[i])
    
print(df.head())

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
sca=[]
x_train,x_test,y_train,y_test=train_test_split(df[df.columns[:-1]],df['CarClass'],random_state=42,test_size=0.2)
for i in range(1,30):
    clf=KNeighborsClassifier(n_neighbors=i)
    clf.fit(x_train,y_train)
    sc=clf.score(x_test,y_test)
    sca.append(sc)
    print("The Score on %d Neighbours is %f" % (i,sc))
ia=list(range(1,30))
plt.xlabel="Number of Neighbours"
plt.ylabel="Accuracy Score"
plt.plot(ia,sca)
#plt.scatter(ia,sca)
    

