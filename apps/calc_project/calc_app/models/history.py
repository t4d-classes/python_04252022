
class HistoryEntry:

    def __init__(self, op_name, op_value, math_op, entry_id=-1):
        self.entry_id = entry_id
        self.op_name = op_name
        self.op_value = op_value
        self.math_op = math_op


class CalcHistory:

    def __init__(self):
        # protected - no public access, it should only be accessed
        # from within the class itself, or within a subclass
        self._history_entries = []
        self._history_entries_iter = None

    def append(self, history_entry):
        history_entry.entry_id = self.get_next_id()
        self._history_entries.append(history_entry)

    def remove(self, history_entry_id):
        for history_entry in self._history_entries:
            if history_entry.entry_id == history_entry_id:
                self._history_entries.remove(history_entry)

    def clear(self):
        self._history_entries = []

    def get_next_id(self):
        return max(
            [entry.entry_id for entry in self._history_entries] or [0]) + 1

    def __iter__(self):
        self._history_entries_iter = iter(self._history_entries)
        return self

    def __next__(self):
        return next(self._history_entries_iter)

    def __len__(self):
        return len(self._history_entries)
