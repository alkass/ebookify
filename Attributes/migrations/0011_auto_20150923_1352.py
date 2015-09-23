# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0010_bookfeedback_feedback_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookfeedback',
            name='discoverable',
            field=models.BooleanField(default=True, help_text=b'Make this comment visible in the book view page'),
        ),
    ]
