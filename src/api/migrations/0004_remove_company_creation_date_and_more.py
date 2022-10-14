# Generated by Django 4.1.2 on 2022-10-14 16:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='creation_date',
        ),
        migrations.AddField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(db_column='createdAt', default=django.utils.timezone.now, verbose_name='createdAt'),
        ),
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(db_column='createdAt', default=django.utils.timezone.now, verbose_name='createdAt'),
        ),
    ]
