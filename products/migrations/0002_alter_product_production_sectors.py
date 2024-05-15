# Generated by Django 5.0.4 on 2024-05-15 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production_sectors', '0002_alter_productionsector_type'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='production_sectors',
            field=models.ManyToManyField(related_name='product_sector', to='production_sectors.productionsector'),
        ),
    ]