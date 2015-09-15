# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author1',
            field=models.ForeignKey(related_name='author1', to='Attributes.Author', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author2',
            field=models.ForeignKey(related_name='author2', to='Attributes.Author', null=True),
        ),
    ]
