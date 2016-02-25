import sys
first = int(sys.argv[1])
last = int(sys.argv[2])
count = 0
sum_half1 = 0
sum_half2 = 0
half1 = 0
half2 = 0
s1 = 0;
s2 = 0;
s3 = 0;
def SumHalf(half):
    s1 = half // 100
    s2 = (half - s1*100) // 10
    s3 = half - s1*100 - s2*10
    return  s1 + s2 + s3

for i in range(first, last + 1):
    half1 = i // 1000;
    half2 = i % 1000
    sum_half1 = SumHalf(half1)
    sum_half2 = SumHalf(half2)
    if sum_half1 == sum_half2:
        count = count + 1
print count
""" f = i % 10
    a = i / 10 % 10
    b = i / 100 % 10
    c = i / 1000 % 10
    d = i / 10000 % 10
    e = i / 100000 % 10"""