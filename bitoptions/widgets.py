from django import forms

from .utils import number2powers


class BinaryWidget(forms.CheckboxSelectMultiple):
    def value_from_datadict(self, data, files, name):
        return sum(map(int, super(BinaryWidget, self).value_from_datadict(
            data, files, name)))

    def render(self, name, value, attrs=None, choices=()):
        if value and isinstance(value, int):
            value = number2powers(value)
        return super(BinaryWidget, self).render(name, value, attrs, choices)
