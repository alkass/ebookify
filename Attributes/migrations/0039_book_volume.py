# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0038_remove_book_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='volume',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'1st'), (2, b'2nd'), (3, b'3rd'), (4, b'4th'), (5, b'5th'), (6, b'6th'), (7, b'7th'), (8, b'8th'), (9, b'9th'), (10, b'10th')]),
        ),
    ]
