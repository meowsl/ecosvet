# Generated by Django 4.2.6 on 2024-09-18 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('surname', models.CharField(blank=True, max_length=150, null=True, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('password', models.CharField(blank=True, max_length=128, null=True, verbose_name='Новый пароль участника')),
            ],
            options={
                'verbose_name': 'Заявка на участие',
                'verbose_name_plural': 'Заявки на участие',
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
