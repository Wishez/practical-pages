# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-09 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20171209_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='contacts_phone',
        ),
        migrations.AddField(
            model_name='settings',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='footer_copyright',
            field=models.CharField(blank=True, default="Copyright by Ideal'", max_length=20, null=True, verbose_name='Текст копирайта в нижней части страницы'),
        ),
    ]
