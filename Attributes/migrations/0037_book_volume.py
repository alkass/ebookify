# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0036_auto_20151018_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='volume',
            field=models.IntegerField(default=1, choices=[(1, 1), (2, 2)]),
            preserve_default=False,
        ),
    ]
