# Get the desired size of the square pattern from the user
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the rows
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Inside the while loop, use a for loop to print the columns (asterisks)
    # The 'range(size)' ensures we print 'size' number of asterisks
    for _ in range(size):
        # Print an asterisk, and use end="" to prevent moving to a new line
        print("*", end="")

    # After the inner for loop completes, print a newline to move to the next row
    print()

    # Increment the row counter to eventually exit the while loop
    row += 1