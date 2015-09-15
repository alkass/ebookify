# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0001_initial'),
        ('Data', '0003_auto_20150915_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='contributor2',
            field=models.ForeignKey(related_name='contributor2', blank=True, to='Attributes.Contributor', null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='contributor3',
            field=models.ForeignKey(related_name='contributor3', blank=True, to='Attributes.Contributor', null=True),
        ),
    ]
