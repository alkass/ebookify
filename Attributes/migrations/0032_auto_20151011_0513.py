# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0031_auto_20151011_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to=b'/Users/fadihannaal-kass/Desktop/ebookify/database/covers', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='file1',
            field=models.FileField(upload_to=b'/Users/fadihannaal-kass/Desktop/ebookify/database/books'),
        ),
        migrations.AlterField(
            model_name='book',
            name='file2',
            field=models.FileField(null=True, upload_to=b'/Users/fadihannaal-kass/Desktop/ebookify/database/books', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='file3',
            field=models.FileField(null=True, upload_to=b'/Users/fadihannaal-kass/Desktop/ebookify/database/books', blank=True),
        ),
    ]
