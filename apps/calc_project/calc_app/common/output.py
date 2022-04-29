from calc_app.common.calc_ops import calc_ops


def output_result(result):
    print(f"\nResult: {result}\n")


def output_history(history, op_counts):

    print()
    print("=" * 30)
    print("|  Id  |    Op    |  Value   |")
    print("-" * 30)
    for history_entry in history:
        print(
            "| " + str(history_entry.entry_id).rjust(4) + " | " +
            history_entry.op_name.ljust(8) + " | " +
            str(history_entry.op_value).rjust(8) + " |"

        )
    print("=" * 30)
    print()

    for calc_op in calc_ops:
        print(f"{calc_op.name} Count: {op_counts.get(calc_op.name, 0)}")

    print()
