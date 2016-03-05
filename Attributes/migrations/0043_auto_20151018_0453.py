# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0042_book_all_authors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='all_authors',
            new_name='authors',
        ),
    ]
