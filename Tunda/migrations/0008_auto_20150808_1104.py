# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tunda', '0007_userregistration_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregistration',
            old_name='userName',
            new_name='username',
        ),
    ]
