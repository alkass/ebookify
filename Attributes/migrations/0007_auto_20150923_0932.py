# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0006_auto_20150922_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookfeedback',
            old_name='deprecated',
            new_name='discoverable',
        ),
        migrations.RemoveField(
            model_name='author',
            name='deprecated',
        ),
        migrations.RemoveField(
            model_name='book',
            name='deprecated',
        ),
        migrations.RemoveField(
            model_name='category',
            name='deprecated',
        ),
        migrations.RemoveField(
            model_name='contributor',
            name='deprecated',
        ),
        migrations.RemoveField(
            model_name='language',
            name='deprecated',
        ),
        migrations.AddField(
            model_name='author',
            name='discoverable',
            field=models.BooleanField(default=True, help_text=b'If checked off, all books associated with this author will NOT be discoverable to clients'),
        ),
        migrations.AddField(
            model_name='book',
            name='discoverable',
            field=models.BooleanField(default=True, help_text=b'If checked off, this book will NOT be discoverable to clients'),
        ),
        migrations.AddField(
            model_name='category',
            name='discoverable',
            field=models.BooleanField(default=True, help_text=b'If checked off, all books associated with this category will NOT be discoverable to clients'),
        ),
        migrations.AddField(
            model_name='contributor',
            name='discoverable',
            field=models.BooleanField(default=True, help_text=b'If checked off, all books associated with this contributor will NOT be discoverable to clients'),
        ),
        migrations.AddField(
            model_name='language',
            name='discoverable',
            field=models.BooleanField(default=True, help_text=b'If checked off, all books associated with this language will NOT be discoverable to clients'),
        ),
        migrations.AlterField(
            model_name='book',
            name='num_downloads',
            field=models.IntegerField(default=0, verbose_name=b'Downloads'),
        ),
        migrations.AlterField(
            model_name='book',
            name='num_views',
            field=models.IntegerField(default=0, verbose_name=b'Views'),
        ),
    ]
