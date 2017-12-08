# -*- coding: utf-8 -*-
from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import *
# Register your models here.

base_settings_page = ('Базовая настройка страницы', {
                'fields': (
                    ('title',),
                    ('meta',),
                    ('scripts',),
                ),
            },)


@admin.register(HomePage)
class HomePageAdmin(SingleModelAdmin):
    fieldsets = (
        base_settings_page,
        ('Контент страницы', {
            'fields': (
                ('main_title',),
                ('jumbotron_video', 'is_video',),
                ('jumbotron_image', 'is_image',),
                ('content',),
            ),
        },),
    )

@admin.register(ServicesPage)
class ServicesPageAdmin(SingleModelAdmin):
    fieldsets = (
        base_settings_page,
        ('Контент страницы', {
            'fields': (
                ('sauna', 'content',),
            ),
        },),
    )
@admin.register(PricesPage)
class ServicesPageAdmin(SingleModelAdmin):
    fieldsets = (
        base_settings_page,
        ('Контент страницы', {
            'fields': (
                ('sauna', 'content',),
            ),
        },),
    )


@admin.register(ContactsPage)
class ContactsPageAdmin(SingleModelAdmin):
    fieldsets = (
        base_settings_page,
        ('Контент страницы', {
            'fields': (
                ('content',),
            ),
        },),
    )
@admin.register(SaunaPage)
class SaunaPageAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name', 'gallery',)
    filter_fields = ('name', 'gallery',)
    search_fields = ('name', 'gallery',)
    filter_horizontal = ('schedule', 'services',)
    fieldsets = (
        base_settings_page,
        ('Контент страницы', {
            'fields': (
                ('name',),
                ('services'),
                ('schedule'),
                ('gallery',),
                ('content',),
            ),
        },),
    )