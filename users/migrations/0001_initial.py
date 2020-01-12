# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-01-12 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('page_views', models.IntegerField(verbose_name='Просмотр страницы')),
                ('clicks', models.IntegerField(verbose_name='Клики')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(db_index=True, verbose_name='Индекс юзера')),
                ('first_name', models.CharField(max_length=64, verbose_name='Имя юзера')),
                ('last_name', models.CharField(max_length=64, verbose_name='Фамилия юзера')),
                ('email', models.EmailField(max_length=254, verbose_name='Фамилия юзера')),
                ('gender', models.CharField(max_length=10, verbose_name='Пол юзера')),
                ('ip_address', models.GenericIPAddressField(verbose_name='Ip адресс юзера')),
            ],
        ),
        migrations.AddField(
            model_name='statistic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]