from django.db.models import IntegerField
from django.utils.translation import ugettext_lazy as _

from .lookups import BitwiseAnd
from .utils import BitOptions
from .forms import BitOptionsForm


class SimpleBitOptionsField(IntegerField):
    """
    Simple version of BitOptionsField class. Only necessary element are
    included. Value is represented by an integer object instance.
    """
    description = _('Bit options')

    def __init__(self, options=(), *args, **kwargs):
        if isinstance(options, BitOptions):
            self.options = options
        else:
            self.options = BitOptions(options)

        _len = len(self.options)
        if _len < 16:
            self._internal_type = 'PositiveSmallIntegerField'
        elif _len < 32:
            self._internal_type = 'PositiveIntegerField'
        elif _len < 64:
            self._internal_type = 'BigIntegerField'
        else:
            raise ValueError('Options list is longer than 63 items.')
        kwargs.setdefault('default', self.options.maximum_value)
        super(SimpleBitOptionsField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        """
        Returns a string naming this field for backend specific purposes.
        """
        return self._internal_type

    def formfield(self, **kwargs):
        """
        Returns the default BitOptionForm of this field for ModelForm.
        """
        form_class = kwargs.get('form_class', BitOptionsForm)
        if issubclass(form_class, BitOptionsForm):
            defaults = {
                'form_class': form_class,
                'min_value': 0,
                'max_value': self.options.maximum_value,
                'options': list(self.options)
            }
            kwargs.pop('widget', None)
        else:
            defaults = {}
        defaults.update(kwargs)
        return super(SimpleBitOptionsField, self).formfield(**defaults)

    def deconstruct(self):
        """
        Defines how to reduce field instance to a serialized form.
        """
        name, path, args, kwargs = super(SimpleBitOptionsField,
                                         self).deconstruct()
        if kwargs['default'] == self.options.maximum_value:
            del kwargs['default']
        kwargs['options'] = self.options.flags
        return name, path, args, kwargs


class BitOptionsField(SimpleBitOptionsField):
    """
    Expanded version of SimpleBitOptionsField. Value is represented by
    a BitOptions object instance.
    """

    def from_db_value(self, value, *args, **kwargs):
        """
        Converts a value as returned by the database to a Python object.
        """
        return self.to_python(value)

    def to_python(self, value):
        """
        Converts the value into the correct Python object.
        """
        if value is None:
            return value
        value = super(BitOptionsField, self).to_python(value)
        return BitOptions(self.options.flags, value)

    def get_prep_value(self, value):
        """
        Takes current value of the model's attribute, and the method returns
        data in a format that has been prepared for use as a parameter in
        a query.
        """
        if isinstance(value, BitOptions):
            return super(BitOptionsField, self).get_prep_value(value.value)
        return super(BitOptionsField, self).get_prep_value(value)

    def get_prep_lookup(self, lookup_type, value):
        """
        Prepares value to the database prior to be used in a lookup.
        """
        value = self.get_prep_value(value)
        return super(BitOptionsField, self).get_prep_lookup(lookup_type, value)


SimpleBitOptionsField.register_lookup(BitwiseAnd)
