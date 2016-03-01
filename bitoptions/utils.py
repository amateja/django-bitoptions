def number2powers(n):
    x = bin(n)[2:]
    i = len(x)
    result = []
    for c in map(int, x):
        i -= 1
        if c:
            try:
                result.append(2 << i - 1)
            except ValueError:
                result.append(1)
    return result


class BitOptions(object):
    def __init__(self, options, value=None):
        self.flags = tuple(map(str, options))
        self._options = []
        self._lookup = {}
        for index, val in enumerate(self.flags):
            try:
                index = 2 << index - 1
            except ValueError:
                index = 1
            self._options.append((index, val))
            self._lookup[val] = index
        if value is None:
            self.value = self.max
        else:
            self.value = int(value) & self.max

    def __iter__(self):
        return iter(self._options)

    def __len__(self):
        return len(self._options)

    def get_selected_values(self, selection=None):
        """ Return a list of values for the given selection """
        if selection is None:
            selection = self.value
        return [v for b, v in self._options if b & selection]

    def get_value(self, vector):
        return sum([self._lookup.get(i, 0) for i in set(vector)])

    def set_value(self, vector):
        self.value = self.get_value(vector)

    @property
    def max(self):
        try:
            return (2 << len(self) - 1) - 1
        except ValueError:
            return 0
