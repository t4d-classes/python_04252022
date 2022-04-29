from calc_app.common.input import float_input, int_input
from calc_app.common.output import output_result, output_history
from calc_app.models.history import CalcHistory, HistoryEntry
from calc_app.common.logger import Logger
from calc_app.common.calc_ops import (
    calc_ops, count_ops_in_history, calc_result
)


def command_math_op(history, math_op, math_op_name, operand):
    history.append(HistoryEntry(math_op_name, operand, math_op))
    output_result(calc_result(history))


def command_output_history(history, *_):
    op_counts = count_ops_in_history(history)
    output_history(history, op_counts)


def command_remove_history_entry(history, *args):
    history_entry_id = int(args[0])
    history.remove(history_entry_id)


def command_clear(calc_history, *_):
    calc_history.clear()


def command_unknown(_1, *_2):
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

        # add 10
        # multiply 34.2
        # remove 3
        # clear
        # history
        user_input_str = input("Please enter a command > ")

        if not user_input_str:
            break

        user_input_parts = user_input_str.split(" ")

        command = user_input_parts[0]

        if len(user_input_parts) == 2:
            arg = user_input_parts[1]
        else:
            arg = None

        command_logger.log(command)

        for calc_op in calc_ops:
            if calc_op.command == command:
                command_math_op(
                    calc_history,
                    calc_op.func,
                    calc_op.name,
                    float(arg))
                command_processed = True
                break

        if command_processed:
            continue

        command_func = commands.get(command, command_unknown)
        command_func(calc_history, arg)


app()
