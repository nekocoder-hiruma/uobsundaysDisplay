# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_user', '0002_auto_20150616_0352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facebook_uid', models.PositiveIntegerField(null=True, blank=True)),
                ('facebook_access_token', models.CharField(max_length=255, blank=True)),
                ('facebook_access_token_expires', models.PositiveIntegerField(null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
