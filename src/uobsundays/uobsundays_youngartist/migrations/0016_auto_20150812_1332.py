# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_youngartist', '0015_youngartistshortlisted'),
    ]

    operations = [
        migrations.AddField(
            model_name='youngartistshortlisted',
            name='title',
            field=models.CharField(default='Title of drawing', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='youngartistsubmission',
            name='title',
            field=models.CharField(default='Title of drawing', max_length=200),
            preserve_default=False,
        ),
    ]
