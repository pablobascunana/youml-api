# Generated by Django 4.1.3 on 2022-11-09 21:34

import api.mixins.validate_model
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0013_image_mark_to_train_at_imagelabels_mark_to_train_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='uuid')),
                ('status', models.CharField(default='PENDING', max_length=10, verbose_name='status')),
                ('trained', models.BooleanField(db_column='trained', default=False, verbose_name='trained')),
                ('created_at', models.DateTimeField(db_column='createdAt', default=django.utils.timezone.now, verbose_name='createdAt')),
                ('dataset', models.ForeignKey(db_column='dataset', on_delete=django.db.models.deletion.CASCADE, to='api.dataset')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'training',
            },
            bases=(api.mixins.validate_model.ValidateModelMixin, models.Model),
        ),
    ]
