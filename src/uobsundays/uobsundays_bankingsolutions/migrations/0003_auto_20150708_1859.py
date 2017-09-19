# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_bankingsolutions', '0002_bankingsolutionsimage_additional_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankingsolutionsimage',
            name='additional_content',
            field=ckeditor.fields.RichTextField(null=True, blank=True),
        ),
    ]
