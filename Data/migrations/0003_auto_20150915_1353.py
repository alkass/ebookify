# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0001_initial'),
        ('Data', '0002_auto_20150915_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='contributor',
        ),
        migrations.AddField(
            model_name='book',
            name='author3',
            field=models.ForeignKey(related_name='author3', blank=True, to='Attributes.Author', null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='author4',
            field=models.ForeignKey(related_name='author4', blank=True, to='Attributes.Author', null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='author5',
            field=models.ForeignKey(related_name='author5', blank=True, to='Attributes.Author', null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='contributor1',
            field=models.ForeignKey(related_name='contributor1', blank=True, to='Attributes.Contributor', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author2',
            field=models.ForeignKey(related_name='author2', blank=True, to='Attributes.Author', null=True),
        ),
    ]
