# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_youngartist', '0008_auto_20150724_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youngartistwinner',
            name='category',
            field=models.CharField(max_length=200, choices=[(b'catA', b'Category A'), (b'catB', b'Category B')]),
        ),
    ]
