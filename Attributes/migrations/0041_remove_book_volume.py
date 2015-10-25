# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0040_auto_20151018_0326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='volume',
        ),
    ]
