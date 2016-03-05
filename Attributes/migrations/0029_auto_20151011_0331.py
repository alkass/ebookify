# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0028_auto_20151011_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to=b'/home/fadi/Projects/ebookify/database/398a23f4-b389-4b48-9a7c-5c23ecbfb175', blank=True),
        ),
    ]
