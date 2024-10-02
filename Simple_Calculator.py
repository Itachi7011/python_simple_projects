print("Welcome to the Calculator Program!")


while True:

    # Get user input for the operation
    operation = input("Enter an operation (+, -, *, /) or 'q' to quit: ")

    if operation == "q":

        break

    # Get user input for the numbers

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the operation

    if operation == "+":

        result = num1 + num2

    elif operation == "-":

        result = num1 - num2

    elif operation == "*":

        result = num1 * num2

    elif operation == "/":

        if num2 != 0:

            result = num1 / num2

        else:

            print("Error: Division by zero!")

            continue

    else:

        print("Error: Invalid operation!")

        continue

    # Print the result

    print(f"Result: {num1} {operation} {num2} = {result:.2f}")
