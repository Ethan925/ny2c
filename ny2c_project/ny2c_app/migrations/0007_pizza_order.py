# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ny2c_app', '0006_order_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='order',
            field=models.ForeignKey(default=1, to='ny2c_app.Order'),
            preserve_default=False,
        ),
    ]
