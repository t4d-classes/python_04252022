

history = []


def calc_result(history):
    result = 0
    for historyEntry in history:
        op_value = historyEntry["op_value"]
        math_op = historyEntry["math_op"]
        result = math_op(result, op_value)
    return result


def get_operand():
    return float(input("Please enter an operand > "))

def append_to_history(history, op_name, op_value, math_op):
    history.append({
        "id": get_next_id(history),
        "op_name": op_name,
        "op_value": op_value,
        "math_op": math_op
    })

def output_result(result):
    print(f"Result: {result}")

def entry_id(entry):
    return entry["id"]

def get_next_id(history):
    if len(history) == 0:
        return 1
    else:
        return max(list(map(entry_id, history))) + 1

def perform_math_op(history, math_op, math_op_name):
    operand = get_operand()
    append_to_history(history, math_op_name, operand, math_op)
    output_result(calc_result(history))

def command_output_history(history):
  
  op_counts = {}
  
  for history_entry in history:
      op_name = history_entry['op_name']
      op_counts[op_name] = op_counts.get(op_name, 0) + 1
      print(history_entry)

  print(op_counts)

  

def command_remove_history_entry(history):
    history_entry_id = int(input("Please enter a history entry id > "))
    for history_entry in history:
        if history_entry["id"] == history_entry_id:
            history.remove(history_entry)

def command_clear():
    global history
    history = []


command = input("Please enter a command > ")

while command:

    if command == "add":
        perform_math_op(history, lambda a,b: a + b, "add")
    elif command == "subtract":
        perform_math_op(history, lambda a,b: a - b, "subtract")
    elif command == "multiply":
        perform_math_op(history, lambda a,b: a * b, "multiply")
    elif command == "divide":
        perform_math_op(history, lambda a,b: a / b, "divide")
    elif command == "history":
        command_output_history(history)
    elif command == "remove":
        command_remove_history_entry(history)
    elif command == "clear":
        command_clear()
    else:
        print("unknown command, please try again")

    command = input("Please enter a command > ")