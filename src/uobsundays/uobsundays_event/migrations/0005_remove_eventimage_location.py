# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_event', '0004_eventimage_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventimage',
            name='location',
        ),
    ]
