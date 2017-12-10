# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-09 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20171208_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='image_href',
            field=models.URLField(blank=True, help_text='Ссылка оборачивающая главное изображение.', max_length=500, null=True, verbose_name='Отобразить избражение?'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='main_title',
            field=models.CharField(help_text='Главный заголовок на домшней странице(можно обернуть в ссылку)', max_length=500, verbose_name='Главный заголовок'),
        ),
    ]