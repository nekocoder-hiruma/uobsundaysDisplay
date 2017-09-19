# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_youngartist', '0006_auto_20150723_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youngartistwinner',
            name='category',
            field=models.CharField(max_length=3, choices=[(b'0', b'Category A'), (b'1', b'Category B')]),
        ),
        migrations.AlterField(
            model_name='youngartistwinner',
            name='prize',
            field=models.CharField(max_length=3, choices=[(b'0', b'First Prize'), (b'1', b'Second Prize'), (b'2', b'Third Prize')]),
        ),
    ]
