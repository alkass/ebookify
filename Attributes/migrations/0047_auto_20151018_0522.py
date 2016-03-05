# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0046_book_contributors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author1',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author2',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author3',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author4',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author5',
        ),
        migrations.RemoveField(
            model_name='book',
            name='contributor1',
        ),
        migrations.RemoveField(
            model_name='book',
            name='contributor2',
        ),
        migrations.RemoveField(
            model_name='book',
            name='contributor3',
        ),
    ]
