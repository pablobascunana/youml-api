# Generated by Django 4.1 on 2022-08-14 11:30

import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('lastname', models.CharField(max_length=30, verbose_name='lastname')),
                ('email', models.EmailField(max_length=80, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='email')),
                ('password', models.CharField(max_length=150, verbose_name='password')),
                ('verified', models.BooleanField(default=False, verbose_name='verified')),
                ('state', models.PositiveSmallIntegerField(default=0, verbose_name='active')),
                ('role', models.CharField(default='USER', max_length=10, verbose_name='role')),
                ('login_attempts', models.PositiveSmallIntegerField(default=0, verbose_name='login_attempts')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='register_date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
