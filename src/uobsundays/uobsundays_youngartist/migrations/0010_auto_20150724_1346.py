# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_youngartist', '0009_auto_20150724_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youngartistwinner',
            name='category',
            field=models.CharField(max_length=200, choices=[(b'Category A', b'Category A'), (b'Category B', b'Category B')]),
        ),
    ]
