# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-09 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0007_remove_album_album_images'),
        ('app', '0008_auto_20171208_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='footer_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='footer_album', to='album.Album', verbose_name='Альбом'),
        ),
    ]
