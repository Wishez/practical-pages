# Generated by Django 2.0 on 2017-12-08 14:34

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=1024, verbose_name='Описание')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Отображать альбом?')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AlbumImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='albums')),
                ('alt', models.CharField(default=uuid.uuid4, max_length=255, verbose_name='Альтернативный текст изображения')),
                ('width', models.IntegerField(default=0, help_text='По умолчанию - адаптивно', verbose_name='Ширина, на ваше усмотрение')),
                ('height', models.IntegerField(default=0, help_text='По умолчанию - адаптивно', verbose_name='Высонта, на ваше усмотрение')),
                ('slug', models.SlugField(default=uuid.uuid4, editable=False, max_length=70)),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='album.Album', verbose_name='Альбом')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
