# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-21 17:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='email',
            new_name='usersname',
        ),
    ]
