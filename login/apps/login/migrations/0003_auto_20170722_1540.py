# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-22 20:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20170722_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Last_name',
            new_name='last_name',
        ),
    ]
