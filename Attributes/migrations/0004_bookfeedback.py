# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0003_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feedback', models.TextField(max_length=1000, null=True)),
                ('book', models.ForeignKey(to='Attributes.Book')),
            ],
            options={
                'verbose_name': 'Book Feedback',
                'verbose_name_plural': 'Book Feedbacks',
            },
        ),
    ]
