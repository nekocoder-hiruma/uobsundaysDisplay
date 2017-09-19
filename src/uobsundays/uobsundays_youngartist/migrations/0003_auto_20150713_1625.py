# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_youngartist', '0002_youngartistsubmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youngartistsubmission',
            name='location',
            field=models.CharField(max_length=1, choices=[(b'J', b'JEM'), (b'N', b'NEX')]),
        ),
    ]
