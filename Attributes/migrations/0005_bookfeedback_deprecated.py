# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0004_bookfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookfeedback',
            name='deprecated',
            field=models.BooleanField(default=False, help_text=b'If checked off, this comment will be hidden from the book list of reviews'),
        ),
    ]
