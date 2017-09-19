# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uobsundays_helpers.helpers


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankingSolutionsImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to=uobsundays_helpers.helpers.upload_file_path, blank=True)),
                ('description', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
