# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 01:33:28 2018

@author: Ashish Jha
"""
import math
T=[('E1',8123,83,424,1370),('E2',8330,2,622,1046),('E3',3954,3080,5,2961),
   ('E4',2886,1363,1320,4431),('E5',1500,2000,500,6000),
   ('E6',4000,2000,1000,3000),('E7',9481,298,127,94),
   ('E8',4000,2000,2000,2000),('E9',7450,2483,4,63),
   ('E10',61,2483,4,7452)]
Tnew=[]
for item in T:
        a,b,c,d,e = item
        fplus1=b+d
        fplus0=c+e
        f1plus=b+c
        f0plus=d+e
        n=b+c+d+e
        Tnew.append((a,b,c,d,e,fplus1,fplus0,f1plus,f0plus,n))
#print(Tnew)
oddratio=[]
correlation=[]
kappa=[]
interest=[]
for item in Tnew:
    a,f11,f10,f01,f00,fplus1,fplus0,f1plus,f0plus,n = item
    correlation.append((a,((n*f11-f1plus*fplus1)/(math.sqrt(fplus1*fplus0*f1plus*f0plus)))))
    oddratio.append((a,(f11*f00)/(f01*f10)))
    kappa.append((a,(n*f11+n*f00-f1plus*fplus1-f0plus*fplus0)/(n*n-f1plus*fplus1-f0plus*fplus0)))
    interest.append((a,n*f11/(f1plus*fplus1)))
oddratioS = sorted(oddratio, key=lambda tup:tup[1],reverse=True )
correlationS = sorted(correlation, key=lambda tup:tup[1],reverse=True )
kappaS = sorted(kappa, key=lambda tup:tup[1],reverse=True )
interestS = sorted(interest, key=lambda tup:tup[1],reverse=True )
print('Correlation')
print(correlationS)
print('Odds ratio')
print(oddratioS)
print('Kappa')
print(kappaS)
print('Interest')
print(interestS)
    