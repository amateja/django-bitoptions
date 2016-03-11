# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import bitoptions.fields


class Migration(migrations.Migration):
    """
    Initial migration class.
    """

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(
                    primary_key=True,
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True)),
                ('colors', bitoptions.fields.BitOptionsField(
                    options=('red', 'green', 'blue'),
                    blank=True,
                    null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True,
                    primary_key=True)
                 ),
                ('toppings', bitoptions.fields.BitOptionsField(
                    options=('pepperoni', 'mushrooms', 'onions', 'sausage',
                             'bacon', 'black olives', 'green olives',
                             'green peppers', 'pineapple', 'spinach',
                             'tomatoes', 'broccoli', 'jalapeno peppers',
                             'anchovies', 'chicken', 'beef', 'ham', 'salami'))
                 ),
                ('cheeses', bitoptions.fields.BitOptionsField(
                    options=('feta', 'parmesan', 'provolone', 'goat',
                             'mozzarella'))
                 ),
            ],
        ),
    ]
