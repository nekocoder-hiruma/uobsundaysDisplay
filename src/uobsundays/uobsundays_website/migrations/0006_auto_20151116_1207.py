# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_website', '0005_signupcontent_eventdetailvenue'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branches',
            options={'verbose_name': 'Branch', 'verbose_name_plural': 'Branches'},
        ),
    ]
