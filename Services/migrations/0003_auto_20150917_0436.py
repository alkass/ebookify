# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0002_auto_20150917_0429'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PlaceBookRequest',
            new_name='BookRequest',
        ),
        migrations.AlterModelOptions(
            name='bookrequest',
            options={'verbose_name': 'Book Request', 'verbose_name_plural': 'Book Requests'},
        ),
    ]
