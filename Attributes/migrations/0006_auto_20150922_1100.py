# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0005_bookfeedback_deprecated'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='num_downloads',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='num_views',
            field=models.IntegerField(default=0),
        ),
    ]
