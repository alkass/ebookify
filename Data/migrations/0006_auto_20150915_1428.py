# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0005_auto_20150915_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author2',
            field=models.ForeignKey(related_name='author2', blank=True, to='Attributes.Author', null=True),
        ),
    ]
