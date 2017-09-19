# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_youngartist', '0003_auto_20150713_1625'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='youngartistsubmission',
            options={},
        ),
        migrations.AlterField(
            model_name='youngartistsubmission',
            name='location',
            field=models.CharField(max_length=3, choices=[(b'0', b'All'), (b'JEM', b'JEM'), (b'NEX', b'NEX')]),
        ),
    ]
