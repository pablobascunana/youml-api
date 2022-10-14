# Generated by Django 4.1.2 on 2022-10-13 11:59

import api.mixins.validate_model
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_remove_company_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='uuid')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_column='creationDate', verbose_name='creationDate')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'project',
                'unique_together': {('user', 'name')},
            },
            bases=(api.mixins.validate_model.ValidateModelMixin, models.Model),
        ),
    ]