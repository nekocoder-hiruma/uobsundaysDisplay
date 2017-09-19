# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_youngartist', '0011_auto_20150724_1349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='youngartistwinner',
            options={'ordering': ['prize', 'category']},
        ),
    ]
