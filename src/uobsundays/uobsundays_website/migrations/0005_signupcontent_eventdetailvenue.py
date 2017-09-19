# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_website', '0004_homepageimage_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupcontent',
            name='EventDetailVenue',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
