# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0001_initial'),
        ('Data', '0009_auto_20150916_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.AddField(
            model_name='book',
            name='category1',
            field=models.ForeignKey(related_name='category1', blank=True, to='Attributes.Category', null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='category2',
            field=models.ForeignKey(related_name='category2', blank=True, to='Attributes.Category', null=True),
        ),
    ]
