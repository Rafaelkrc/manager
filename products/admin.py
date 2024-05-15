from django.contrib import admin
from django.contrib.admin import ModelAdmin
from products.models import Product


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('code', 'name', 'group', 'brand', 'cost_price', 'selling_price', 'unit_measure', 'quantity', 'production_time', 'average_production_time', 'created_at', 'update_at', 'user_created', 'user_update',)
    search_fields = ('code', 'name',)
    ordering = ('code', 'name',)
