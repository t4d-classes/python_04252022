
result = 0

history = []

def get_operand():
  return float(input("Please enter an operand > "))

def append_to_history(history, opName, opValue):
  history.append((get_next_id(history), opName, opValue))

def output_result(result):
  print(f"Result: {result}")



# def entry_id(entry):
#     return entry[0]

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

def perform_math_op(result, math_op, math_op_name):
  operand = get_operand()
  result = math_op(result, operand)
  append_to_history(history, math_op_name, operand)
  output_result(result)
  return result

def do_add(a,b):
  return a + b

def do_subtract(a,b):
  return a - b

def do_multiply(a,b):
  return a * b

def do_divide(a,b):
  return a / b


command = input("Please enter a command > ")

while command:

    if command == "add":
        result = perform_math_op(result, do_add, "add")
    elif command == "subtract":
        result = perform_math_op(result, do_subtract, "subtract")
    elif command == "multiply":
        result = perform_math_op(result, do_multiply, "multiply")
    elif command == "divide":
        result = perform_math_op(result, do_divide, "divide")
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