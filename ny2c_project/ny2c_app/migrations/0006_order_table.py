# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ny2c_app', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.CharField(default=b'counter', max_length=50),
            preserve_default=True,
        ),
    ]
