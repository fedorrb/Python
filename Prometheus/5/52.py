a = 12345
b = 99999
a = 12303211
b = 100212811

def counter1(a, b):
    num = 0
    a_str = str(a)
    b_str = str(b)
    found = ''
    for char_b in b_str:
        if a_str.find(char_b) != -1 and found.find(char_b) == -1:
            num = num + 1
            found = found + char_b
    return num
#*******************************************
def counter(a, b):
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
    list_a = list(str(a))
    list_b = list(str(b))
    list_a = clean_list(list_a)
    list_b = clean_list(list_b)
    c = 0
    for i in list_b:
        for j in list_a:
            if i == j:
                c = c + 1
    return c

print counter(a, b)
