# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tunda', '0002_auto_20150805_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='emailAddress',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='firstName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='lastName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='password',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='userName',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterModelTable(
            name='userregistration',
            table='Users',
        ),
    ]
