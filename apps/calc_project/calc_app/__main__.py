from calc_app.common.input import float_input, int_input
from calc_app.common.output import output_result, output_history
from calc_app.models.history import CalcHistory, HistoryEntry
from calc_app.common.logger import Logger
from calc_app.common.calc_ops import (
    calc_ops, count_ops_in_history, calc_result
)


def command_math_op(history, math_op, math_op_name):
    operand = float_input("Enter an operand > ")
    history.append(HistoryEntry(math_op_name, operand, math_op))
    output_result(calc_result(history))


def command_output_history(history):
    op_counts = count_ops_in_history(history)
    output_history(history, op_counts)


def command_remove_history_entry(history):
    history_entry_id = int_input("Please enter a history entry id > ")
    history.remove(history_entry_id)


def command_clear(calc_history):
    calc_history.clear()


def command_unknown(_):
    print("unknown command, please try again")


def app():

    command_logger = Logger("command.log", log_name="Command")

    calc_history = CalcHistory()

    commands = {
        "history": command_output_history,
        "remove": command_remove_history_entry,
        "clear": command_clear,
    }

    while True:

        command_processed = False

        command = input("Please enter a command > ")

        if not command:
            break

        command_logger.log(command)

        for calc_op in calc_ops:
            if calc_op.command == command:
                command_math_op(calc_history, calc_op.func, calc_op.name)
                command_processed = True
                break

        if command_processed:
            continue

        command_func = commands.get(command, command_unknown)
        command_func(calc_history)


app()
