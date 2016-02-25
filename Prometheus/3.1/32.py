import sys
try:
    n = int(sys.argv[1])
except NameError:
    n = -1
a = 0
b = 1
c = 0
if n > 2:
    for i in range(n-1):
        c = a + b
        a, b = b, c
if n == 1:
    c = 1
if n == 2:
    c = 1
print c
