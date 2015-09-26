# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0017_auto_20150926_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file2',
            field=models.FileField(default=datetime.datetime(2015, 9, 26, 16, 21, 4, 839872, tzinfo=utc), upload_to=b'/home/fadi/Projects/ebookify/database'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='file3',
            field=models.FileField(default=datetime.datetime(2015, 9, 26, 16, 21, 16, 720327, tzinfo=utc), upload_to=b'/home/fadi/Projects/ebookify/database'),
            preserve_default=False,
        ),
    ]
