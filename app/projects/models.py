from django.db import models
from django.utils.safestring import mark_safe

from app.services.models import upload_to


class ProjectCategory(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=256)
    slug = models.SlugField(verbose_name='URL', null=True, blank=False)
    cover = models.ImageField(verbose_name='Выбрать фотографию обложки', blank=True, upload_to=upload_to)
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория проекта'
        verbose_name_plural = 'Категории проектов'
        ordering = ['sort_index']


class Project(models.Model):
    category = models.ForeignKey('ProjectCategory', verbose_name='Категория проекта', related_name='project_categories')
    name = models.CharField(verbose_name='Название пректа', max_length=256)
    cover = models.ImageField(verbose_name='Выбрать фотографию обложки', blank=True, upload_to=upload_to)
    date = models.DateField(verbose_name='Дата', auto_now=False, auto_now_add=False)
    youtube_link = models.CharField(verbose_name='ID cсылки на видео', null=True, max_length=256, blank=True)
    short_desc = models.TextField(verbose_name='Короткое описание', null=True)
    description = models.TextField(verbose_name='Описание')
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)
    is_main = models.BooleanField(verbose_name='Выводить на главной', default=False)

    resent = models.BooleanField(verbose_name='Недавний проект', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['sort_index']


class ProjectImage(models.Model):
    project = models.ForeignKey('Project', null=True, blank=False, verbose_name='Фото для проекта', related_name='project_images')
    image = models.ImageField(verbose_name='Изображение', blank=False, upload_to=upload_to)
    sorting = models.PositiveIntegerField(verbose_name='Сортировка', default=0, blank=True)

    class Meta:
        verbose_name = 'Фотография проекта'
        verbose_name_plural = 'Фотографии проекта'
        ordering = ['sorting', ]

    def image_img(self):
        if self.image:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


class ProjectDevice(models.Model):
    project = models.ForeignKey('Project', verbose_name='Project', related_name='project_devices',)
    category = models.ForeignKey('devices.Category', verbose_name='Категория оборудования', null=True, blank=False)
    device = models.ManyToManyField('devices.Devices', verbose_name='Оборудование', related_name='project_devices')
