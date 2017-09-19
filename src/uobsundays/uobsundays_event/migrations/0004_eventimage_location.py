# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_event', '0003_auto_20150616_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventimage',
            name='location',
            field=models.CharField(default=datetime.datetime(2015, 6, 17, 10, 18, 35, 131774, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
