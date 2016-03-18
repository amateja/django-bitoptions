def number2powers(n):
    """
    Converts an integer value to list of powers of 2.
    :param n: integer value to convert
    :type n: int
    :return: list of powers of 2
    """
    x = bin(n)[2:]
    i = len(x)
    result = []
    for c in map(int, x):
        i -= 1
        if c:
            result.append(1 << i)
    return result


class BitOptions(object):
    """
    Stores a list of options with theirs weights as a powers of 2.
    """
    def __init__(self, options, value=None):
        self.flags = options
        self._options = []
        self._lookup = None
        for index, val in enumerate(self.flags):
            self._options.append((1 << index, val))
        if value is None:
            self.value = self.maximum_value
        else:
            self.value = int(value) & self.maximum_value

    def __iter__(self):
        return iter(self._options)

    def __len__(self):
        return len(self._options)

    def get_selected_values(self, selection=None):
        """
        Returns a list of options for the given selection.
        :param selection: a number to be converted to a list of options
        :type selection: int
        """
        if selection is None:
            selection = self.value
        return [v for b, v in self._options if b & selection]

    def _initialize_lookup(self):
        """
        Initializes self._lookup dict only if needed to let self.flags be
        a list of translatable strings.
        """
        self._lookup = {}
        for index, val in enumerate(self.flags):
            self._lookup[val] = 1 << index

    def get_value(self, vector):
        """
        Converts a list of options to sum of theirs weights.
        :param vector: list of options
        :type vector: iterable
        :return: int as a sum of weights of given options' list
        """
        if self._lookup is None:
            self._initialize_lookup()
        return sum([self._lookup.get(i, 0) for i in set(vector)])

    def set_value(self, vector):
        """
        Sets a value basing on given list of options.
        :param vector: list of options
        :type vector: iterable
        """
        self.value = self.get_value(vector)

    @property
    def maximum_value(self):
        """
        Returns maximal value which is when all options are set.
        """
        return (1 << len(self)) - 1
