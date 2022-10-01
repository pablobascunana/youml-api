# Generated by Django 4.1.1 on 2022-10-01 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_company'),
        ('users', '0001_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(db_column='companyId', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company'),
        ),
    ]
