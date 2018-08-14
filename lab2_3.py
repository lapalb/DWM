# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 15:01:55 2018

@author: Ashish Jha
"""
#normalize between 0 and 1

#Importing Libraries 

import numpy as np
from scipy import stats
import pandas as pd
import statistics as s

#Defining MinMax Scaler
def minmax(data):
    data=np.array(data)
    return (data-min(data))/(max(data)-min(data))

#Defining Z-score  Scaler
def zscore(data):
    data=np.array(data)
    mean = np.mean(data)
    std=np.std(data)
    b=(data-mean)/std
    return b

#Defining Decimal Scaler
def decimal(data):
    data=np.array(data)
    return [item/pow(10,len(str(int(max(data))))) for item in data]
  
df=pd.read_csv('cancerData.csv')
data = df['TumourSize'].fillna(df['TumourSize'].mean()).tolist()#[100,58,1,100000,222]
print("The Data is \n",data)


print("After MinMax Normalisation We get, :\n",minmax(data))
print("\nAfter Z score Normalisation We get, :\n",(data))
print("\nAfter Decimel Normalisation We get, :\n",decimal(data))