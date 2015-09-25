# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0015_auto_20150925_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='file1',
            field=models.FileField(upload_to=b'C:\\Users\\hannaafh\\Downloads\\ebookify\\database'),
        ),
    ]
