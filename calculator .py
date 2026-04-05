# This program performs basic arithmetic operations using a function

def calculator():
    # Ask the user to enter the first number
    num1 = float(input("Enter first number: "))
 
    # Ask the user to choose an operator
    operation = input("Enter operator (+, -, *, /): ")
 
    # Ask the user to enter the second number
    num2 = float(input("Enter second number: "))

    # Perform the operation based on the user's choice
    if operation == "+":
        print("Result:", num1 + num2)
    elif operation == "-":
        print("Result:", num1 - num2)
    elif operation == "*":
        print("Result:", num1 * num2)
    elif operation == "/":
        # Check for division by zero
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero")
    else:
        # Handle invalid operator input
        print("Invalid operator")

# Call the function to run the calculator
calculator()
