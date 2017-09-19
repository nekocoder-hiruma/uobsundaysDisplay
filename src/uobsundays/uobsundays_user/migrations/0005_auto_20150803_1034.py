# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_user', '0004_auto_20150803_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facebook_uid', models.PositiveIntegerField(null=True, blank=True)),
                ('facebook_access_token', models.CharField(max_length=255, blank=True)),
                ('facebook_access_token_expires', models.PositiveIntegerField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
