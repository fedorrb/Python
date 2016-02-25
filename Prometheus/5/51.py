import sys
text = [2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5]
text1 = [2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5]
#text = [32, 32.1, 32.0, -123]
#text = ['qwe', 'reg', 'qwe', 'REG']
#text1 = ['qwe', 'reg', 'qwe', 'REG']
#text = [1, 1.0, '1', -1, 1]
def clean_list(list_to_clean):
    list_to_clean = list(list_to_clean)
    temp_list = list(list_to_clean)
    list_to_clean.reverse()
    temp_list.sort()
    old = None
    for i in temp_list:
        if old == i and type(old) == type(i):
            list_to_clean.remove(i)
        old = i
    list_to_clean.reverse()
    return list_to_clean
#**************************************************
def clean_list1(list_to_clean):
    flag = True
    list_new = []
    for element in list_to_clean:
        flag = True
        for i in list_new:
            if i == element and str(i) == str(element):
                flag = False
        if flag:
            list_new.append(element)
    return list_new
#*******************************************
def clean_list2(list_to_clean):
    c = []
    f = set() #mnojestvo
    for obj in list_to_clean:
        f.add((type(obj), obj,))
    for pair in f:
        c.append(pair[1])
    return sorted(c)
#*********************************************
print clean_list(text)
print clean_list2(text1)