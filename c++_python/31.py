import sys
triangle = 0
try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
except NameError:
    a = 0
    b = 0
    c = 0
def CheckABC():
    result = 0
    if a > 0:
        if b > 0:
            if c > 0:
                result = 1
    return result
triangle = CheckABC()
if triangle == 1:
    gipot = max(a, b, c)
    sum_all = a + b + c
    sum_katet = sum_all - gipot
    if sum_katet <= gipot:
        triangle = 0;
if triangle == 1:
    print "triangle"
else:
    print "not triangle"
