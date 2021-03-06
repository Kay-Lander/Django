# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-19 22:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('publish_date', models.TextField()),
                ('category', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('in_print', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='authors',
            name='books',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='Books.Books'),
        ),
    ]
