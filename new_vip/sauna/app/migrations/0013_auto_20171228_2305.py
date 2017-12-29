# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-28 20:05
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20171209_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='default_image_bg',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='background', verbose_name='Фоновое изображение сайта'),
        ),
    ]
