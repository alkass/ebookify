# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0041_remove_book_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='all_authors',
            field=models.ManyToManyField(to='Attributes.Author'),
        ),
    ]
