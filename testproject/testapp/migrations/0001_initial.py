# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import bitoptions.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True,
                    primary_key=True)
                 ),
                ('toppings', bitoptions.fields.SimpleBitOptionsField(
                    options=('pepperoni', 'mushrooms', 'onions', 'sausage',
                             'bacon', 'black olives', 'green olives',
                             'green peppers', 'pineapple', 'spinach',
                             'tomatoes', 'broccoli', 'jalapeno peppers',
                             'anchovies', 'chicken', 'beef', 'ham', 'salami'))
                 ),
                ('cheeses', bitoptions.fields.SimpleBitOptionsField(
                    options=('feta', 'parmesan', 'provolone', 'goat',
                             'mozzarella'))
                 ),
            ],
        ),
    ]
