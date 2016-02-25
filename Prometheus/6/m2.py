#import string
# windows-1251
# -*- coding: utf-8 -*-
def convert_n_to_m(x, n, m):
    import string
    def check_str_x(str_x, all_num, osn):
        all_num_osn = all_num.keys()
        all_num_osn.sort()
        all_num_osn = all_num_osn[:osn]
        for c in str_x:
            if (c in all_num_osn) == False:
                return False
        return True
    #fill all_numbers
    minus = False
    alphabet = string.ascii_uppercase
    digit = string.digits
    numbers = digit + alphabet
    all_numbers = {}
    i = 0
    while i < len(digit):
        all_numbers[digit[i]] = i
        i = i + 1
    while i < len(alphabet) + 10:
        all_numbers[alphabet[i-10]] = i
        i = i + 1
    #check x for chars
    type_x = type(x)
    if type_x != int and type_x != str and type_x != long:
        return False
    x = str(x)
    x = x.upper()
    #minus
    if x[0] == '-':
        minus = True;
        x = x[1:]
        return False
    if check_str_x(x, all_numbers, n) == False:
        return False
    int10 = 0
    power = 0
    pos = 0
    #convert to int 10
    if m == n:
        return x
    if n == 10:
        int10 = int(x)
    if n != 10:
        if n == 1:
            int10 = len(x)
        if n != 1:
            #int10 = int(x, 10)
            power = len(x) - 1
            pos = 0
            while pos < len(x):
                int10 = int10 + all_numbers.get(x[pos]) * n ** power
                pos = pos + 1
                power = power - 1
    #convert to m
    ost = 0
    cha = 0
    result = ''
    if m == 1:
        result = '0' * int10
    elif m == 10:
        result = str(int10)
    else:
        while int10 >= m:
            #dm = divmod(int10,m)
            cha = int10 // m
            ost = int10 % m
            int10 = cha
            result = numbers[ost] + result
        result = numbers[cha] + result

    return result
#print convert_n_to_m("A1Z",36,16)
#print convert_n_to_m(777L, 10, 2)
#print convert_n_to_m('qweasd', 33, 36)
#print convert_n_to_m('bnh34521', 31, 14)
#print convert_n_to_m(123123123123123123123, 10, 10)
print convert_n_to_m(123123123123123123123, 11, 16)

