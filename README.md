[![Travis](https://img.shields.io/travis/amateja/django-bitoptions.svg)]
(https://travis-ci.org/amateja/django-bitoptions)
[![Coveralls](https://img.shields.io/coveralls/amateja/django-bitoptions.svg)]
(https://coveralls.io/github/amateja/django-bitoptions)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/9d2810191a234414a3edf7843f5d1c1c/badge.svg)]
(https://www.quantifiedcode.com/app/project/9d2810191a234414a3edf7843f5d1c1c)

# django-bitoptions
This project replaces several related BooleanFields with a single field and
a few eye candy features.

## installation

    $ pip install django-bitoptions

## usage

```python
from django.db import models
from bitoptions import BitOptions, BitOptionsField

TOPPINGS = BitOptions(
    ('pepperoni', 'mushrooms', 'onions', 'sausage', 'bacon', 'black olives',
     'green olives', 'green peppers', 'pineapple', 'spinach', 'tomatoes',
     'broccoli', 'jalapeno peppers', 'anchovies', 'chicken', 'beef', 'ham',
     'salami')
)
CHEESES = BitOptions(('feta', 'parmesan', 'provolone', 'goat', 'mozzarella'))


class Pizza(models.Model):
    toppings = BitOptionsField(options=TOPPINGS)
    cheeses = BitOptionsField(options=CHEESES)
```
