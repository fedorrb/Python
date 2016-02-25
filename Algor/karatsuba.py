# -*- coding: utf-8 -*-
#добуток x*y=10^n*ac+10^(n/2)*(ad+bc)+bd.
def Karatsuba(x, y, arr):
    dobutok = 0
    result = 0 #(ad+bc)
    x_str = str(x)
    y_str = str(y)
    #вирівнювання довжини x, y
    len_x = len(x_str)
    len_y = len(y_str)
    max_len = max(len_x, len_y)
    zeros_to_add = max_len - len(x_str)
    x_str = zeros_to_add * '0' + x_str
    zeros_to_add = max_len - len(y_str)
    y_str = zeros_to_add * '0' + y_str
    #формування a,b,c,d
    half_len = max_len / 2
    if max_len % 2 != 0:
        half_len += 1

    a = x_str[:half_len]
    b = x_str[half_len:]
    c = y_str[:half_len]
    d = y_str[half_len:]
    #b <= a
    power = len(b)*2
    if len(b) == 1:
        if len(a) > 1:
            ac = Karatsuba(a, c, arr)
        else:
            ac = int(a) * int(c)
        bd = int(b) * int(d)
        #(ad+bc) = (a+b)(c+d)−ac−bd
        sum_a_b = int(a) + int(b)
        sum_c_d = int(c) + int(d)
        if sum_a_b > 9 or sum_c_d > 9:
            mul_sum = Karatsuba(sum_a_b, sum_c_d, arr)
        else:
            mul_sum = sum_a_b * sum_c_d

        result = mul_sum - ac - bd
        dobutok = 10**2*ac + 10*result + bd

        if result == 105:
            arr[2] += 1
        if result == 72:
            arr[1] += 1
        if result == 12:
            arr[0] += 1
    else:
        ac = Karatsuba(a, c, arr)
        bd = Karatsuba(b, d, arr)
        #(ad+bc) = (a+b)(c+d)−ac−bd
        sum_a_b = int(a) + int(b)
        sum_c_d = int(c) + int(d)
        if sum_a_b > 9 or sum_c_d > 9:
            mul_sum = Karatsuba(sum_a_b, sum_c_d, arr)
        else:
            mul_sum = sum_a_b * sum_c_d

        result = mul_sum - ac - bd
        dobutok = 10**power*ac + 10**(power/2)*result + bd

    return dobutok

list_count = [0,0,0]
x = 1685287499328328297814655639278583667919355849391453456921116729
y = 7114192848577754587969744626558571536728983167954552999895348492

x_y = Karatsuba(x, y, list_count)
if x*y != x_y:
    print 'Error'
else:
    print 'OK'
    print str(list_count)
print x_y