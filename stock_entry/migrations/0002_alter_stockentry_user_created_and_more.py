# Generated by Django 5.0.4 on 2024-06-27 21:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_entry', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockentry',
            name='user_created',
            field=models.ForeignKey(auto_created=True, blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='entry_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stockentry',
            name='user_update',
            field=models.ForeignKey(auto_created=True, blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='entry_up_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
