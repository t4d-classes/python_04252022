result = 0

history = []

def get_operand():
  return float(input("Please enter an operand > "))

def append_to_history(history, opName, opValue):
  history.append((get_next_id(history), opName, opValue))

def output_result(result):
  print(f"Result: {result}")

def entry_id(entry):
    return entry[0]

def get_next_id(history):
    return max(list(map(entry_id, history))) + 1

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

def command_output_history(history):
  for historyEntry in history:
      print(historyEntry)

def command_remove_history_entry(history):
    historyEntryId = int(input("Please enter a history entry id > "))
    for historyEntry in history:
        if historyEntry[0] == historyEntryId:
            history.remove(historyEntry)

def command_clear():
    global result, history
    result = 0
    history = []

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
        command_output_history(history)
    elif command == "remove":
        command_remove_history_entry(history)
    elif command == "clear":
        command_clear()
    else:
        print("unknown command, please try again")

    command = input("Please enter a command > ")