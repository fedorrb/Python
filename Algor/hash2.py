import math
a = float(0.000001)
delta = float(0.000001)
while a < 1.0:
    a1 = (1/a)*math.log(1/(1-a))
    a2 = 1/(1-a)
    if abs((a2/2.0 - a1)) < delta:
        #print 'a1 = ' + str(a1)
        #print 'a2 = ' + str(a2)
        print 'a = ' + str(a)
    a += delta