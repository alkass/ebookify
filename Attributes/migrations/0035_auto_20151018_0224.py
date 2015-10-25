# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0034_auto_20151012_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='file2',
            new_name='epub_file',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='file3',
            new_name='mobi_file',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='file1',
            new_name='pdf_file',
        ),
        migrations.RemoveField(
            model_name='book',
            name='cats',
        ),
    ]
