# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_youngartist', '0019_delete_youngartistshortlisted'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='youngartistsubmission',
            options={'ordering': ['created']},
        ),
    ]
