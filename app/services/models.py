import os
import uuid

from django.db import models
from django.utils.safestring import mark_safe


def upload_to(instance, filename):
    """
    Auto generate name for File and Image fields.
    :param instance: Instance of Model
    :param filename: Name of uploaded file
    :return:
    """
    name, ext = os.path.splitext(filename)
    filename = "%s%s" % (uuid.uuid4(), ext or '.jpg')
    basedir = os.path.join(instance._meta.app_label, instance._meta.model_name)
    return os.path.join(basedir, filename[:2], filename[2:4], filename)


class Service(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название услуги', null=False, blank=True)
    cover = models.ImageField(verbose_name='Выбрать фотографию обложки', blank=True, upload_to=upload_to)
    short_description = models.TextField(verbose_name='Короткое описание услуги')
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['sort_index']


class ServiceDescription(models.Model):
    service = models.ForeignKey(Service, related_name='service_desces')
    name = models.CharField(verbose_name='Название', max_length=128)
    cover = models.ImageField(verbose_name='Выбрать фотографию подпункта', blank=True, upload_to=upload_to)
    description = models.TextField(verbose_name='Описание', null=True)
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт описания'
        verbose_name_plural = 'Пункты описания'
        ordering = ['sort_index']

    def image_img(self):
        if self.cover:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(self.cover.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Фотография подпункта'
    image_img.allow_tags = True