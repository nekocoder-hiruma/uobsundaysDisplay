# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_user', '0005_auto_20150803_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_time_vote',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_time_vote',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 11, 6, 23, 40, 372999, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
