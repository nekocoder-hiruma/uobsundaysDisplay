# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_youngartist', '0013_auto_20150724_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='youngartistsubmission',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
