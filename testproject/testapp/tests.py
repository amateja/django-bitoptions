from django.http import QueryDict
from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from django.contrib.admin.options import ModelAdmin
from bitoptions import BitOptions, BitOptionsField, BinaryWidget
from bitoptions.utils import number2powers

from .models import TOPPINGS, Box, Pizza


class MockRequest(object):
    pass


class MockSuperUser(object):
    def has_perm(self, perm):
        return True


request = MockRequest()
request.user = MockSuperUser()


class ModelAdminTests(TestCase):
    def test_default_fields(self):
        ma = ModelAdmin(Pizza, AdminSite)
        self.assertEqual(
            list(ma.get_form(request).base_fields), ['toppings', 'cheeses'])
        self.assertEqual(
            list(ma.get_fields(request)), ['toppings', 'cheeses'])
        self.assertEqual(ma.get_fields(request), ['toppings', 'cheeses'])

    def test_xxl(self):
        self.assertRaises(ValueError, BitOptionsField, options=range(0, 99))

    def test_bitoptions_empty(self):
        self.assertEqual(BitOptions(()).max, 0)

    def test_bitoptions_value(self):
        self.assertEqual(BitOptions(('a', 'b', 'c', 'd'), 42).value, 10)

    def test_bitoptions_get_selected_values(self):
        options = ['a', 'b', 'c', 'd']
        self.assertEqual(BitOptions(options).get_selected_values(), options)

    def test_bitoptions_set_value(self):
        options = BitOptions(('a', 'b', 'c', 'd'))
        options.set_value(('a', 'd'))
        self.assertEqual(options.value, 9)

    def test_numer2powers(self):
        self.assertEqual(number2powers(127), [64, 32, 16, 8, 4, 2, 1])

    def test_get_selected_values(self):
        self.assertEqual(TOPPINGS.get_selected_values(131140),
                         ['onions', 'green olives', 'salami'])

    def test_get_value(self):
        self.assertEqual(
            TOPPINGS.get_value(['onions', 'green olives', 'salami']), 131140)

    def test_large(self):
        field = BitOptionsField(options=range(0, 40), null=True)
        self.assertEqual('BigIntegerField', field.get_internal_type())

    def test_widget_render(self):
        widget = BinaryWidget()
        widget.options = TOPPINGS
        html = widget.render('toppings', 131140, {'id': 'id_toppings'},
                             TOPPINGS)
        self.assertEqual(html.count('<li>'), len(TOPPINGS))
        self.assertEqual(html.count('checked="checked"'),
                         len(TOPPINGS.get_selected_values(131140)))

    def test_widget_value_from_datadict(self):
        qd = '_save=Save&cheeses=1&cheeses=16&toppings=1&toppings=131072'
        widget = BinaryWidget()
        self.assertEqual(
            widget.value_from_datadict(QueryDict(qd), {}, 'cheeses'), 17)

    def test_lookup(self):
        toppings = BitOptions(TOPPINGS.flags, 10)
        p = Pizza.objects.create(toppings=30, cheeses=18)
        Pizza.objects.create(toppings=20, cheeses=18)
        self.assertEqual(Pizza.objects.get(toppings__bitwise_and=toppings).id, p.id)

    def test_null(self):
        Box.objects.create(colors=None)
        b = Box.objects.get()
        self.assertIsNone(b.colors)
