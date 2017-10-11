# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 13:02
from __future__ import unicode_literals

import app.services.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, verbose_name='Название услуги')),
                ('cover', models.ImageField(blank=True, upload_to=app.services.models.upload_to, verbose_name='Выбрать фотографию обложки')),
                ('short_description', models.TextField(verbose_name='Короткое описание услуги')),
                ('sort_index', models.PositiveIntegerField(default=0, verbose_name='Индекс сортировки')),
            ],
            options={
                'verbose_name': 'Услуга',
                'ordering': ['sort_index'],
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='ServiceDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('cover', models.ImageField(blank=True, upload_to=app.services.models.upload_to, verbose_name='Выбрать фотографию подпункта')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('sort_index', models.PositiveIntegerField(default=0, verbose_name='Индекс сортировки')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_desces', to='services.Service')),
            ],
            options={
                'verbose_name': 'Пункт описания',
                'ordering': ['sort_index'],
                'verbose_name_plural': 'Пункты описания',
            },
        ),
    ]
