# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ny2c_app', '0002_auto_20150124_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.CharField(default=b'Pepperoni', max_length=8, choices=[(b'Pepperoni', b'Pepperoni'), (b'Sausage', b'Sausage'), (b'Onion', b'Onion')]),
            preserve_default=True,
        ),
    ]
