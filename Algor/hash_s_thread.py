# -*- coding: utf-8 -*-
import os, sys, copy
import string
import thread, time
import threading
from hash_func import *
#f = open(r"input_06.txt","r").read()
f = open(r"test_06.txt","r").read()
A = f.split('\n')
B = []
n = 0
len_A = len(A)
while n < len_A:
    B.append(int(A[n]))
    n += 1
counter = 0
y_max = 0
y_min = 0
D = Hash_S(B)
S = set()
found = 0
y = 0
finished_thread = set()

def S_Counter(partB, ttt, counter, S, D, finished_thread):
    print 'thread ' + str(ttt) + '  ' + str(len(partB))
    for x in partB:
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
    finished_thread.add(ttt)
    print 'finished thread ' + str(ttt)

len_B = len(B)
part_B = len_B // 4
start = 0

threads = []

for i in range(4):
    thread1 = threading.Thread(target = S_Counter,args = ((B[start:part_B],i,counter,S,D,finished_thread)))
    thread1.start()
    threads.append(thread1)
    start = part_B
    part_B += (len(B) // 4)

for i in range(4):
    thread.start_new_thread(S_Counter,(B[start:part_B],i,counter,S,D,finished_thread))
    start = part_B
    part_B += (len(B) // 4)

while len(finished_thread) < 4:
    pass
print counter
print len(S)
print S
