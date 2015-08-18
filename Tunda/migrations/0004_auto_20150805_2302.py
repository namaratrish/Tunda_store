# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tunda', '0003_auto_20150805_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='emailAddress',
            field=models.EmailField(max_length=50),
        ),
    ]
