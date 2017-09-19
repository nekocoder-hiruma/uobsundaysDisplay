# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_event', '0002_eventvote'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='EventImage',
        ),
    ]
