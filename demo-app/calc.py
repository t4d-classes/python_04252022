
result = 0

command = input("Please enter a command > ")

while command:

    if command == "add":
        operand = float(input("Please enter an operand > "))
        result = result + operand
        #print("Result: " + str(result))
        print(f"Result: {result}")
    elif command == "subtract":
        operand = float(input("Please enter an operand > "))
        result = result - operand
        #print("Result: " + str(result))
        print(f"Result: {result}")
    elif command == "multiply":
        operand = float(input("Please enter an operand > "))
        result = result * operand
        #print("Result: " + str(result))
        print(f"Result: {result}")
    elif command == "divide":
        operand = float(input("Please enter an operand > "))
        result = result / operand
        #print("Result: " + str(result))
        print(f"Result: {result}")
    elif command == "clear":
        result = 0
        print(f"Result: {result}")
    else:
        print("unknown command, please try again")

    command = input("Please enter a command > ")