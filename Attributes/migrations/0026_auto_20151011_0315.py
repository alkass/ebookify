# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0025_auto_20151011_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to=b'/home/fadi/Projects/ebookify/database/6dad9f6e-169b-4291-86a8-53c80ad8bc74', blank=True),
        ),
    ]
