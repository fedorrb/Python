import sys
text = sys.argv[1].lower()
text1 = ""
text2 = ""
for letter in text:
    if(letter != " "):
        text1 = letter + text1
        text2 = text2 + letter
if text1 == text2:
    print "YES"
else:
    print "NO"