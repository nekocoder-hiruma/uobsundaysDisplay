# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_bankingsolutions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankingsolutionsimage',
            name='additional_content',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
