# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0005_auto_20171012_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devices',
            name='slug',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, verbose_name='URL'),
        ),
    ]
