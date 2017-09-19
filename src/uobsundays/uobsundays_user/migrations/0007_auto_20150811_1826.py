# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_user', '0006_auto_20150811_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_time_vote',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nric',
            field=models.CharField(max_length=12),
        ),
    ]
