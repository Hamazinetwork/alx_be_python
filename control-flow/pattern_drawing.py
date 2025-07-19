# square_pattern.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to control the rows
while row < size:
    # Use a for loop to print a row of asterisks
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
