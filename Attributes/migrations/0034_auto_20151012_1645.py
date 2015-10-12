# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0033_auto_20151012_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookfeedback',
            name='d',
        ),
        migrations.AddField(
            model_name='book',
            name='cats',
            field=models.ManyToManyField(to='Attributes.Category'),
        ),
    ]
