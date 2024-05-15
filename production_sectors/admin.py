from django.contrib import admin
from django.contrib.admin import ModelAdmin
from production_sectors.models import ProductionSector


@admin.register(ProductionSector)
class ProductionSectorAdmin(ModelAdmin):
    list_display = ('name', 'ordering',)
    search_fields = ('name',)
    ordering = ('ordering',)
