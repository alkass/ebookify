# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0045_auto_20151018_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='contributors',
            field=models.ManyToManyField(to='Attributes.Contributor'),
        ),
    ]
