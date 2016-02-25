import sys
text = sys.argv[1]
d1 = "("
d2 = ")"
result = 1;
i = 0
for letter in text:
    if(letter == d1):
        i = i + 1
    else:
        i = i - 1
    if i < 0:
        result = 0
if i != 0:
    result = 0
if result == 1:
    print "YES"
else:
    print "NO"