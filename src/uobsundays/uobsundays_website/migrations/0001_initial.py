# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignupContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('EventDetailDate', ckeditor.fields.RichTextField()),
                ('EventDetailSession', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
