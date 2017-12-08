# -*- encoding: utf-8 -*-
from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import *
# Register your models here.


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('title', 'condition_1', 'condition_2', 'condition_3', 'note',)
    filter_fields = ('title', 'condition_1', 'condition_2', 'condition_3',)
    search_fields = ('title', 'condition_1', 'condition_2', 'condition_3', 'note',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_per_page = 10
    filter_fields = ('name',)
    search_fields = ('name',)
@admin.register(Settings)
class SettingsAdmin(SingleModelAdmin):
    fieldsets = (
        ('Настройка информации сайта', {
            'fields': (
                ('widgets',),
                ('meta',)
            ),
        },),
        ('Настройка контактной информации', {
            'fields': (
                ('email',),
                ('contacts_phone', 'footer_phone',),
                ('address', 'addressHref',),
                ('map',),
            ),
        },),
        ('Ссылки', {
            'fields': (
                ('default_link_color', 'default_link_hover_color',),
            ),
        },),
        ('Загрузка', {
            'fields': (
                ('preloader_color', 'curtain_bg',),
            ),
        },),
        ('Фон сайта', {
            'fields': (
                ('default_bg', 'default_image_bg',),
            ),
        },),
        ('Шрифт', {
            'fields': (
                ('default_color',),
            ),
        },),
    )
