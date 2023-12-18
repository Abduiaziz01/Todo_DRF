# Generated by Django 5.0 on 2023-12-16 11:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(message='Номер телефона должен быть в формате +996XXXXXXXXX.', regex='^\\+996\\d{9}$')], verbose_name='Номер телефона'),
        ),
    ]
