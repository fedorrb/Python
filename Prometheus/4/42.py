import sys
size = len(sys.argv) - 1
text = ""
while size > 0:
    text = text + str(sys.argv[size])
    size = size - 1
    if size:
        text = text + " "
print text