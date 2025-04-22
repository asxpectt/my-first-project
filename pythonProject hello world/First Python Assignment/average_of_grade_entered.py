"""# Initialize variables
# Ask user to input exam grades
# Find average of exam grades


# Tell user to stop entering grades when they input -1
# Display highest and lowest grades entered

grade_1 = int(input("What is the first grade (Type -1 to end):"))
grade_2 = int(input("What is the second grade (Type -1 to end):"))
grade_3 = int(input("What is the third grade (Type -1 to end):"))
grade_4 = int(input("What is the fourth grade (Type -1 to end):"))
number_of_grades_entered = int(input("How many grades did you enter?:"))

if grade_1 == -1:
    number_of_grades_entered = 0
    total = 0
elif grade_2 == -1:
    number_of_grades_entered = 1
    total = grade_1
elif grade_3 == -1:
    number_of_grades_entered = 2
    total = grade_1 + grade_2
elif grade_4 == -1:
    number_of_grades_entered = 3
    total = grade_1 + grade_2 + grade_3
else:
    number_of_grades_entered = 4
    total = grade_1 + grade_2 + grade_3 + grade_4

total = grade_4 + grade_1 + grade_2 + grade_3  # Sum of grades
average = total/number_of_grades_entered

print(f"The average of the grades is:{average}")



"""

user_Input = int(input("Enter a number:"))

while user_Input < 5:
    print("Bunmi")
