# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0012_book_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='subtitle',
            field=models.CharField(max_length=256, unique=True, null=True, blank=True),
        ),
    ]
