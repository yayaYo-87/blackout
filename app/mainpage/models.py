from django.db import models

from app.services.models import upload_to


class Slider(models.Model):
    name = models.CharField(verbose_name='Производитель', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'


class TopSlide(models.Model):
    slider = models.ForeignKey(Slider, verbose_name='Слайдер', related_name='top_sliders')
    name = models.CharField(verbose_name='Название слайда', max_length=256)
    description = models.CharField(verbose_name='Короткое описание', max_length=256, null=True)
    cover = models.ImageField(verbose_name='Обложка слайда', blank=True, upload_to=upload_to)
    ikon = models.ImageField(verbose_name='Иконка слайда', blank=True, upload_to=upload_to)
    link = models.URLField(verbose_name='Ссылка слайда', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Верхний слайд'
        verbose_name_plural = 'Верхние слайды'


class BottomSlide(models.Model):
    slider = models.ForeignKey(Slider, verbose_name='Слайдер', related_name='bottom_sliders')
    name = models.CharField(verbose_name='Название слайда', max_length=256)
    description = models.CharField(verbose_name='Короткое описание', max_length=256, null=True)
    cover = models.ImageField(verbose_name='Обложка слайда', blank=True, upload_to=upload_to)
    link = models.URLField(verbose_name='Ссылка слайда', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Нижний слайд'
        verbose_name_plural = 'Нижние слайды'