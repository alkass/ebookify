# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=256, unique=True, null=True)),
                ('brief', models.TextField(max_length=2000, null=True, blank=True)),
                ('deprecated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, unique=True, null=True)),
                ('brief', models.TextField(max_length=2000, null=True, blank=True)),
                ('deprecated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=256, unique=True, null=True)),
                ('deprecated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, unique=True, null=True)),
                ('deprecated', models.BooleanField(default=False)),
            ],
        ),
    ]
