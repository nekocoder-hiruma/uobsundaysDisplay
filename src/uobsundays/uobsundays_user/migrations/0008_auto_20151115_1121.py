# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_user', '0007_auto_20150811_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nric',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
