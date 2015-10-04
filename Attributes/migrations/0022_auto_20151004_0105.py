# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0021_auto_20150926_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='num_pages',
            field=models.IntegerField(default=0, help_text=b"Leave at 0 if you don't want the number of pages to be shown", verbose_name=b'number of Pages'),
        ),
    ]
