key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
import sys
#text1 = sys.argv[1]
text2 = sys.argv[1].replace(' ', '')
i = 0
part1 = ""
letter1 = ""
result = ""
def FindLetter():
    letterPosition = key.find(part1)
    trueLetter = alphabet[letterPosition]
    return trueLetter
for letter in text2:
    if(letter == letter.upper()):
        letter1 = "b"
    else:
        letter1 = "a"
    part1 = part1 + letter1
    if len(part1) == 5:
        result = result + FindLetter()
        part1 = ""
print result