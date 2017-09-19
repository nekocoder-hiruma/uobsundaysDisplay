# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_user', '0010_auto_20151124_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=400)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='email address', db_index=True)),
                ('first_name', models.CharField(max_length=400, verbose_name=b'first name')),
                ('last_name', models.CharField(max_length=400, verbose_name=b'last name')),
                ('UID', models.PositiveIntegerField(null=True, blank=True)),
            ],
        ),
    ]
