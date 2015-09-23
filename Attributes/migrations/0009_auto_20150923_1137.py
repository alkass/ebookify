# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0008_auto_20150923_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.ForeignKey(to='Attributes.Language', null=True),
        ),
    ]
