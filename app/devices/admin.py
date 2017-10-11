from django.contrib import admin
from django.utils.safestring import mark_safe

from app.devices.models import Producer, Category, SubCategory, Devices


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    model = Producer
    fields = ['name', 'cover', 'image_img', 'country']
    readonly_fields = ['image_img']

    def image_img(self, obj):
        if obj.cover:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(obj.cover.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Фотография обложки'
    image_img.allow_tags = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fields = ['name', 'cover', 'image_img', 'sort_index', 'short_desc']
    readonly_fields = ['image_img']

    def image_img(self, obj):
        if obj.cover:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(obj.cover.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Фотография обложки'
    image_img.allow_tags = True


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    model = SubCategory
    fields = ['name', 'sort_index', 'category']


@admin.register(Devices)
class DevicesAdmin(admin.ModelAdmin):
    model = Devices
    fieldsets = [
        (
            'Основные характеристики',
            {
                'classes': ('suit-tab', 'suit-tab-general',),
                'fields': (
                    'name',
                    'cover',
                    'image_img',
                    'sub_category',
                    'description',
                    'sort_index',
                    'is_main',
                    'tag',
                    'you_tube_link'
                )
            }
        ),
        (
            'Дополнительно',
            {
                'classes': ('suit-tab', 'suit-tab-extra',),
                'fields': ('producer', 'producer_link', 'projects')
            }
        )
    ]
    filter_horizontal = ['projects', ]
    readonly_fields = ['image_img']

    def image_img(self, obj):
        if obj.cover:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(obj.cover.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Фотография обложки'
    image_img.allow_tags = True
    suit_form_tabs = (('general', 'Основные'), ('extra', 'Дополнительно'))
