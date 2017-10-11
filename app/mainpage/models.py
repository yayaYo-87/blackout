from django.db import models
from django.utils.safestring import mark_safe

from app.services.models import upload_to


class TopSlider(models.Model):
    name = models.CharField(verbose_name='Слайдер', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Верхний слайдер'
        verbose_name_plural = 'Верхние слайдеры'


class BottomSlider(models.Model):
    name = models.CharField(verbose_name='Слайдер', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Нижний лайдер'
        verbose_name_plural = 'Нижние слайдеры'


class TopSlide(models.Model):
    slider = models.ForeignKey(TopSlider, verbose_name='Слайдер', related_name='top_sliders')
    name = models.CharField(verbose_name='Название слайда', max_length=256)
    description = models.CharField(verbose_name='Короткое описание', max_length=256, null=True)
    cover = models.ImageField(verbose_name='Обложка слайда', blank=True, upload_to=upload_to)
    ikon = models.ImageField(verbose_name='Иконка слайда', blank=True, upload_to=upload_to)
    link = models.URLField(verbose_name='Ссылка слайда', blank=True)
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)

    def __str__(self):
        return self.name

    def image_img(self):
        if self.cover:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(self.cover.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

    def ikon_img(self):
        if self.ikon:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(self.ikon.url))
        else:
            return '(Нет изображения)'

    ikon_img.short_description = 'Иконка'
    ikon_img.allow_tags = True

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        ordering = ['sort_index']


class BottomSlide(models.Model):
    slider = models.ForeignKey(BottomSlider, verbose_name='Слайдер', related_name='bottom_sliders')
    name = models.CharField(verbose_name='Название слайда', max_length=256)
    description = models.CharField(verbose_name='Короткое описание', max_length=256, null=True)
    cover = models.ImageField(verbose_name='Обложка слайда', blank=True, upload_to=upload_to)
    link = models.URLField(verbose_name='Ссылка слайда', blank=True)
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)

    def __str__(self):
        return self.name

    def image_img(self):
        if self.cover:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(self.cover.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        ordering = ['sort_index']