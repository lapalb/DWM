# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:45:08 2018

@author: Student
"""
from math import *
def euclidean(x,y):
    return sqrt(sum([pow(a-b,2) for a,b in zip(x,y)]))

def manhattan(x,y):
    return (sum([abs(a-b) for a,b in zip(x,y)]))
def p_root(val,p):
    power=1/p
    return pow(val,power)
def minkowski(x,y,p):
    return p_root(sum([pow(abs(a-b),p) for a,b in zip(x,y)]),p)
x=[3,5,4,6]
y=[2,3,7,8]
print (euclidean(x,y))
print(manhattan(x,y))
print(minkowski(x,y,2))
print(minkowski(x,y,3))
print(minkowski(x,y,1))

for a,b in zip(x,y):
    print(a,b)