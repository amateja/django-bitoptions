from django.db import models
from bitoptions import BitOptions, SimpleBitOptionsField

TOPPINGS = BitOptions(
    ('pepperoni', 'mushrooms', 'onions', 'sausage', 'bacon', 'black olives',
     'green olives', 'green peppers', 'pineapple', 'spinach', 'tomatoes',
     'broccoli', 'jalapeno peppers', 'anchovies', 'chicken', 'beef', 'ham',
     'salami')
)
CHEESES = BitOptions(('feta', 'parmesan', 'provolone', 'goat', 'mozzarella'))


class Pizza(models.Model):
    toppings = SimpleBitOptionsField(options=TOPPINGS)
    cheeses = SimpleBitOptionsField(options=CHEESES)
