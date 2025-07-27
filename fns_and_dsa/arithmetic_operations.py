def perfom_operations(num1, num2 , operations):
    if operations == "+":
        return num1 + num2
    elif operations == "-":
        return num1 - num2
    elif operations == "*":
        return num1 * num2
    elif operations == "/":
        return num1 / num2
    else:
        return "invalid operation"