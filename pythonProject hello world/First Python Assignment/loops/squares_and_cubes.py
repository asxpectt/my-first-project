"""(Table of Squares and Cubes) In Exercise 2.8, you wrote a script to calculate the
squares and cubes of the numbers from 0 through 5, then printed the resulting values in
table format. Reimplement your script using a for loop and the f-string capabilities you
learned in this chapter to produce the following table with the numbers right aligned in
each column."""
print("Number Squares Cubes")

# Create a for loop with a range of numbers 0 - 6
# 
for num in range(6):
    print(f"{num:<7}{num**2:<7} {num**3:<7}")
