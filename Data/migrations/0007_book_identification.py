# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0006_auto_20150915_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='identification',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
    ]
