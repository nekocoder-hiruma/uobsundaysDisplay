# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uobsundays_helpers.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_youngartist', '0014_youngartistsubmission_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoungArtistShortlisted',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=uobsundays_helpers.helpers.upload_file_path, blank=True)),
                ('artist', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('location', models.CharField(max_length=3, choices=[(b'0', b'All'), (b'JEM', b'JEM'), (b'NEX', b'NEX')])),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]
