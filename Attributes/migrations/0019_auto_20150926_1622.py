# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0018_auto_20150926_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='file2',
            field=models.FileField(null=True, upload_to=b'/home/fadi/Projects/ebookify/database', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='file3',
            field=models.FileField(null=True, upload_to=b'/home/fadi/Projects/ebookify/database', blank=True),
        ),
    ]
