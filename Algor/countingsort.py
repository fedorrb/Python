# -*- coding: utf-8 -*-
import os, sys, copy
import string
f = open(r"input_1000_str.txt","r").read()
#read file to list
A = f.split('\n')
B = copy.deepcopy(A)
#f.close()

#start sort list
#масиви A,B; колонка масиву A; максимальна кількість можливих значень елементу в колонці А
def CountingSort(masA, masB, colA, k):
    ord_a = ord('a')
    C = []
    for i in range(k):
        C.append(0)
    for elA in colA:
        C[ord(elA)-ord_a] += 1
    i = 1
    while i < c_size:
        C[i] = C[i] + C[i-1]
        i += 1
    #array C ready
    i = len(colA) - 1
    posB = 0
    while i >= 0:
        charA = colA[i]
        posB = C[ord(charA)-ord_a]-1
        C[ord(charA)-ord_a] -= 1
        masB[posB] = masA[i]
        i -= 1
    return masB

alphabet = string.ascii_lowercase
c_size = len(alphabet)#k
colMasA = []
d = range(len(A[0]))
d.reverse()  #d = d[::-1]
for j in d:
    colMasA = [row[j] for row in A] #j-я колонка списка (не строка)
    B = CountingSort(A, B, colMasA, c_size)
    A = copy.deepcopy(B)
#сортування закінчено

#count alphabets
C = []
ord_a = ord('a')
for i in range(c_size):
    C.append(0)
for j in d:
    colMasA = [row[j] for row in A]
    for elA in colMasA:
        C[ord(elA)-ord_a] += 1
print sum(C)
m = max(C)
for i in C:
    if i == m:
        print chr(i+97)