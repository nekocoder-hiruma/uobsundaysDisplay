# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_youngartist', '0010_auto_20150724_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youngartistwinner',
            name='prize',
            field=models.CharField(max_length=20, choices=[(b'First Prize', b'First Prize'), (b'Second Prize', b'Second Prize'), (b'Third Prize', b'Third Prize')]),
        ),
    ]
