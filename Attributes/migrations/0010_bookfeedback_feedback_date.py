# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0009_auto_20150923_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookfeedback',
            name='feedback_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 23, 15, 47, 28, 782000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
