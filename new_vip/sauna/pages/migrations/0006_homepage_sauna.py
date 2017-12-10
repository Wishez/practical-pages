# Generated by Django 2.0 on 2017-12-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20171208_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='sauna',
            field=models.ManyToManyField(help_text='Списко саун, которые отображаются в конце страницы.', related_name='shown_home_sauna', to='pages.SaunaPage', verbose_name='Сауны'),
        ),
    ]