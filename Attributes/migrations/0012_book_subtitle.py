# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0011_auto_20150923_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='subtitle',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
    ]
