from django import forms

from .widgets import BitOptionsWidget


class BitOptionsForm(forms.IntegerField):
    """
    Default form for BitOptionsField.
    """
    widget = BitOptionsWidget

    def __init__(self, options, *args, **kwargs):
        if self.widget == BitOptionsWidget:
            kwargs.setdefault('widget', BitOptionsWidget(choices=options))
        super(BitOptionsForm, self).__init__(*args, **kwargs)
