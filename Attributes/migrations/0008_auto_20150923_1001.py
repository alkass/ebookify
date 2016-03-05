# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0007_auto_20150923_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file1',
            field=models.FileField(default=datetime.datetime(2015, 9, 23, 14, 1, 25, 13000, tzinfo=utc), upload_to=b'C:\\Users\\hannaafh\\Desktop\\project\\database'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='discoverable',
            field=models.BooleanField(default=True, help_text=b'If checked off, all books associated with this author will be discoverable to clients'),
        ),
        migrations.AlterField(
            model_name='book',
            name='discoverable',
            field=models.BooleanField(default=True, help_text=b'Make this book discoverable to view and download'),
        ),
        migrations.AlterField(
            model_name='bookfeedback',
            name='discoverable',
            field=models.BooleanField(default=False, help_text=b'Make this comment visible in the book view page'),
        ),
        migrations.AlterField(
            model_name='category',
            name='discoverable',
            field=models.BooleanField(default=True, help_text=b'If checked off, all books associated with this category will be discoverable to clients'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='discoverable',
            field=models.BooleanField(default=True, help_text=b'If checked off, all books associated with this contributor will be discoverable to clients'),
        ),
        migrations.AlterField(
            model_name='language',
            name='discoverable',
            field=models.BooleanField(default=True, help_text=b'If checked off, all books associated with this language will be discoverable to clients'),
        ),
    ]
