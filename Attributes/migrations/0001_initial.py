# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


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
                ('discoverable', models.BooleanField(default=True, help_text=b'If checked off, all books associated with this author will be discoverable to clients')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identification', models.UUIDField(default=uuid.uuid4, null=True, verbose_name=b'Book ID')),
                ('title', models.CharField(max_length=256, null=True)),
                ('subtitle', models.CharField(max_length=256, null=True, blank=True)),
                ('pdf_file', models.FileField(upload_to=b'/Users/fadihannaal-kass/Desktop/ebookify/database/books', null=True, verbose_name=b'PDF File', blank=True)),
                ('epub_file', models.FileField(upload_to=b'/Users/fadihannaal-kass/Desktop/ebookify/database/books', null=True, verbose_name=b'EPUB File', blank=True)),
                ('mobi_file', models.FileField(upload_to=b'/Users/fadihannaal-kass/Desktop/ebookify/database/books', null=True, verbose_name=b'MOBI File', blank=True)),
                ('cover', models.ImageField(null=True, upload_to=b'/Users/fadihannaal-kass/Desktop/ebookify/database/covers', blank=True)),
                ('description', models.TextField(max_length=5000, null=True, blank=True)),
                ('num_pages', models.IntegerField(default=0, help_text=b"Leave at 0 if you don't want the number of pages to be shown", verbose_name=b'number of Pages')),
                ('num_views', models.IntegerField(default=0, verbose_name=b'Views')),
                ('num_downloads', models.IntegerField(default=0, verbose_name=b'Downloads')),
                ('discoverable', models.BooleanField(default=True, help_text=b'Make this book discoverable to view and download')),
                ('recommended', models.BooleanField(default=False, help_text=b'Recommend this book to your library visitors')),
                ('authors', models.ManyToManyField(to='Attributes.Author')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='BookFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feedback', models.TextField(max_length=1000, null=True)),
                ('feedback_date', models.DateTimeField(auto_now_add=True)),
                ('discoverable', models.BooleanField(default=True, help_text=b'Make this comment visible in the book view page')),
                ('book', models.ForeignKey(to='Attributes.Book')),
            ],
            options={
                'verbose_name': 'Book Feedback',
                'verbose_name_plural': 'Book Feedbacks',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, unique=True, null=True)),
                ('brief', models.TextField(max_length=2000, null=True, blank=True)),
                ('discoverable', models.BooleanField(default=True, help_text=b'If checked off, all books associated with this category will be discoverable to clients')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=256, unique=True, null=True)),
                ('discoverable', models.BooleanField(default=True, help_text=b'If checked off, all books associated with this contributor will be discoverable to clients')),
            ],
            options={
                'verbose_name': 'Contributor',
                'verbose_name_plural': 'Contributors',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, unique=True, null=True)),
                ('discoverable', models.BooleanField(default=True, help_text=b'If checked off, all books associated with this language will be discoverable to clients')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='Attributes.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='contributors',
            field=models.ManyToManyField(to='Attributes.Contributor', blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(to='Attributes.Language', null=True),
        ),
    ]
