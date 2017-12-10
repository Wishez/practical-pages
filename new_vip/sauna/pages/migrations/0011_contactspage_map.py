# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-09 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20171209_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactspage',
            name='map',
            field=models.TextField(blank=True, default='<iframe class=\'mapContainer__map\' src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2181.9975502050816!2d60.63935701597335!3d56.84598588085985!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x43c16c2be5298e21%3A0x77522d799d8f3f75!2z0YPQuy4g0J_QtdGA0LLQvtC80LDQudGB0LrQsNGPLCA3Nywg0JXQutCw0YLQtdGA0LjQvdCx0YPRgNCzLCDQodCy0LXRgNC00LvQvtCy0YHQutCw0Y8g0L7QsdC7LiwgNjIwMDYy!5e0!3m2!1sru!2sru!4v1508837567170" width="100%" height="600" frameborder="0" style="border:0" allowfullscreen></iframe>', help_text='Карта, которая отображается в контактах', max_length=2048, null=True, verbose_name='Окно с картой'),
        ),
    ]