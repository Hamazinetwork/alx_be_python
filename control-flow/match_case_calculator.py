# User's Input
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
Operation = input("Enter the operation (+, -, *, /): ")

# calculation using match-case
match Operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            result = "Error: Division by zero is not allowed."
    case _:
        result = "Error: Invalid operation."