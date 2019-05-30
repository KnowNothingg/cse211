file = open("Step2Data.txt", "r")

bookDic = {}
categ = 0


def journal(line, s):
    if(line[0: line.index(":")] == "Author\n"):
        li = line[line.index(":") + 2: len(line) - 1]
        lastName = li[line.index(" ") + 1 : len(li)]
        firstName = li[0: line.index(" ")]
        name = lastName + ", " + firstName + ", "
        s += name
    elif(line[0: line.index(":")] == "Title\n"):
        s += line[line.index(" "): len(line) - 1] + ", "
    elif(line[0: line.index(":")] == "Journal\n"):
        s += line[line.index(" "): len(line) - 1] + ", "
    elif(line[0: line.index(":")] == "Publisher\n"):
        s += line[line.index(" "): len(line) - 1] + ":"
    elif(line[0: line.index(":")] == "Date\n"):
        date = line[line.index(" "): len(line) - 1] + ", "
    elif(line[0: line.index(":")] == "Volume\n"):
        vol = line[line.index(" "): len(line) - 1]
    elif(line[0: line.index(":")] == "Number\n"):
        num = line[line.index(" "): len(line) - 1]
        s += vol + "(" + num + ")" + ", " + date

    print(s)
    return s
  
s = ""

for line in file:
    if((line == "Book\n" or line == "Journal\n") and s):
        bookDic[key] = s[0: len(s) - 2]
        s = ""
    elif(line == "Book\n"):
        categ = 1
        s = ""  
    elif(line == "Journal\n"):
        categ = 2
        s = ""
    elif(line[0: line.index(":")] == "Key"):
        key = line[line.index(":") + 2: len(line) - 1]
    elif(categ == 1):
        s += line[line.index(":") + 2 : len(line) - 1] + ", "
    elif(categ == 2):
        journal(line, s)
    