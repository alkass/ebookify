# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, null=True)),
                ('description', models.TextField(max_length=2000, null=True, blank=True)),
                ('deprecated', models.BooleanField(default=False, help_text=b'Hide this book')),
                ('author1', models.ForeignKey(related_name='author1', to='Attributes.Author')),
                ('author2', models.ForeignKey(related_name='author2', blank=True, to='Attributes.Author')),
                ('category', models.ForeignKey(blank=True, to='Attributes.Category', null=True)),
                ('contributor', models.ForeignKey(blank=True, to='Attributes.Contributor', null=True)),
                ('language', models.ForeignKey(blank=True, to='Attributes.Language', null=True)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
