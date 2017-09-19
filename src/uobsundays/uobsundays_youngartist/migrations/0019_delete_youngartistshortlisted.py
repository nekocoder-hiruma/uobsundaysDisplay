# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_youngartist', '0018_remove_youngartistoverview_judging'),
    ]

    operations = [
        migrations.DeleteModel(
            name='YoungArtistShortlisted',
        ),
    ]
