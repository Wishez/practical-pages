# Generated by Django 2.0 on 2017-12-08 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_schedule_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='menu_link_active_color',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='menu_link_hover_bg',
        ),
    ]