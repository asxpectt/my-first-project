# Initialize variables
# Ask user to input exam grades
# Find average of exam grades
# Tell user to stop entering grades when they input -1
# Display highest and lowest grades entered

grades = 0
number_of_grades_entered = int(input("How many grades do you plan to enter?:"))
while True:
    grade = int(input("Type in grade (or -1 to stop): "))
    if grade == -1:
        break





    print(number_of_grades_entered * grade)
