num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")
match operation:
    case "+":
        print("the result is: " ,num1 + num2)
    case "-":
        print("the result is: " ,num1 - num2)
    case "*":
        print("the result is: " ,num1*num2)
    case "/":
        print("the result is: " ,num1 / num2)
