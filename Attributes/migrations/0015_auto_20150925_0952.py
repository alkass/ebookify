# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0014_auto_20150923_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='recommended',
            field=models.BooleanField(default=True, help_text=b'Recommend this book to your library visitors'),
        ),
        migrations.AlterField(
            model_name='book',
            name='file1',
            field=models.FileField(upload_to=b'C:\\Users\\hannaafh\\Desktop\\ebookify_\\database'),
        ),
    ]
