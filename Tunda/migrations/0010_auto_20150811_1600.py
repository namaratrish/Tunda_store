# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tunda', '0009_remove_userregistration_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregistration',
            old_name='firstName',
            new_name='Address',
        ),
        migrations.RemoveField(
            model_name='userregistration',
            name='emailAddress',
        ),
        migrations.RemoveField(
            model_name='userregistration',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='userregistration',
            name='password',
        ),
        migrations.RemoveField(
            model_name='userregistration',
            name='username',
        ),
        migrations.AddField(
            model_name='userregistration',
            name='City',
            field=models.CharField(default=datetime.datetime(2015, 8, 11, 13, 0, 34, 3000, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userregistration',
            name='user',
            field=models.OneToOneField(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
