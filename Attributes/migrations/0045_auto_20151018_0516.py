# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0044_book_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category1',
        ),
        migrations.RemoveField(
            model_name='book',
            name='category10',
        ),
        migrations.RemoveField(
            model_name='book',
            name='category2',
        ),
        migrations.RemoveField(
            model_name='book',
            name='category3',
        ),
        migrations.RemoveField(
            model_name='book',
            name='category4',
        ),
        migrations.RemoveField(
            model_name='book',
            name='category5',
        ),
        migrations.RemoveField(
            model_name='book',
            name='category6',
        ),
        migrations.RemoveField(
            model_name='book',
            name='category7',
        ),
        migrations.RemoveField(
            model_name='book',
            name='category8',
        ),
        migrations.RemoveField(
            model_name='book',
            name='category9',
        ),
    ]
