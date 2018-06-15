from django import forms

from .utils import number2powers, BitOptions


class BitOptionsWidget(forms.CheckboxSelectMultiple):
    """
    Default BitOptionsField widget to present every option (bit) as checkbox.
    """

    def value_from_datadict(self, data, files, name):
        """
        Given a dictionary of data and this widget's name, returns the value of
        this widget.
        """
        return sum(map(int, super(BitOptionsWidget, self).value_from_datadict(
            data, files, name)))

    def render(self, name, value, attrs=None, renderer=None):
        """
        Returns HTML for the widget, as a Unicode string.
        """
        if isinstance(value, BitOptions):
            value = list(number2powers(value.value))
        elif isinstance(value, int):
            value = list(number2powers(value))
        try:
            return super(BitOptionsWidget, self).render(name, value,
                                                        attrs, renderer)
        except TypeError:
            return super(BitOptionsWidget, self).render(name, value, attrs)
