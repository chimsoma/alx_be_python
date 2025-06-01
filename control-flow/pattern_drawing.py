# pattern_drawing.py

# Prompt the user to enter a positive integer for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for rows
while row < size:
    # Use for loop to print asterisks in a row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
