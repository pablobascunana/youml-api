# Generated by Django 4.1.2 on 2022-10-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_imagelabels'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='storage_in',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='storage_in'),
        ),
    ]