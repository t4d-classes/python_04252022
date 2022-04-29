from calc_app.models.calc import CalcOp

calc_ops = [
    CalcOp("add", "Add", lambda a, b: a + b),
    CalcOp("subtract", "Subtract", lambda a, b: a - b),
    CalcOp("multiply", "Multiply", lambda a, b: a * b),
    CalcOp("divide", "Divide", lambda a, b: a / b),
    CalcOp("power", "Power", lambda a, b: a ** b),
]


def calc_result(history):
    result = 0
    for history_entry in history:
        op_value = history_entry.op_value
        math_op = history_entry.math_op
        result = math_op(result, op_value)
    return result


def count_ops_in_history(history):
    """ counts the frequency of the different operations in the history """

    op_counts = {}

    for history_entry in history:
        op_name = history_entry.op_name
        op_counts[op_name] = op_counts.get(op_name, 0) + 1

    return op_counts
