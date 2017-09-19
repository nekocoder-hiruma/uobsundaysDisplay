# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_youngartist', '0017_youngartistoverview_judging'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youngartistoverview',
            name='Judging',
        ),
    ]
