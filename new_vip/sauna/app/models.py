# -*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_save
from colorfield.fields import ColorField

if not settings.DEBUG:
    encoding = 'utf-8'
    import sys
    reload(sys)
    sys.setdefaultencoding(encoding)

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Settings(TimeStampedModel):
    name = models.CharField(
        _('Имя настройки'),
        max_length=100,
        default='Main Settings'
    )
    widgets = models.TextField(
        _('Метрики, виджеты и прочее'),
        max_length=8196,
        blank=True,
        null=True
    )
    meta = models.TextField(
        _('Глобальное META-описание сайта'),
        max_length=300,
        blank=True,
        null=True
    )
    email = models.CharField(
        _('Email'),
        max_length=200,
        blank=True,
        null=True
    )
    contacts_phone = models.CharField(
        _('Телефон/ы на странице контактов'),
        max_length=90,
        blank=True,
        null=True
    )
    footer_phone = models.CharField(
        _('Телефон в нижней части страници'),
        max_length=90,
        blank=True,
        null=True
    )
    address = models.CharField(
        _('Адрес'),
        max_length=200,
        blank=True,
        null=True
    )
    addressHref = models.CharField(
        _('Ссылка перенаправляющая на карты(Google/Yandex)'),
        max_length=500,
        blank=True,
        null=True
    )
    map = models.TextField(
        _('Окно с картой'),
        help_text=_('Карта, которая отображается в контактах'),
        max_length=1024,
        blank=True,
        null=True
    )

    default_link_color = ColorField(_('Стандартный цвет ссылок'), blank=True,
                                    null=True)
    default_link_hover_color = ColorField(_('Стандартный цвет ссылок при наведении'), blank=True,
                                          null=True)

    default_color = ColorField(_('Цвет шрифта по умолчанию'), blank=True,
                               null=True)
    default_bg = ColorField(_('Цвет фона сайта'), blank=True,
                            null=True)
    default_image_bg = models.ImageField(
        _('Фоновое изображение сайта'),
        upload_to='background/',
        blank=True,
        null=True
    )

    preloader_color = ColorField(_('Цвет прелоадера'), blank=True,
                                 null=True)
    curtain_bg = ColorField(_('Цвет фона предварительной загрузки'), blank=True,
                            null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table='site_settings'
        verbose_name = _('Настройка')
        verbose_name_plural = _('Настройки')


class Service(TimeStampedModel):
    name = models.CharField(
        _('Наименование услуги'),
        max_length=150
    )
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'sauna_service'
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')

class Schedule(TimeStampedModel):
    title = models.CharField(
        _('Период'),
        max_length=250,
        help_text=_('К примеру, "Буднии дни с ПН по ЧТ')
    )

    condition_1 = models.CharField(
        _('Время и цена(Условие 1)'),
        max_length=200,
        help_text=_('С 9:00 до 17:00 – 500 руб.\час')
    )

    condition_2 = models.CharField(
        _('Время и цена(Условие 2)'),
        max_length=200,
        help_text=_('с 17:00 до 09:00 – 1000 руб.\час'),
        blank=True,
        null=True
    )
    condition_3 = models.CharField(
        _('Время и цена(Условие 3)'),
        max_length=200,
        help_text=_('с 17:00 до 09:00 – 1000 руб.\час'),
        blank=True,
        null=True
    )

    note = models.CharField(
        _('Примечание'),
        max_length=250,
        help_text=_('К примеру, "*свыше 6 чел, за каждого последующего 100 руб.\час".'),
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'sauna_schedule'
        verbose_name = _('Расписание')
        verbose_name_plural = _('Расписания')