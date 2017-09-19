# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_user', '0009_auto_20151115_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facebookuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='FacebookUser',
        ),
    ]
