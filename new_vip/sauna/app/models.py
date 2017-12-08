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
class Contacts(TimeStampedModel):
    name = models.CharField(
        _('Подпись'),
        help_text=_('Заметка для того, чтобы отличать одни контакты от других. К примеру, "Основные контакты" или "Запасной вариант".'),
        max_length=100
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

    def __str__(self):
        return self.name

    class Meta:
        db_table='site_contacts'
        verbose_name = _('Контакты')
        verbose_name_plural = _('Контакты')

class Settings(TimeStampedModel):
    name = models.CharField(
        _('Имя настройки'),
        max_length=100
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

    contacts = models.ForeignKey(
        Contacts,
        models.SET_NULL,
        verbose_name=_('Контакты'),
        related_name='site_contacts',
        help_text=_('Укажите контакты, которые хотите отобразить'),
        blank=True,
        null=True
    )

    default_link_color = ColorField(_('Стандартный цвет ссылок'), blank=True,
                                    null=True)
    default_link_hover_color = ColorField(_('Стандартный цвет ссылок при наведении'), blank=True,
                                          null=True)

    menu_link_active_color = ColorField(_('Цвет шрифта активной ссылки'), blank=True,
                                        null=True)
    menu_link_hover_bg = ColorField(_('Цвет фона ссылок при наведении'), blank=True,
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
    # statuses = (
    #     (_('Не активная'), 'Не активна'),
    #     (_('Активная'), 'Активная'),
    # )
    # is_active = models.CharField(
    #     _('Активация'),
    #     default=_('Не активна'),
    #     choices=statuses,
    #     max_length=12
    # )

    def __str__(self):
        return self.name

    class Meta:
        db_table='site_settings'
        verbose_name = _('Настройка')
        verbose_name_plural = _('Настройки')


# def switch_active_custom(sender, instance, **kwargs):
#     print('Sender:', sender.objects.all())
#     print('Instance:', instance.is_active)
#     if instance.is_active == _('Активная'):
#         customs = sender.objects.all()
#         if len(customs):
#             for custom in customs:
#                 custom.is_active = _('Не активная')
#                 custom.save()
#         instance.is_active = _('Активная')
#
#
# pre_save.connect(switch_active_custom, sender=Settings)