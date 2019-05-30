# Name: Ling Xiang, Weiqi Hu, Tianyu Zhang
# instructor: Hakam Alomari
# CSE211 A
# Date: February 26, 2019
# Description: HW2, Load a book information file and printed in a nice format
# Statement identifying: We all work together 
# Python version: Python 3.7.2



f = open("Step3Data.txt", "r")
articleDic = {}     # Dictionary of the article info
key = ""
value = ""
categ = 0
journalDate = ""
conferenceDate = ""

for line in f:      # read the file line by line using for loop
    a = line.split()    # split the line into list by space
    if a[0] == "Book":      # if it is a book, then the category would be 1
        value = ""
        key = ""
        categ = 1
    elif a[0] == "Journal":     #Journal as 2
        value = ""
        key = ""
        categ = 2
    elif a[0] == "Conference":      # Conference as 3
        value = ""
        key = ""
        categ = 3
    elif a[0] == "Key:":       # Key is in the index of 1 of the list
        key = a[1]
    elif a[0] == "Author:": 
        if len(a) > 3:          # if the number of author is greater than 3, 
                                # change the order the first author
            temp = a[1]
            a[1] = a[2]
            a[2] = temp + ","
            value += " ".join(a[1:len(a)]) + ", "
        else:
            value += a[2] + ", " + a[1] + ", "      # if the number of author is 1, add comma between first and last name
    elif a[0] == "Title:":                  # If the line starts with "Title", add it to string
        value += " ".join(a[1:len(a)]) + ", "
    elif a[0] == "Conference:":             # If the line starts with "Conference: ", add info to string
        value += "in Proceedings of " + " ".join(a[1:len(a)]) + ", "
    elif a[0] == "Location:":               # If the line starts with "Location", add info to string
        value += a[1] + " " + a[2] + ", " + conferenceDate
    elif a[0] == "Journal:":                # If the line starts with "Journal: ", add info to string
        value += " ".join(a[1:len(a)]) + ", "
    elif a[0] == "Publisher:" and categ == 1:      # If the line starts with "Publisher: " and it is a book, add info to string
        value += " ".join(a[1:len(a)]) + ", "
    elif a[0] == "Publisher:" and categ == 2:       # If the line starts with "Publisher" and it is a journal, add info to string
        value += " ".join(a[1:len(a)]) + ":"
    elif a[0] == "Date:" and categ == 2:        # If the line starts with "Date" and it is a journal, add info to string
        journalDate = a[1]
    elif a[0] == "Date:" and categ == 3:        # If the line starts with "Date" and it is a conference, change the style and add it to string
        conferenceDate = a[1] + " "+ a[2] + " "+ a[3].replace(".","")+ ", "
    elif a[0] == "Volume:":         # If the line starts with "Volumen", add it with (
        value += a[1]+ "("
    elif a[0] == "Number:":
        value += a[1] + "), " + journalDate + "."   # Close )
        articleDic[key] = value         # add it to dic
    elif a[0] == "Date:" and categ == 1:    # If the line starts with Date and it is a book, add . to the string
        value += a[1] + "."
        articleDic[key] = value         # add it to dic
    elif a[0] == "Pages:":      
        value += "".join(a[1:len(a)]) + "."
        articleDic[key] = value         # add it to dic


for x in articleDic:                    # print the keys and value one by one
    print(x + "\t" + articleDic.get(x))
