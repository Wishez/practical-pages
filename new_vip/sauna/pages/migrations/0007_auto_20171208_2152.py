# Generated by Django 2.0 on 2017-12-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_homepage_sauna'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricespage',
            name='slug',
        ),
        migrations.AddField(
            model_name='saunapage',
            name='slug',
            field=models.SlugField(default='', help_text='К примеру, "my_new_awesome_hall"', max_length=70, verbose_name='Название ссылки к странице сауны'),
        ),
    ]
