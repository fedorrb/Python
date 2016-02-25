import sys
import math
x = float(sys.argv[1])
m = float(sys.argv[2])
b = float(sys.argv[3])
a = 1/(b*math.sqrt(2*math.pi))
e = math.exp((((x-m)**2)/(2*b**2))*(-1))
f = a*e
print f