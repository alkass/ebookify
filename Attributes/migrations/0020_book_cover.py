# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0019_auto_20150926_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(default=1, upload_to=b'/home/fadi/Projects/ebookify/database'),
            preserve_default=False,
        ),
    ]
