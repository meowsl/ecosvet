# Generated by Django 4.2.6 on 2024-09-18 20:12

import apps.api.reference.models.achievement
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание достижения')),
                ('icon', models.ImageField(upload_to=apps.api.reference.models.achievement.Achievement.upload_path, verbose_name='Иконка достижения')),
            ],
        ),
    ]
