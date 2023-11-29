from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import AdminSite
from django.forms import IntegerField
from django.http import QueryDict
from django.test import TestCase

from bitoptions import BitOptions, BitOptionsField, BitOptionsWidget
from bitoptions.utils import number2powers
from .models import TOPPINGS, Box, Pizza


class MockRequest(object):
    """
    Empty class to mimic a HTTP request.
    """
    pass


class MockSuperUser(object):
    """
    Mimics super user.
    """

    @staticmethod
    def has_perm(*args, **kwargs):
        """
        Super user has every permission.
        """
        return True


request = MockRequest()
request.user = MockSuperUser()


class BitOptionFieldTests(TestCase):
    """
    Contains functional and coverage tests.
    """

    def test_default_fields(self):
        """
        Tests widget.
        """
        ma = ModelAdmin(Pizza, AdminSite)
        self.assertEqual(
            list(ma.get_form(request).base_fields), ['toppings', 'cheeses'])
        self.assertEqual(
            list(ma.get_fields(request)), ['toppings', 'cheeses'])
        self.assertEqual(ma.get_fields(request), ['toppings', 'cheeses'])

    def test_overridden_form_class(self):
        """
        Tests type of form returned by BitOptionsField.formfield when default
        form_class parameter is overridden.
        """
        f = BitOptionsField()
        form = f.formfield(form_class=IntegerField)
        self.assertTrue(isinstance(form, IntegerField))

    def test_xxl(self):
        """
        Tests oversize list of options.
        """
        self.assertRaises(ValueError, BitOptionsField, options=range(0, 99))

    def test_bitoptions_empty(self):
        """
        Tests empty list of options.
        """
        self.assertEqual(BitOptions(()).maximum_value, 0)

    def test_bitoptions_value(self):
        """
        Tests BitOptions object creation with given initial value.
        """
        self.assertEqual(BitOptions(('a', 'b', 'c', 'd'), 42).value, 10)

    def test_bitoptions_get_selected_values_no_param(self):
        """
        Tests BitOptions.get_selected_values method with no given parameter.
        """
        options = ['a', 'b', 'c', 'd']
        self.assertEqual(BitOptions(options).get_selected_values(), options)

    def test_bitoptions_set_value(self):
        """
        Tests BitOptions.set_value method.
        """
        options = BitOptions(('a', 'b', 'c', 'd'))
        options.set_value(('a', 'd'))
        self.assertEqual(options.value, 9)

    def test_number2powers(self):
        """
        Tests number2powers function.
        """
        self.assertEqual(sum(number2powers(127)), 127)

    def test_bitoptions_get_selected_values(self):
        """
        Tests BitOptions.get_selected_values method.
        """
        self.assertEqual(TOPPINGS.get_selected_values(131140),
                         ['onions', 'green olives', 'salami'])

    def test_get_value(self):
        """
        Tests BitOptions.get_value method.
        """
        self.assertEqual(
            TOPPINGS.get_value(['onions', 'green olives', 'salami']), 131140)

    def test_large(self):
        """
        Tests BitOptionsField.get_internal_type method for a large options
        list.
        """
        field = BitOptionsField(options=range(0, 40), null=True)
        self.assertEqual('BigIntegerField', field.get_internal_type())

    def test_widget_render_int(self):
        """
        Tests BitOptionsWidget.render method with integer value.
        """
        widget = BitOptionsWidget(choices=TOPPINGS)
        html = widget.render('toppings', 131140, {'id': 'id_toppings'})
        self.assertEqual(html.count('<input '), len(TOPPINGS))
        self.assertEqual(html.count(' checked'),
                         len(TOPPINGS.get_selected_values(131140)))

    def test_widget_render_bitoptions(self):
        """
        Tests BitOptionsWidget.render method with BitOptions object.
        """
        TOPPINGS.value = 131140
        widget = BitOptionsWidget(choices=TOPPINGS)
        html = widget.render('toppings', TOPPINGS, {'id': 'id_toppings'})
        self.assertEqual(html.count('<input '), len(TOPPINGS))
        self.assertEqual(html.count(' checked'),
                         len(TOPPINGS.get_selected_values(131140)))

    def test_widget_value_from_datadict(self):
        """
        Tests BitOptionsWidget.value_from_datadict method.
        """
        qd = '_save=Save&cheeses=1&cheeses=16&toppings=1&toppings=131072'
        widget = BitOptionsWidget()
        self.assertEqual(
            widget.value_from_datadict(QueryDict(qd), {}, 'cheeses'), 17)

    def test_lookup(self):
        """
        Tests BitwiseAnd lookup.
        """
        toppings = BitOptions(TOPPINGS.flags, 10)
        p = Pizza.objects.create(toppings=30, cheeses=18)
        Pizza.objects.create(toppings=20, cheeses=18)
        self.assertEqual(Pizza.objects.get(toppings__bitwise_and=toppings).id,
                         p.id)

    def test_null(self):
        """
        Tests nullable BitOptionsField.
        """
        Box.objects.create(colors=None)
        b = Box.objects.get()
        self.assertIsNone(b.colors)
