# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uobsundays_user', '0001_initial'),
        ('uobsundays_event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(related_name='votes', to='uobsundays_event.Event')),
                ('user', models.ForeignKey(related_name='votes', to='uobsundays_user.User')),
            ],
        ),
    ]
