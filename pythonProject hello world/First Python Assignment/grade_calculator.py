#Ask student to input their score
#Grades are
#A-90-100
#B:80-89
#C: 70-79
#D: 60-69
#F:Below 60
#Create a condition to check if the input score is valid
#If it is not valid print "invalid score"

grade = int(input("What is your grade score:"))

if grade < 0 or grade > 100:
    print("This is an Invalid score")

if grade < 60:
    print("Your grade is an F")

if 60 <= grade < 69:
    print("Your grade is a D")

if 70 <= grade < 79:
    print("Your grade is a C")

if 80 <= grade < 89:
    print("Your grade is a B")

if 90 <= grade < 100:
    print("Your grade is an A")







