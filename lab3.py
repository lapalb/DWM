# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 16:35:59 2018

@author: Ashish Jha
"""
import itertools
support = int(input("Enter support value in  "))
confidence = int(input("Enter confidence value in %: "))

"""Compute candidate 1-itemset"""
C1 = {}
"""total number of transactions contained in the file"""
transactions = 0
D = []
T = []
with open("test.txt", "r") as f:
    for line in f:
        T = []
        transactions += 1
        for word in line.split():
            T.append(word)
            if word not in C1.keys():
                C1[word] = 1
            else:
                count = C1[word]
                C1[word] = count + 1
        D.append(T)
print ("-------------------------TEST DATASET----------------------------")
print(D)

print ("-------------------------Dictionary Contains----------------------------")
for k in C1:
    print(k,C1[k])

"""Compute frequent 1-itemset"""
L1 = []
for key in C1:
    if (100 * C1[key]/transactions) >= support:
        list = []
        list.append(key)
        L1.append(list)
print("----------------------FREQUENT 1-ITEMSET-------------------------")
print(L1)
print ("-----------------------------------------------------------------")
def apriori_gen(Lk_1, k):
    length = k
    Ck = [] #Candidate K ItemSet
    for list1 in Lk_1:
        for list2 in Lk_1:
            count = 0
            c = []
            if list1 != list2:
                while count < length-1:
                    if list1[count] != list2[count]:
                        break
                    else:
                        count += 1
                else:
                    if list1[length-1] < list2[length-1]:
                        for item in list1:
                            c.append(item)
                        c.append(list2[length-1])
                        if not has_infrequent_subset(c, Lk_1, k):
                            Ck.append(c) 
                            c = []
    return Ck


def findsubsets(S,m):
    return set(itertools.combinations(S, m))

def has_infrequent_subset(c, Lk_1, k):
    list = []
    list = findsubsets(c,k)
    for item in list: 
        s = []
        for l in item:
            s.append(l)
        s.sort()
        if s not in Lk_1:
            return True
    return False

def frequent_itemsets():
    k = 2
    Lk_1 = []
    Lk = []
    L = []
    count = 0
    transactions = 0
    for item in L1:
        Lk_1.append(item)
    while Lk_1 != []:
        Ck = []
        Lk = []
        Ck = apriori_gen(Lk_1, k-1)
        #print "-------------------------CANDIDATE %d-ITEMSET---------------------" % k
        #print "Ck: %s" % Ck
        #print "------------------------------------------------------------------"
        for c in Ck:
            count = 0
            transactions = 0
            s = set(c)
            for T in D:
                transactions += 1
                t = set(T)
                if s.issubset(t) == True:
                    count += 1
            if (100 * count/transactions) >= support:
                c.sort()
                Lk.append(c)
        Lk_1 = []
        print ("-----------------------FREQUENT ", k," ITEMSET------------------------") 
        print (Lk)
        print ("------------------------------------------------------------------")
        for l in Lk:
            Lk_1.append(l)
        k += 1
        if Lk != []:
            L.append(Lk)
    
    return L
     

def generate_association_rules():
    s = []
    r = []
    length = 0
    count = 1
    inc1 = 0
    inc2 = 0
    num = 1
    m = []
    L= frequent_itemsets()
    print ("---------------------ASSOCIATION RULES------------------")
    print ("RULES \t SUPPORT \t CONFIDENCE")
    print ("--------------------------------------------------------")
    for list in L:
        for l in list:
            length = len(l)
            count = 1
            while count < length: 
                s = []
                r = findsubsets(l,count)
                count += 1
                for item in r:
                    inc1 = 0
                    inc2 = 0
                    s = []
                    m = []
                    for i in item:
                        s.append(i)
                    for T in D:
                        if set(s).issubset(set(T)) == True:
                            inc1 += 1
                        if set(l).issubset(set(T)) == True:
                            inc2 += 1
                    if 100*inc2/inc1 >= confidence:
                        for index in l:
                            if index not in s:
                                m.append(index)
                        print ("Rule#  %d : %s==>%s %d %d" %(num, s, m, 100*inc2/len(D), 100*inc2/inc1))
                        num += 1  

generate_association_rules()   

