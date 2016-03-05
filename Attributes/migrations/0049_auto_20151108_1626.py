# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0048_auto_20151108_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='contributors',
            field=models.ManyToManyField(to='Attributes.Contributor', blank=True),
        ),
    ]
