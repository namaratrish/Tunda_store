# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tunda', '0005_userregistration_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregistration',
            name='user',
        ),
    ]
