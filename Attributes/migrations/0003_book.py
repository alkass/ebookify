# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0002_auto_20150917_0425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, null=True)),
                ('description', models.TextField(max_length=2000, null=True, blank=True)),
                ('deprecated', models.BooleanField(default=False, help_text=b'If checked off, this book will NOT be discoverable to clients')),
                ('identification', models.UUIDField(default=uuid.uuid4, null=True, verbose_name=b'Book ID')),
                ('author1', models.ForeignKey(related_name='author1', to='Attributes.Author', null=True)),
                ('author2', models.ForeignKey(related_name='author2', blank=True, to='Attributes.Author', null=True)),
                ('author3', models.ForeignKey(related_name='author3', blank=True, to='Attributes.Author', null=True)),
                ('author4', models.ForeignKey(related_name='author4', blank=True, to='Attributes.Author', null=True)),
                ('author5', models.ForeignKey(related_name='author5', blank=True, to='Attributes.Author', null=True)),
                ('category1', models.ForeignKey(related_name='category1', to='Attributes.Category', null=True)),
                ('category10', models.ForeignKey(related_name='category10', blank=True, to='Attributes.Category', null=True)),
                ('category2', models.ForeignKey(related_name='category2', blank=True, to='Attributes.Category', null=True)),
                ('category3', models.ForeignKey(related_name='category3', blank=True, to='Attributes.Category', null=True)),
                ('category4', models.ForeignKey(related_name='category4', blank=True, to='Attributes.Category', null=True)),
                ('category5', models.ForeignKey(related_name='category5', blank=True, to='Attributes.Category', null=True)),
                ('category6', models.ForeignKey(related_name='category6', blank=True, to='Attributes.Category', null=True)),
                ('category7', models.ForeignKey(related_name='category7', blank=True, to='Attributes.Category', null=True)),
                ('category8', models.ForeignKey(related_name='category8', blank=True, to='Attributes.Category', null=True)),
                ('category9', models.ForeignKey(related_name='category9', blank=True, to='Attributes.Category', null=True)),
                ('contributor1', models.ForeignKey(related_name='contributor1', blank=True, to='Attributes.Contributor', null=True)),
                ('contributor2', models.ForeignKey(related_name='contributor2', blank=True, to='Attributes.Contributor', null=True)),
                ('contributor3', models.ForeignKey(related_name='contributor3', blank=True, to='Attributes.Contributor', null=True)),
                ('language', models.ForeignKey(blank=True, to='Attributes.Language', null=True)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
