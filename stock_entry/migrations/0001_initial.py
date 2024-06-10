# Generated by Django 5.0.4 on 2024-05-16 16:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
        ('production_movements', '0002_alter_productionmovement_destynation_employee_and_more'),
        ('production_sectors', '0002_alter_productionsector_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StockEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Stock Entry')),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='entry_employee', to='employees.employee')),
                ('origin_sector', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='entry_orig_sector', to='production_sectors.productionsector')),
                ('po', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='entry_movement', to='production_movements.productionmovement')),
                ('user_created', models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.PROTECT, related_name='entry_user', to=settings.AUTH_USER_MODEL)),
                ('user_update', models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.PROTECT, related_name='entry_up_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]