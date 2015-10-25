# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0039_book_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='volume',
            field=models.IntegerField(blank=True, null=True, choices=[(b'1st', 1), (b'2nd', 2), (b'3rd', 3), (b'4th', 4), (b'5th', 5), (b'6th', 6), (b'7th', 7), (b'8th', 8), (b'9th', 9), (b'10th', 10)]),
        ),
    ]
