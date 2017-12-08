# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from app.models import TimeStampedModel, Service, Schedule
from album.models import Album

class BasePage(TimeStampedModel):
    title = models.CharField(
        _('Заголовок'),
        help_text=_('Название заголовка во вкладке'),
        max_length=100
    )
    meta = models.TextField(
        _('META-описание сайта'),
        max_length=300,
        blank=True,
        null=True
    )

    content = models.TextField(
        _('Контент страницы'),
        max_length=300,
        blank=True,
        null=True
    )

    scripts =  models.TextField(
        _('Скрипты'),
        help_text=_('Можно вставить код метрик, который будет работать только на текущей странице.'),
        max_length=4085,
        blank=True,
        null=True
    )
    class Meta:
        abstract=True

class HomePage(BasePage):
    main_title = models.CharField(
        _('Главный заголовок'),
        help_text=_('Главный заголовок на домшней странице'),
        max_length=150
    )
    jumbotron_video = models.TextField(
        _('Джамботрон - видео'),
        help_text=_('Элемент идущий после главного заголовка - это может быть картинка, либо видео и т.д. Будет выбрано либо видео, либо изображение.'),
        max_length=1024,
        blank=True,
        null=True
    )
    jumbotron_image = models.ImageField(
        _('Джамботрон - изображение'),
        help_text=_('Элемент идущий после главного заголовка - это может быть картинка, либо видео и т.д.Будет выбрано либо видео, либо изображение.'),
        blank=True,
        null=True
    )
    is_image = models.BooleanField(_('Отобразить избражение?'), default=False)
    is_video = models.BooleanField(_('Отобразить видео?'), default=True)


    class Meta:
        db_table='data_home_page'
        verbose_name=_('Страница "Главная"')
        verbose_name_plural = _('Страница "Главная"')




class SaunaPage(BasePage):

    name = models.CharField(
        _('Название сауны'),
        max_length=150
    )
    schedule = models.ManyToManyField(
        Schedule,
        verbose_name=_('Расписание'),
        related_name='sauna_schedule'
    )
    services = models.ManyToManyField(
        Service,
        verbose_name=_('Список услуг'),
        related_name='sauna_services'
    )
    gallery = models.ForeignKey(
        Album,
        models.SET_NULL,
        verbose_name=_('Галерея фотографий'),
        null=True
    )

    class Meta:
        db_table = 'data_sauna_page'
        verbose_name = _('Сауна')
        verbose_name_plural = _('Сауны')

class ServicesPage(BasePage):
    sauna = models.ManyToManyField(
        SaunaPage,
        verbose_name=_('Сауны'),
        related_name='shown_services_sauna',
        help_text=_('Сауны, который будут отображены в услугах')
    )

    class Meta:
        db_table = 'data_services_page'
        verbose_name = _('Станица "Услуги"')
        verbose_name_plural = _('Страница "Услуги"')


class PricesPage(BasePage):
    sauna = models.ManyToManyField(
        SaunaPage,
        verbose_name=_('Сауны'),
        related_name='shown_prices_sauna',
        help_text=_('Сауны, чьи цены и расписание будут отображенны на странице цен.')
    )
    class Meta:
        db_table = 'data_prices_page'
        verbose_name = _('Страница "Цены"')
        verbose_name_plural = _('Страница "Цены"')


class ContactsPage(BasePage):
    class Meta:
        db_table = 'data_contacts_page'
        verbose_name = _('Страница "Контакты"')
        verbose_name_plural = _('Страница "Контакты"')