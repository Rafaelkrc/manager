# Generated by Django 5.0.4 on 2024-06-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_user_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]
