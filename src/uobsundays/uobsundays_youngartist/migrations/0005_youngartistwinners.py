# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uobsundays_helpers.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_youngartist', '0004_auto_20150717_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoungArtistWinners',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prize', models.CharField(max_length=3, choices=[(b'1', b'First Prize'), (b'2', b'Second Prize'), (b'3', b'Third Prize')])),
                ('artist_photo', models.ImageField(null=True, upload_to=uobsundays_helpers.helpers.upload_file_path, blank=True)),
                ('artist', models.CharField(max_length=200)),
                ('artist_age', models.CharField(max_length=200)),
                ('number_of_likes', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=3, choices=[(b'1', b'Category A'), (b'2', b'Category B')])),
            ],
        ),
    ]
