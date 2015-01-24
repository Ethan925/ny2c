# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ny2c_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='crust',
            field=models.CharField(default=b'New York', max_length=8, choices=[(b'New York', b'New York'), (b'CH', b'Chicago'), (b'BR', b'Bravo'), (b'SC', b'Sicilian')]),
            preserve_default=True,
        ),
    ]
