# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0008_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='auth1',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='auth2',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='auth3',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='auth4',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='auth5',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='category',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='contrib1',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='contrib2',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='contrib3',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='language',
        ),
        migrations.DeleteModel(
            name='Upload',
        ),
    ]
