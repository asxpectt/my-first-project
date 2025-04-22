"""Title: FizzBuzz """

while True:
    input_number = int(input("Type a number from 1-50:"))

    if 1 <= input_number <= 50:
        if input_number % 3 == 0 and input_number % 5 == 0:
            print("FizzBuzz")
        elif input_number % 3 == 0:
            print("Fizz")
        elif input_number % 5 == 0:
            print("Buzz")
        else:
            print(input_number)