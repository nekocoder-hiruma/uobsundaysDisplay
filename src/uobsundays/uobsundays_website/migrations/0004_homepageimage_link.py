# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_website', '0003_homepageimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepageimage',
            name='link',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
