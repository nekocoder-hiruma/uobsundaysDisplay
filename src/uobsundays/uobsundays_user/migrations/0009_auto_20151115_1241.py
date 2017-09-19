# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_user', '0008_auto_20151115_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(default='', max_length=12, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='nric',
            field=models.CharField(default='', max_length=12, blank=True),
            preserve_default=False,
        ),
    ]
