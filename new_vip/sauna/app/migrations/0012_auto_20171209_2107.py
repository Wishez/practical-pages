# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-09 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20171209_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='map',
        ),
        migrations.AlterField(
            model_name='settings',
            name='address',
            field=models.CharField(blank=True, default='ул. Первомайская, 77', max_length=200, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='city',
            field=models.CharField(blank=True, default='г. Екатеринбург', max_length=100, null=True, verbose_name='Город'),
        ),
    ]