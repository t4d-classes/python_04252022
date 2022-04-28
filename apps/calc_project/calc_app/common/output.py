def output_result(result):
    print(f"Result: {result}")


def output_history(history, op_counts):

    for history_entry in history:
        print(history_entry)

    print(f"Add Count: {op_counts.get('add', 0)}")
    print(f"Subtract Count: {op_counts.get('subtract', 0)}")
    print(f"Multiply Count: {op_counts.get('multiply', 0)}")
    print(f"Divide Count: {op_counts.get('divide', 0)}")
