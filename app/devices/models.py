from django.db import models

from app.services.models import upload_to
from tinymce.models import HTMLField


class Producer(models.Model):
    name = models.CharField(verbose_name='Производитель', max_length=128)
    country = models.CharField(verbose_name='Страна', max_length=128)
    cover = models.ImageField(verbose_name='Логотип производителя', blank=True, upload_to=upload_to)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=256)
    cover = models.ImageField(verbose_name='Выбрать фотографию обложки', blank=True, upload_to=upload_to)
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)
    short_desc = models.CharField(verbose_name='Короткое описание для главной', max_length=256, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['sort_index']


class SubCategory(models.Model):
    category = models.ForeignKey('Category', verbose_name='Категория', related_name='cat_subcategories')
    name = models.CharField(verbose_name='Название подкатегории', max_length=256)
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['sort_index']



class Devices(models.Model):
    name = models.CharField(verbose_name='Название услуги', max_length=256)
    cover = models.ImageField(verbose_name='Выбрать фотографию обложки', blank=True, upload_to=upload_to)
    is_main = models.BooleanField(verbose_name='Выводить на главной', default=False)
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)
    tag = models.BooleanField(verbose_name='Новинка', default=False)

    sub_category = models.ForeignKey('SubCategory', verbose_name='Подкатегория оборудования', related_name='device_subcategories')
    producer = models.ForeignKey('Producer', verbose_name='Производитель', related_name='device_producers')
    producer_link = models.URLField(verbose_name='Ссылка на описание производителя', null=True)

    projects = models.ManyToManyField('projects.Project', verbose_name='Использован на мероприятиях:', blank=True)
    description = HTMLField(verbose_name='Описание проекта', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
        ordering = ['sort_index']
