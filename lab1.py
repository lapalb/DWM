# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:43:41 2018

@author: Ashish Jha
"""

#Program to find Mean, Mode and Median without numpy or statitics Module

n=int(input("Enter the number of element in the list\n"))
a=list()
for t in range(n):
    x=int(input())
    a.append(x)

print("\n\n========Without Library============\n\n")

#Finding Mean
sum=0
for x in a:
    sum+=x
print("The mean of the Data is ", sum/n)

#Finding Mode
d=dict()
for x in a:
    if x not in d:
        d[x]=1
    else:
        d[x]=d[x]+1
import operator 
sorted_x = sorted(d.items(), key=operator.itemgetter(1))
key1=d[list(d.keys())[0]]
for key, value in d.items():
    if key1 == value:
        print ("The mode is : ",key)
        
#Mode using Counter        
from collections import Counter
data = Counter(a)   # Returns all unique items and their counts
print("The mode is :" ,data.most_common(1)) 

#Finding Median
a.sort()
i=n//2
if(n%2==0):
    print("The median is :",(a[i]+a[i-1])/2)
else:
    print("The median is :",a[i])



#Program to find Mean, Mode and Median using numpy 
print("\n\n========Using Numpy============\n\n")
import numpy as np
ar=np.array(a)
print("The mean according to Numpy Library is :", np.mean(ar))
print("The Median according to Numpy library is :",np.median(ar))

#Program to find Mean, Mode and Median using statistics
print("\n\n========Using Statistics============\n\n")
from statistics import *
print("The Mean according to statistics Library is :", mean(a))
print("The Mode according to statistics Library is :", mode(a))
print("The Median according to statistics library is :",median(a))
 
