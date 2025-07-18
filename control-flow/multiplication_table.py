number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    # This f-string is a more modern way to format the output
    print(f"{number} * {i} = {number * i}")
