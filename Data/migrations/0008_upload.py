# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Attributes', '0001_initial'),
        ('Data', '0007_book_identification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, null=True)),
                ('description', models.TextField(max_length=2000, null=True, blank=True)),
                ('deprecated', models.BooleanField(default=False, help_text=b'Hide this book')),
                ('identification', models.UUIDField(default=uuid.uuid4, null=True)),
                ('auth1', models.ForeignKey(related_name='auth1', to='Attributes.Author', null=True)),
                ('auth2', models.ForeignKey(related_name='auth2', blank=True, to='Attributes.Author', null=True)),
                ('auth3', models.ForeignKey(related_name='auth3', blank=True, to='Attributes.Author', null=True)),
                ('auth4', models.ForeignKey(related_name='auth4', blank=True, to='Attributes.Author', null=True)),
                ('auth5', models.ForeignKey(related_name='auth5', blank=True, to='Attributes.Author', null=True)),
                ('category', models.ForeignKey(blank=True, to='Attributes.Category', null=True)),
                ('contrib1', models.ForeignKey(related_name='contrib1', blank=True, to='Attributes.Contributor', null=True)),
                ('contrib2', models.ForeignKey(related_name='contrib2', blank=True, to='Attributes.Contributor', null=True)),
                ('contrib3', models.ForeignKey(related_name='contrib3', blank=True, to='Attributes.Contributor', null=True)),
                ('language', models.ForeignKey(blank=True, to='Attributes.Language', null=True)),
            ],
            options={
                'verbose_name': 'Upload',
                'verbose_name_plural': 'Uploads',
            },
        ),
    ]
