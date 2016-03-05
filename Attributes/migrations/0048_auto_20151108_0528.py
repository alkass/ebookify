# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0047_auto_20151018_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to=b'/home/fadi/Projects/_ebookify/database/covers', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='epub_file',
            field=models.FileField(upload_to=b'/home/fadi/Projects/_ebookify/database/books', null=True, verbose_name=b'EPUB File', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='mobi_file',
            field=models.FileField(upload_to=b'/home/fadi/Projects/_ebookify/database/books', null=True, verbose_name=b'MOBI File', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf_file',
            field=models.FileField(upload_to=b'/home/fadi/Projects/_ebookify/database/books', null=True, verbose_name=b'PDF File', blank=True),
        ),
    ]
