# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0011_auto_20150916_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='deprecated',
            field=models.BooleanField(default=False, help_text=b'If checked off, this book will NOT be discoverable to clients'),
        ),
        migrations.AlterField(
            model_name='book',
            name='identification',
            field=models.UUIDField(default=uuid.uuid4, null=True, verbose_name=b'Book ID'),
        ),
    ]
