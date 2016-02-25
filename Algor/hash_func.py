# -*- coding: utf-8 -*-
#from cpmoptimize import cpmoptimize
#формування хеш таблиці по вхідному масиву A
#@cpmoptimize()
def Hash_S(A):
    D = {} #словник (хеш : список значеннь)
    h = 0
    arr = [] #ланцюг для колізій
    for a in A:
        h = hash(a)
        if D.has_key(h):
            arr = D[h]
            arr.append(a)
            D[h] = arr
        else:
            D[h] = [a]

    return D
#пошук у словнику хеш значення числа 'y'
def HashSearch(D, y):
    h = hash(y)
    c = 0
    if D.has_key(h):
        arr = D[h]
        if y in arr:
            c = 1 #len(D[h])
##        else:
##            #debug only
##            print str(y) + '  ' + str(arr)
    return c

