# HW2

file = open("Step1Data.txt", "r")

bookDic = {}

s = ""
for line in file:
    if(line == "Book\n" and s):
        bookDic[key] = s[0: len(s) - 2]
        s = ""
    elif(line == "Book\n"):
        s = ""
    elif(line[0: line.index(":")] == "Key"):
        key = line[line.index(":") + 2: len(line) - 1]
    else:
        s += line[line.index(":") + 2 : len(line) - 1] + ", "