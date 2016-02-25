import sys
a1 = sys.argv[1]
a2 = sys.argv[2]
sumcounter = 0
str1 = ""
str2 = ""
sum1 = 0
sum2 = 0

while int(a1) <= int(a2):
    while len(a1) < 6:
        a1 = "0" + a1
    while len(a2) < 6:
        a2 = "0" + a2
    str1 = a1[:3]
    str2 = a1[3:]
    for j in str1:
        sum1 += int(j)
    for x in str2:
        sum2 += int(x)
    if sum1 == sum2:
        sumcounter += 1
    a1 = int(a1)+1
    a1 = str(a1)
    sum1 = 0
    sum2 = 0

print sumcounter