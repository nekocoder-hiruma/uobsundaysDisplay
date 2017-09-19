# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_youngartist', '0016_auto_20150812_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='youngartistoverview',
            name='Judging',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
