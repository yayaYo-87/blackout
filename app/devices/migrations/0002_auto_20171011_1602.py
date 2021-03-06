# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devices', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='projects',
            field=models.ManyToManyField(blank=True, to='projects.Project', verbose_name='Использован на мероприятиях:'),
        ),
        migrations.AddField(
            model_name='devices',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_subcategories', to='devices.SubCategory', verbose_name='Подкатегория оборудования'),
        ),
    ]
