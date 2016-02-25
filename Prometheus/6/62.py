def encode_morze(text):
    morse_code1 = {
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--.."
    }
    output = ''
    text = str(text)
    text = text.upper()
    text = text.split(' ')
    space_1 = ''
    space_3 = '_' * 3
    space_7 = '_' * 7
    len_text = len(text)
    len_slovo= 0
    i = 0
    j = 0
    while i < len_text:
        slovo = text[i]
        len_slovo = len(slovo)
        if len_slovo > 0:
            j = 0
            while j < len_slovo:
                char = slovo[j]
                if morse_code1.has_key(char):
                    if j > 0:
                        output = output + space_3
                    space_1 = ''
                    for c in morse_code1[char]:
                        if c == '.':
                            output = output + space_1 + '^'
                        if c == '-':
                            output = output + space_1 + '^^^'
                        space_1 = '_'
                j = j + 1
        if i < len_text - 1:
            output = output + space_7
        i = i + 1

    return output
def encode_morze1(text):
    morze = {
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
    }
    encoded = ''
    for i in text:
        to_add = ''
        if i == ' ':
            to_add = '____'
        elif i.upper() in morze.keys():
            to_add = morze[i.upper()].replace('.','^_').replace('-','^^^_') + '__'
        encoded = encoded + to_add

    if len(encoded):
        while encoded[-1] == '_':
            encoded = encoded[:-1]

    return encoded
#print encode_morze('SOS')
#print encode_morze1('SOS')
print encode_morze('abc ')
print encode_morze1('abc ')