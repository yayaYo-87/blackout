# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 14:42
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
            name='BottomSlide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название слайда')),
                ('description', models.CharField(max_length=256, null=True, verbose_name='Короткое описание')),
                ('cover', models.ImageField(blank=True, upload_to=app.services.models.upload_to, verbose_name='Обложка слайда')),
                ('link', models.URLField(blank=True, verbose_name='Ссылка слайда')),
            ],
            options={
                'verbose_name_plural': 'Нижние слайды',
                'verbose_name': 'Нижний слайд',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Производитель')),
            ],
            options={
                'verbose_name_plural': 'Слайдеры',
                'verbose_name': 'Слайдер',
            },
        ),
        migrations.CreateModel(
            name='TopSlide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название слайда')),
                ('description', models.CharField(max_length=256, null=True, verbose_name='Короткое описание')),
                ('cover', models.ImageField(blank=True, upload_to=app.services.models.upload_to, verbose_name='Обложка слайда')),
                ('ikon', models.ImageField(blank=True, upload_to=app.services.models.upload_to, verbose_name='Иконка слайда')),
                ('link', models.URLField(blank=True, verbose_name='Ссылка слайда')),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='top_sliders', to='mainpage.Slider', verbose_name='Слайдер')),
            ],
            options={
                'verbose_name_plural': 'Верхние слайды',
                'verbose_name': 'Верхний слайд',
            },
        ),
        migrations.AddField(
            model_name='bottomslide',
            name='slider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bottom_sliders', to='mainpage.Slider', verbose_name='Слайдер'),
        ),
    ]