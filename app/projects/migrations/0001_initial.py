# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 19:46
from __future__ import unicode_literals

import app.services.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название пректа')),
                ('cover', models.ImageField(blank=True, upload_to=app.services.models.upload_to, verbose_name='Выбрать фотографию обложки')),
                ('date', models.DateField(verbose_name='Дата')),
                ('youtube_link', models.URLField(null=True, verbose_name='Ссылка на видео')),
                ('short_desc', models.TextField(null=True, verbose_name='Короткое описание')),
                ('description', models.TextField(verbose_name='Описание')),
                ('sort_index', models.PositiveIntegerField(default=0, verbose_name='Индекс сортировки')),
                ('resent', models.BooleanField(default=False, verbose_name='Недавний проект')),
            ],
            options={
                'ordering': ['sort_index'],
                'verbose_name_plural': 'Проекты',
                'verbose_name': 'Проект',
            },
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название категории')),
                ('cover', models.ImageField(blank=True, upload_to=app.services.models.upload_to, verbose_name='Выбрать фотографию обложки')),
                ('sort_index', models.PositiveIntegerField(default=0, verbose_name='Индекс сортировки')),
            ],
            options={
                'ordering': ['sort_index'],
                'verbose_name_plural': 'Категории проектов',
                'verbose_name': 'Категория проекта',
            },
        ),
        migrations.CreateModel(
            name='ProjectDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ManyToManyField(related_name='project_devices_category', to='devices.Category', verbose_name='Категория оборудования')),
                ('device', models.ManyToManyField(related_name='project_devices', to='devices.Devices', verbose_name='Оборудование')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_devices', to='projects.Project', verbose_name='Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=app.services.models.upload_to, verbose_name='Изображение')),
                ('sorting', models.PositiveIntegerField(blank=True, default=0, verbose_name='Сортировка')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_images', to='projects.Project', verbose_name='Фото для проекта')),
            ],
            options={
                'ordering': ['sorting'],
                'verbose_name_plural': 'Фотографии проекта',
                'verbose_name': 'Фотография проекта',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_categories', to='projects.ProjectCategory', verbose_name='Категория проекта'),
        ),
    ]
