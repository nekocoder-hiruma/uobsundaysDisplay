# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uobsundays_helpers.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_website', '0002_branches'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomepageImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('fg', models.ImageField(null=True, upload_to=uobsundays_helpers.helpers.upload_file_path, blank=True)),
                ('bg', models.ImageField(null=True, upload_to=uobsundays_helpers.helpers.upload_file_path, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
