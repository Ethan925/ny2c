# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crust', models.CharField(default=b'NY', max_length=2, choices=[(b'NY', b'New York'), (b'CH', b'Chicago'), (b'BR', b'Bravo'), (b'SC', b'Sicilian')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
