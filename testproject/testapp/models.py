from django.db import models
from bitoptions import BitOptions, BitOptionsField

TOPPINGS = BitOptions(
    ('pepperoni', 'mushrooms', 'onions', 'sausage', 'bacon', 'black olives',
     'green olives', 'green peppers', 'pineapple', 'spinach', 'tomatoes',
     'broccoli', 'jalapeno peppers', 'anchovies', 'chicken', 'beef', 'ham',
     'salami')
)
CHEESES = BitOptions(('feta', 'parmesan', 'provolone', 'goat', 'mozzarella'))
COLORS = BitOptions(('red', 'green', 'blue'))


class Box(models.Model):
    """
    Test model with nullable BitOptionsField.
    """
    colors = BitOptionsField(options=COLORS, null=True, blank=True)


class Pizza(models.Model):
    """
    Test model with small and medium size list of options.
    """
    toppings = BitOptionsField(options=TOPPINGS)
    cheeses = BitOptionsField(options=CHEESES)
