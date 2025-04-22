first_number = int(input("What is your first number? :"))
second_number = int(input("What is your second number? :"))
third_number = int(input("What is your third number? :"))
sum_of_numbers = first_number + second_number + third_number
average_of_numbers = sum_of_numbers // 3
product_of_numbers = first_number * second_number * third_number



print("The sum of all the numbers is :", sum_of_numbers)
print("The average of all the numbers is :", average_of_numbers)
print("The product of all the numbers is :", product_of_numbers)

if first_number > second_number and first_number > third_number:
    print("The largest number is :", first_number)

if second_number > first_number and second_number > third_number:
    print("The largest number is :", second_number)

if third_number > first_number and third_number > second_number:
    print("The largest number is :", third_number)

if first_number < second_number and first_number < third_number:
    print("The smallest number is :", first_number)

if second_number < first_number and third_number:
    print("The smallest number is :", second_number)

if third_number < first_number and second_number:
    print("The smallest number is :", third_number)

