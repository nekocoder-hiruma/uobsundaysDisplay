# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YoungArtistOverview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('Contest_Detail_Place', ckeditor.fields.RichTextField()),
                ('Contest_Detail_Date', ckeditor.fields.RichTextField()),
                ('Contest_Detail_Session', ckeditor.fields.RichTextField()),
                ('Sign_Up', ckeditor.fields.RichTextField()),
                ('Vote', ckeditor.fields.RichTextField()),
                ('Winner_Prize', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
