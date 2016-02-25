#i = -8
#i = 0
#i = "008"
#i = 1.0
#i = -0.8
#i = 1234567890
#i = 9999999999999999333228888888888888888L
#i = "987654d"
i = "009999999999999999333228888888888888888"

def count_holes(n):
    def count_holes_str(text):
        j = len(text) - 1
        c = 0
        while j >= 0:
            if text[j] == "4":
                c = c + 1
            if text[j] == "6":
                c = c + 1
            if text[j] == "8":
                c = c + 2
            if text[j] == "9":
                c = c + 1
            if text[j] == "0":
                c = c + 1
            j = j - 1
        return c
    if type(n) == int or type(n) == long:
        text = str(n)
        return count_holes_str(text)
    elif type(n) == str:
        try:
            text = str(int(n))
            return count_holes_str(text)
        except:
            return "ERROR"
    else:
        return "ERROR"
c = count_holes(i)
print c


