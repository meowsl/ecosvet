# Generated by Django 4.2.6 on 2024-09-16 12:49

import apps.api.blog.models.post
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
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Контент')),
                ('content_type', models.CharField(choices=[('AR', 'Статьи'), ('IN', 'Интервью'), ('RE', 'Исследования'), ('RP', 'Отчеты'), ('UP', 'Обновления платформы')], default='AR', max_length=2, verbose_name='Тип контента')),
                ('image', models.ImageField(blank=True, upload_to=apps.api.blog.models.post.Post.upload_path, verbose_name='Изображение для поста')),
                ('publish_date', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('update_date', models.DateField(auto_now=True, verbose_name='Дата изменения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор поста')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-id'],
            },
        ),
    ]