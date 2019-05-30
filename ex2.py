# Name: Ling Xiang, Weiqi Hu, Tianyu Zhang
# Instructor: Hakam Alomari
# CSE 211 Ex2 cipher
# Team 7
# 2/21/2019
# Description: A cipher with ROT-13
# Statement identifying: We all work together 
# Python version: Python 3.7.2


key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
        'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
        'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
        'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
        'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
        'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
        'W':'J', 'X':'K', 'Y':'L', 'Z':'M'} 

Alfakey = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo',
        'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett',
        'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar',
        'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango',
        'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee',
        'z':'zulu'}

def cipher(str):
    result = ""
    x = x.lower()
    for x in str:
        if(x in key):
            y = key.get(x)
            result += y
        else:
            result += x
    print(result)

def cipher2(str):
    result = ""
    for x in str:
        if(x in Alfakey and x != " "):
            y = Alfakey.get(x)
            result += y + ' '
        elif(x == " "):
            pass
        else:
            result += "None "
    print(result)


s = "hello world!"
cipher2(s)