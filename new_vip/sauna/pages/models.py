# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from app.models import TimeStampedModel, Service, Schedule
from album.models import Album
from .validators import validate_slug_field

class PageManager(models.Manager):
    user_for_related_fields = True

class BasePage(TimeStampedModel):

    title = models.CharField(
        _('Заголовок'),
        help_text=_('Название страницы во вкладке'),
        max_length=100
    )
    meta = models.TextField(
        _('META-описание сайта'),
        max_length=300,
        blank=True,
        null=True
    )
    main_title = models.CharField(
        _('Заголовок страницы'),
        help_text=_('Заголовок(можно обернуть в ссылку)'),
        max_length=500,
        null=True,
        blank=True
    )
    content = models.TextField(
        _('Контент страницы'),
        max_length=16000,
        blank=True,
        null=True,
        help_text=_('Заголовок - h3, параграф - p.')
    )

    scripts =  models.TextField(
        _('Скрипты'),
        help_text=_('Можно вставить код метрик, который будет работать только на текущей странице.'),
        max_length=4085,
        blank=True,
        null=True
    )

    objects = PageManager()
    def __str__(self):
        return self.title
    class Meta:
        abstract=True
class SaunaPage(BasePage):
    main_title = None
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
    slug = models.SlugField(
        _('Название ссылки к странице сауны'),
        max_length=70,
        help_text=_('К примеру, "my_new_awesome_hall"'),
        default='',
        validators=[validate_slug_field],
        unique=True
    )
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'data_sauna_page'
        verbose_name = _('Сауна')
        verbose_name_plural = _('Сауны')
class HomePage(BasePage):
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
    image_href = models.URLField(
        _('Отобразить избражение?'),
        max_length=500,
        help_text=_('Ссылка оборачивающая главное изображение.'),
        blank=True,
        null=True
    )
    is_video = models.BooleanField(_('Отобразить видео?'), default=True)
    sauna = models.ManyToManyField(
        SaunaPage,
        verbose_name=_('Сауны'),
        related_name='shown_home_sauna',
        help_text=_('Списко саун, которые отображаются в конце страницы.')
    )

    class Meta:
        db_table='data_home_page'
        verbose_name=_('Страница "Главная"')
        verbose_name_plural = _('Страница "Главная"')


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
    phone_1 = models.CharField(
        _('Телефон 2'),
        max_length=90,
        blank=True,
        null=True,
        default='+7 (343) 36-16-911'

    )
    phone_2 = models.CharField(
        _('Телефон 1'),
        max_length=90,
        blank=True,
        null=True,
        default='+7 (922) 18-16-911'
    )
    map = models.TextField(
        _('Окно с картой'),
        help_text=_('Карта, которая отображается в контактах'),
        max_length=2048,
        blank=True,
        null=True,
        default='<iframe class=\'mapContainer__map\' src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2181.9975502050816!2d60.63935701597335!3d56.84598588085985!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x43c16c2be5298e21%3A0x77522d799d8f3f75!2z0YPQuy4g0J_QtdGA0LLQvtC80LDQudGB0LrQsNGPLCA3Nywg0JXQutCw0YLQtdGA0LjQvdCx0YPRgNCzLCDQodCy0LXRgNC00LvQvtCy0YHQutCw0Y8g0L7QsdC7LiwgNjIwMDYy!5e0!3m2!1sru!2sru!4v1508837567170" width="100%" height="600" frameborder="0" style="border:0" allowfullscreen></iframe>'
    )
    class Meta:
        db_table = 'data_contacts_page'
        verbose_name = _('Страница "Контакты"')
        verbose_name_plural = _('Страница "Контакты"')