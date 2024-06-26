# Generated by Django 5.0.4 on 2024-06-13 16:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production_movements', '0002_alter_productionmovement_destynation_employee_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionmovement',
            name='user_created',
            field=models.ForeignKey(auto_created=True, blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='movement_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='productionmovement',
            name='user_update',
            field=models.ForeignKey(auto_created=True, blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='movement_up_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
