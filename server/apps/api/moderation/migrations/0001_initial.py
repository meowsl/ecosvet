# Generated by Django 4.2.6 on 2024-09-19 05:53

import apps.api.moderation.models.application
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Название мероприятия')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to=apps.api.moderation.models.application.Application.upload_path, verbose_name='Картинка мероприятия')),
                ('date', models.DateTimeField(verbose_name='Дата мероприятия')),
                ('address', models.CharField(max_length=64, verbose_name='Адрес мероприятия')),
                ('landmark', models.CharField(blank=True, max_length=100, verbose_name='Ориентир')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Заявка на мероприятие',
                'verbose_name_plural': 'Заявки на мероприятие',
            },
        ),
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Одобрено'), (2, 'Отклонено')], editable=False, verbose_name='Статус заявки')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moderation.application', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'Архив',
                'verbose_name_plural': 'Архив',
                'ordering': ['-id'],
            },
        ),
    ]
