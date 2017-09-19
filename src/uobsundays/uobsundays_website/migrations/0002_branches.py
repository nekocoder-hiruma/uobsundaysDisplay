# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('map', models.TextField(null=True, blank=True)),
                ('branches', models.CharField(max_length=1, choices=[(b'O', b'Other'), (b'M', b'Main')])),
            ],
        ),
    ]
