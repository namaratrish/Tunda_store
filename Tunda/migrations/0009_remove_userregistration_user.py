# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tunda', '0008_auto_20150808_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregistration',
            name='user',
        ),
    ]
