# Generated by Django 4.2.6 on 2024-09-19 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0001_initial'),
        ('auth_api', '0002_usertelegram'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='achievement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reference.achievement', verbose_name='Достижение пользователя'),
        ),
    ]
