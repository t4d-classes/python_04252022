
result = 0

history = []


def entry_id(entry):
    return entry[0]

def get_next_id(history):
    # return max(list(map(entry_id, history))) + 1
    ids = [ entry[0] for entry in history ]
    if len(ids) == 0:
        return 1
    else:
        return max(ids) + 1

    # max_id = 0

    # for entry in history:
    #     if max_id < entry[0]:
    #         max_id = entry[0]
    
    # return max_id + 1

command = input("Please enter a command > ")

while command:

    if command == "add":
        operand = float(input("Please enter an operand > "))
        result = result + operand
        history.append((get_next_id(history), 'add', operand))
        #print("Result: " + str(result))
        print(f"Result: {result}")
    elif command == "subtract":
        operand = float(input("Please enter an operand > "))
        result = result - operand
        history.append((get_next_id(history), 'subtract', operand))
        #print("Result: " + str(result))
        print(f"Result: {result}")
    elif command == "multiply":
        operand = float(input("Please enter an operand > "))
        result = result * operand
        history.append((get_next_id(history), 'multiply', operand))
        #print("Result: " + str(result))
        print(f"Result: {result}")
    elif command == "divide":
        operand = float(input("Please enter an operand > "))
        result = result / operand
        history.append((get_next_id(history), 'divide', operand))
        #print("Result: " + str(result))
        print(f"Result: {result}")
    elif command == "history":
        for historyEntry in history:
            print(historyEntry)
    elif command == "remove":
        historyEntryId = int(input("Please enter a history entry id > "))
        for historyEntry in history:
            if historyEntry[0] == historyEntryId:
                history.remove(historyEntry)
    elif command == "clear":
        result = 0
        history = []
        print(f"Result: {result}")
    else:
        print("unknown command, please try again")

    command = input("Please enter a command > ")