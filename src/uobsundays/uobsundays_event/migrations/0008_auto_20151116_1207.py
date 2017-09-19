# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_event', '0007_eventimage3'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventimage',
            options={'verbose_name': 'June Photo Gallery', 'verbose_name_plural': 'June Photo Galleries'},
        ),
        migrations.AlterModelOptions(
            name='eventimage2',
            options={'verbose_name': 'July Photo Gallery', 'verbose_name_plural': 'July Photo Galleries'},
        ),
        migrations.AlterModelOptions(
            name='eventimage3',
            options={'verbose_name': 'November Photo Gallery', 'verbose_name_plural': 'November Photo Galleries'},
        ),
    ]
