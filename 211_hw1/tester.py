# Name: Ling Xiang, Weiqi Hu, Tianyu Zhang
# instructor: Hakam Alomari
# CSE211 A
# Date: February 17, 2019
# Description: HW1, calcaulte the grade of students and then print it out
# Statement identifying: We all work together 
# Python version: Python 3.7.2


f = open("studentGrades.txt", "r") #open and read the text file

list = [] #create an empty list

for line in f: #use for loop to access each line recursively
	li = line.split( ) #add every single element from each line to a list
	quiz =( float(li[1]) + float(li[2]) + float(li[3]) ) /3 * 0.2 #calculate overall quiz grades 
	hw = ( float(li[4]) + float(li[5]) + float(li[6]) + float(li[7]) + float(li[8])) / 5 * 0.3 #calculate overall homework grades
	ex = ( float(li[9]) + float(li[10]) ) /2 * 0.5 #calculate overall exam grades
	avg = round(quiz + hw + ex,1) #calculate overall grades
	if avg > 90: #convert grades to standard letter grades
		grade = "A"
	elif avg > 80:
		grade = "B"
	elif avg > 70:
		grade = "C"
	elif avg > 60:
		grade = "D"
	else:
		grade = "F"	

	a = [li[0], str(avg), grade] #add name, grades, and letter grades to a list
	
	list.append(a)

f.close() #close the file studentGrades.txt

file = open("studentFinal.txt", "w") #open and write to a txt file named studentFinal.txt

for x in list: #use for loop to write name, grades, and letter grades of every students to the output file
	a = ' '.join(x) + " "
	file.write(a)


file.close() #close the output file

