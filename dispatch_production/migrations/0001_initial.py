# Generated by Django 5.0.4 on 2024-05-16 14:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_alter_product_production_sectors'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DispatchProduction',
            fields=[
                ('po', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('priority', models.IntegerField(unique=True)),
                ('estimated_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dispatch_product', to='products.product')),
                ('user_created', models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.PROTECT, related_name='dispatch_user', to=settings.AUTH_USER_MODEL)),
                ('user_update', models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.PROTECT, related_name='dispatch_up_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]