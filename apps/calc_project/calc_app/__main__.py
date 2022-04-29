import argparse
import re

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


def parse_command_split(command_input_str):

    command_input_parts = command_input_str.split(" ")

    command = command_input_parts[0]

    if len(command_input_parts) == 2:
        arg = command_input_parts[1]
    else:
        arg = None

    return (command, arg)


def parse_command(command_input_str):

    command_re = re.compile(
        r"(?P<command>[a-z]*)( (?P<arg>[0-9]*))?"
    )

    command_match = command_re.match(command_input_str)

    if not command_match:
        return ("", None)

    command_dict = command_match.groupdict()

    return (command_dict["command"], command_dict.get("arg", None))


def app_cli_args():

    parser = argparse.ArgumentParser(description="Command Line Calculator")

    parser.add_argument(
        "--command_log_file",
        type=str,
        help="command log file path",
        default="command.log"
    )

    return parser.parse_args()


def app():

    app_options = app_cli_args()

    command_logger = Logger(app_options.command_log_file, log_name="Command")

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

        command, arg = parse_command(user_input_str)

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
