def calculator():
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Perform calculation based on the operation
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == "/":
        # Handle division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid operation. Please use +, -, *, or /")

# Call the calculator function
if __name__ == "__main__":
    print("Welcome to the Basic Calculator")
    calculator()