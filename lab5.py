# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 14:40:48 2018

@author: Ashish Jha
#Car Evaluation Dataset
"""

import numpy as np
import pandas as pd
import sklearn 

#Reading the CSV file
df=pd.read_csv('car.data.csv',sep=",",names = ["Cost", "maintenace", "door", "person","Luggage Boot","Safety","CarClass"])
print("The shape of Dataframe is",df.shape)
print("First Few lines are :\n",df.head())


#describing the Attribute
print("The Attributes are:\n" ,df.describe())

#Printing the unique value
print("The Unique value in person columns are: ",df.loc[:,'person'].unique())
print("The Unique value in door columns are: ",df.loc[:,'door'].unique())
print(df.shape[0])

#Calculation of Gini Index of target
c1=(df.loc[df['CarClass']=='unacc'].count())/df.shape[0]
c2=(df.loc[df['CarClass']=='acc'].count())/df.shape[0]
c3=(df.loc[df['CarClass']=='good'].count())/df.shape[0]
c4=(df.loc[df['CarClass']=='vgood'].count())/df.shape[0]

#GiniIndex
print("The Gini Index is ",1-(c1**2+c2**2+c4**2+c3**2))

