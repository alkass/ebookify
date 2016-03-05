# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='deprecated',
            field=models.BooleanField(default=False, help_text=b'If checked off, all books associated with this author will NOT be discoverable to clients'),
        ),
        migrations.AlterField(
            model_name='category',
            name='deprecated',
            field=models.BooleanField(default=False, help_text=b'If checked off, all books associated with this category will NOT be discoverable to clients'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='deprecated',
            field=models.BooleanField(default=False, help_text=b'If checked off, all books associated with this contributor will NOT be discoverable to clients'),
        ),
        migrations.AlterField(
            model_name='language',
            name='deprecated',
            field=models.BooleanField(default=False, help_text=b'If checked off, all books associated with this language will NOT be discoverable to clients'),
        ),
    ]
