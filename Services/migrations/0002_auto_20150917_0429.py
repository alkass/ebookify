# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CheckBookRequestStatus',
        ),
        migrations.AddField(
            model_name='placebookrequest',
            name='request_id',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
    ]
