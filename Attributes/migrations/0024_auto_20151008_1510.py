# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0023_auto_20151005_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to=b'C:\\Users\\hannaafh\\Desktop\\ebookify\\database', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=5000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='file1',
            field=models.FileField(upload_to=b'C:\\Users\\hannaafh\\Desktop\\ebookify\\database'),
        ),
        migrations.AlterField(
            model_name='book',
            name='file2',
            field=models.FileField(null=True, upload_to=b'C:\\Users\\hannaafh\\Desktop\\ebookify\\database', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='file3',
            field=models.FileField(null=True, upload_to=b'C:\\Users\\hannaafh\\Desktop\\ebookify\\database', blank=True),
        ),
    ]
