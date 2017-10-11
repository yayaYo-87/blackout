from django.contrib import admin

from app.mainpage.models import TopSlide, BottomSlide, TopSlider, BottomSlider


class TopSlideInline(admin.StackedInline):
    model = TopSlide
    fields = ['name', 'sort_index', 'cover', 'image_img', 'ikon', 'ikon_img', 'link']
    readonly_fields = ['image_img', 'ikon_img']
    extra = 1


class BottomSlideInline(admin.StackedInline):
    model = BottomSlide
    fields = ['name', 'sort_index', 'cover', 'image_img', 'link']
    readonly_fields = ['image_img',]
    extra = 1


@admin.register(TopSlider)
class TopSliderAdmin(admin.ModelAdmin):
    model = TopSlider
    fieldsets = [
        (
            'Основные характеристики',
            {
                'classes': ('suit-tab', 'suit-tab-general',),
                'fields': (
                    'name',
                )
            }
        ),
    ]
    inlines = [TopSlideInline, ]
    suit_form_tabs = (('general', 'Слайдер'),)


@admin.register(BottomSlider)
class BottomSliderAdmin(admin.ModelAdmin):
    model = BottomSlider
    fieldsets = [
        (
            'Основные характеристики',
            {
                'classes': ('suit-tab', 'suit-tab-general',),
                'fields': (
                    'name',
                )
            }
        ),
    ]
    inlines = [BottomSlideInline, ]
    suit_form_tabs = (('general', 'Слайдер'),)