# -*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from colorfield.fields import ColorField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

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
        default='Глобальная настройка'
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
    footer_phone = models.CharField(
        _('Телефон в нижней части страници'),
        max_length=90,
        blank=True,
        null=True,
        default='+7 (343) 111-11-11'
    )
    city = models.CharField(
        _('Город'),
        max_length=100,
        blank=True,
        null=True,
        default='г. Екатеринбург'
    )
    address = models.CharField(
        _('Адрес'),
        max_length=200,
        blank=True,
        null=True,
        default='ул. Первомайская, 77'
    )
    addressHref = models.CharField(
        _('Ссылка перенаправляющая на карты(Google/Yandex)'),
        max_length=500,
        blank=True,
        null=True,
        default='https://www.google.ru/maps/place/%D1%83%D0%BB.+%D0%9F%D0%B5%D1%80%D0%B2%D0%BE%D0%BC%D0%B0%D0%B9%D1%81%D0%BA%D0%B0%D1%8F,+77,+%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3,+%D0%A1%D0%B2%D0%B5%D1%80%D0%B4%D0%BB%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F+%D0%BE%D0%B1%D0%BB.,+620062/@56.8459859,60.639357,17z/data=!3m1!4b1!4m5!3m4!1s0x43c16c2be5298e21:0x77522d799d8f3f75!8m2!3d56.8459859!4d60.6415457'
    )
    footer_photo = models.ForeignKey(
        "album.album",
        verbose_name=_('Альбом'),
        related_name='footer_album',
        blank=True,
        null=True
    )

    footer_copyright = models.CharField(
        _('Текст копирайта в нижней части страницы'),
        max_length=20,
        blank=True,
        null=True,
        default='Copyright by Ideal\''
    )

    default_link_color = ColorField(_('Стандартный цвет ссылок'), blank=True,
                                    null=True)
    default_link_hover_color = ColorField(_('Стандартный цвет ссылок при наведении'), blank=True,
                                          null=True)

    default_color = ColorField(_('Цвет шрифта по умолчанию'), blank=True,
                               null=True)
    default_bg = ColorField(_('Цвет фона сайта'), blank=True,
                            null=True)
    default_image_bg = ProcessedImageField(
        verbose_name=_('Фоновое изображение сайта'),
        upload_to='background',
        processors=[ResizeToFit(1280)],
        format='JPEG',
        options={'quality': 90},
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