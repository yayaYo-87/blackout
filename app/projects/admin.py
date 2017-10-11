from django.contrib import admin
from django.utils.safestring import mark_safe

from app.projects.models import ProjectCategory, Project, ProjectImage, ProjectDevice


class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    fields = ['image', 'sorting', 'image_img',]
    readonly_fields = ['image_img']
    extra = 1
    suit_classes = 'suit-tab suit-tab-extra'


class ProjectDeviceInline(admin.StackedInline):
    model = ProjectDevice
    fields = ['category', 'device']
    filter_horizontal = ['device', ]
    extra = 1
    suit_classes = 'suit-tab suit-tab-extra'


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    model = ProjectCategory
    fields = ['name', 'slug', 'cover', 'image_img', 'sort_index']
    readonly_fields = ['image_img']

    def image_img(self, obj):
        if obj.cover:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(obj.cover.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Фотография обложки'
    image_img.allow_tags = True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    fieldsets = [
        (
            'Основные характеристики',
            {
                'classes': ('suit-tab', 'suit-tab-general',),
                'fields': (
                    'name',
                    'cover',
                    'image_img',
                    'short_desc',
                    'description',
                    'category',
                    'date',
                    'youtube_link',
                    'sort_index',
                    'resent',
                )
            }
        ),
    ]
    readonly_fields = ['image_img']

    def image_img(self, obj):
        if obj.cover:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(obj.cover.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Фотография обложки'
    image_img.allow_tags = True
    inlines = [ProjectImageInline, ProjectDeviceInline]
    suit_form_tabs = (('general', 'Основные'), ('extra', 'Фото и оборудование'))
