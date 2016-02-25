import sys
text = [1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5]
# text = [32, 32.1, 32.0, -123]
# text = ['qwe', 'reg', 'qwe', 'REG']
# text = [1, 1.0, '1', -1, 1]
def clean_list(list_to_clean):
    found = []
    for element in list_to_clean:
        flag = False
        for i in found:
            if i == element and str(i) == str(element):
                flag = True
        if not flag:
            found.append(element)
    return found
def clean_list1(list_to_clean):
    list_to_clean = list(list_to_clean)
    list_to_clean.reverse()
    temp_list = list(list_to_clean)
    old = None
    new = None
    i = len(temp_list) - 1
    j = i
    r = 0
    while i > 0:
        r = 0
        j = i - 1
        old = temp_list[i]
        while j >= 0:
            new = temp_list[j]
            if old == new and type(old) == type(new):
                list_to_clean.remove(new)
                temp_list.remove(new)
                r = r + 1
            j = j - 1
        i = i - r
        i = i - 1
    list_to_clean.reverse()
    return list_to_clean

text = clean_list(text)
print text