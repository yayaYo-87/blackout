from django.contrib import admin
from django.utils.safestring import mark_safe
import nested_admin

from app.services.models import Service, ServiceDescription


class ServiceDescriptionInline(admin.StackedInline):
    model = ServiceDescription
    fields = ['name', 'cover', 'image_img', 'description', 'sort_index']
    readonly_fields = ['image_img']
    extra = 1
    suit_classes = 'suit-tab suit-tab-points'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    model = Service
    fieldsets = [
        (
            'Основные характеристики',
            {
                'classes': ('suit-tab', 'suit-tab-general',),
                'fields': (
                    'name',
                    'cover',
                    'image_img',
                    'short_description',
                    'sort_index',
                )
            }
        ),
    ]
    readonly_fields = ['image_img']
    inlines = [ServiceDescriptionInline, ]

    def image_img(self, obj):
        if obj.cover:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(obj.cover.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Фотография обложки'
    image_img.allow_tags = True
    suit_form_tabs = (('general', 'Основные'), ('points', 'Подпункты описания'))

