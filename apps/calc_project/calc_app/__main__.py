from calc_app.common.input import float_input, int_input
from calc_app.common.output import output_result, output_history
from calc_app.models.history import CalcHistory, HistoryEntry


def calc_result(history):
    result = 0
    for history_entry in history:
        op_value = history_entry.op_value
        math_op = history_entry.math_op
        result = math_op(result, op_value)
    return result


def command_math_op(history, math_op, math_op_name):
    operand = float_input("Enter an operand > ")
    history.append(HistoryEntry(math_op_name, operand, math_op))
    output_result(calc_result(history))


def count_ops_in_history(history):
    """ counts the frequency of the different operations in the history """

    op_counts = {}

    for history_entry in history:
        op_name = history_entry.op_name
        op_counts[op_name] = op_counts.get(op_name, 0) + 1

    return op_counts


def command_output_history(history):
    op_counts = count_ops_in_history(history)
    output_history(history, op_counts)


def command_remove_history_entry(history):
    history_entry_id = int_input("Please enter a history entry id > ")
    history.remove(history_entry_id)


def command_clear(calc_history):
    calc_history.clear()


def app():

    calc_history = CalcHistory()

    command = input("Please enter a command > ")

    while command:

        if command == "add":
            command_math_op(calc_history, lambda a, b: a + b, "add")
        elif command == "subtract":
            command_math_op(calc_history, lambda a, b: a - b, "subtract")
        elif command == "multiply":
            command_math_op(calc_history, lambda a, b: a * b, "multiply")
        elif command == "divide":
            command_math_op(calc_history, lambda a, b: a / b, "divide")
        elif command == "history":
            command_output_history(calc_history)
        elif command == "remove":
            command_remove_history_entry(calc_history)
        elif command == "clear":
            command_clear(calc_history)
        else:
            print("unknown command, please try again")

        command = input("Please enter a command > ")


app()
