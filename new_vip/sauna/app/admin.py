# -*- encoding: utf-8 -*-
from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import *
# Register your models here.


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('title', 'condition_1', 'condition_2', 'condition_3', 'note',)
    filter_fields = ('title', 'condition_1', 'condition_2', 'condition_3', 'created',)
    search_fields = ('title', 'condition_1', 'condition_2', 'condition_3', 'note',)
    date_hierarchy = 'created'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_per_page = 10
    filter_fields = ('name', 'created',)
    search_fields = ('name',)
    date_hierarchy = 'created'
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
                ('email', 'footer_phone',),
                ('city', 'address',),
                ('addressHref',),
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
        ('Нижняя часть страницы', {
            'fields': (
                ('footer_photo',),
                ('footer_copyright',)
            ),
        },),
    )
