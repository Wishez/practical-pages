# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-09 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import pages.validators


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20171209_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saunapage',
            name='slug',
            field=models.SlugField(default='', help_text='К примеру, "my_new_awesome_hall"', max_length=70, unique=True, validators=[pages.validators.validate_slug_field], verbose_name='Название ссылки к странице сауны'),
        ),
    ]
