
class HistoryEntry:

    def __init__(self, op_name, op_value, math_op, entry_id=-1):
        self.entry_id = entry_id
        self.op_name = op_name
        self.op_value = op_value
        self.math_op = math_op


class CalcHistory:

    def __init__(self):
        self.history_entries = []

    def append(self, history_entry):
        history_entry.entry_id = self.get_next_id()
        self.history_entries.append(history_entry)

    def remove(self, history_entry_id):
        for history_entry in self.history_entries:
            if history_entry.entry_id == history_entry_id:
                self.history_entries.remove(history_entry)

    def clear(self):
        self.history_entries = []

    def get_entries(self):
        return self.history_entries

    # def get_next_id(self, history):
    #     return max(list(
    #         map(lambda entry: entry.entry_id, history) or [0]
    #     )) + 1

    def get_next_id(self):
        return max(
            [entry.entry_id for entry in self.history_entries] or [0]) + 1
