# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_youngartist', '0007_auto_20150723_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youngartistwinner',
            name='category',
            field=models.CharField(max_length=3, choices=[(b'catA', b'Category A'), (b'catB', b'Category B')]),
        ),
        migrations.AlterField(
            model_name='youngartistwinner',
            name='prize',
            field=models.CharField(max_length=20, choices=[(b'first', b'First Prize'), (b'second', b'Second Prize'), (b'third', b'Third Prize')]),
        ),
    ]
