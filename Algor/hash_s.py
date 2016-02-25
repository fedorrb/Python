# -*- coding: utf-8 -*-
import os, sys, copy
import string
from hash_func import *
#from cpmoptimize import cpmoptimize
#import cpmoptimize
#f = open(r"input_06.txt","r").read()
f = open(r"test_061.txt","r").read()
#read file to list
A = f.split('\n')
B = []
n = 0
len_A = len(A)-1
while n < len_A:
    #A[n] = int(A[n])
    B.append(int(A[n])) #масив цілих чисел
    n += 1
counter = 0
y_max = 0
y_min = 0
D = Hash_S(B) #формування хеш таблиці
S = set() #результат роботи буде тут (кількість різних значень S)
found = 0
y = 0
#@cpmoptimize()
def S_Counter(B, S, D, counter):
    for x in B:
        for r in range(1001):
            y = r - x
            found = HashSearch(D, y)
            counter += found
            if found > 0:
                S.add(r)
            y = -1*r - x
            found = HashSearch(D, y)
            counter += found
            if found > 0:
                S.add(-1*r)
##for x in B:
##    for r in range(1001):
##        y = r - x
##        found = HashSearch(D, y)
##        counter += found
##        if found > 0:
##            S.add(r)
##        y = -1*r - x
##        found = HashSearch(D, y)
##        counter += found
##        if found > 0:
##            S.add(-1*r)
S_Counter(B, S, D, counter)
print counter
print len(S)
print S