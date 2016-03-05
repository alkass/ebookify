# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0022_auto_20151004_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to=b'C:\\Users\\hannaafh\\Desktop\\eb\\database', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='file1',
            field=models.FileField(upload_to=b'C:\\Users\\hannaafh\\Desktop\\eb\\database'),
        ),
        migrations.AlterField(
            model_name='book',
            name='file2',
            field=models.FileField(null=True, upload_to=b'C:\\Users\\hannaafh\\Desktop\\eb\\database', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='file3',
            field=models.FileField(null=True, upload_to=b'C:\\Users\\hannaafh\\Desktop\\eb\\database', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='recommended',
            field=models.BooleanField(default=False, help_text=b'Recommend this book to your library visitors'),
        ),
    ]
