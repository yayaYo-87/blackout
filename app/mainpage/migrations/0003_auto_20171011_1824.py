# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_auto_20171011_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='BottomSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Слайдер')),
            ],
            options={
                'verbose_name_plural': 'Нижние слайдеры',
                'verbose_name': 'Нижний лайдер',
            },
        ),
        migrations.CreateModel(
            name='TopSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Слайдер')),
            ],
            options={
                'verbose_name_plural': 'Верхние слайдеры',
                'verbose_name': 'Верхний слайдер',
            },
        ),
        migrations.AlterModelOptions(
            name='bottomslide',
            options={'ordering': ['sort_index'], 'verbose_name': 'Слайд', 'verbose_name_plural': 'Слайды'},
        ),
        migrations.AlterModelOptions(
            name='topslide',
            options={'ordering': ['sort_index'], 'verbose_name': 'Слайд', 'verbose_name_plural': 'Слайды'},
        ),
        migrations.AlterField(
            model_name='bottomslide',
            name='slider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bottom_sliders', to='mainpage.BottomSlider', verbose_name='Слайдер'),
        ),
        migrations.AlterField(
            model_name='topslide',
            name='slider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='top_sliders', to='mainpage.TopSlider', verbose_name='Слайдер'),
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
    ]
