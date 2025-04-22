"""Set a starting balance (e.g., $1000).
2. Show a menu: 1. Withdraw 2. Deposit 3. Check Balance 4. Exit.
3. Perform actions based on user input.
4. Prevent overdrawing (no negative balance!).
Use a while True loop and update balance accordingly."""

"""Title: ATM simulator"""

# Pseudocode
# Create 4 different print statements "Withdraw, Deposit, Check Balance, Exit"
# Create 4 different variables with these names
# Create an input statement asking user to type either 1 2 3 4 these numbers will be assigned to the variables
# Create if variables to account for whatever the user picks
# Set a condition saying if number is negative print invalid

print("withdraw - 1")
print("deposit - 2")
print("check Balance - 3")
print("exit - 4")
starting_balance = 1000
while True:

    withdraw_command = "withdraw"
    deposit_command = "deposit"
    check_balance_command = "check balance"
    exit_command = "exit"
    user_input = input("What would you like to do today? :")

    if user_input == "withdraw":
        withdraw_amount = int(input("How much would you like to withdraw:"))
        starting_balance = starting_balance - withdraw_amount

        print(f"Withdraw successful: New balance:{starting_balance}")
    elif user_input == "deposit":
        deposit_amount = int(input("How much would you like to deposit:"))
        starting_balance = starting_balance + deposit_amount
        print(f"Deposit successful: New balance:{starting_balance}")
    elif user_input == "check balance":
        print(starting_balance)
    elif user_input == "exit":
        break
































































"""    if user_input == "check balance":
        print(starting_balance)
    elif user_input == "exit":
        print("Goodbye")
        break
    elif user_input == "withdraw":
        withdraw_amount = int(input("How much would you like to withdraw? :"))
        if withdraw_amount > starting_balance:
            print("Invalid amount")
        elif starting_balance > withdraw_amount > 0:
            print(f" {withdraw_amount} has been withdrawn")
    elif user_input == "deposit":
        deposit_amount = int(input("How much would you like to deposit :"))
        if deposit_amount == deposit_amount:
            print(f"{deposit_amount} has been deposited")
            print(f"new balance:{deposit_amount + starting_balance} ")"""
