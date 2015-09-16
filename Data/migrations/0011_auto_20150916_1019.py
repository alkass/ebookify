# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0001_initial'),
        ('Data', '0010_auto_20150916_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category10',
            field=models.ForeignKey(related_name='category10', blank=True, to='Attributes.Category', null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='category3',
            field=models.ForeignKey(related_name='category3', blank=True, to='Attributes.Category', null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='category4',
            field=models.ForeignKey(related_name='category4', blank=True, to='Attributes.Category', null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='category5',
            field=models.ForeignKey(related_name='category5', blank=True, to='Attributes.Category', null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='category6',
            field=models.ForeignKey(related_name='category6', blank=True, to='Attributes.Category', null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='category7',
            field=models.ForeignKey(related_name='category7', blank=True, to='Attributes.Category', null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='category8',
            field=models.ForeignKey(related_name='category8', blank=True, to='Attributes.Category', null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='category9',
            field=models.ForeignKey(related_name='category9', blank=True, to='Attributes.Category', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='category1',
            field=models.ForeignKey(related_name='category1', to='Attributes.Category', null=True),
        ),
    ]
