from django.contrib import admin
from django.contrib.admin import ModelAdmin
from production_movements.models import ProductionMovement


@admin.register(ProductionMovement)
class ProductionMovementAdmin(ModelAdmin):
    list_display = ('po', 'quantity', 'description', 'employee', 'origin_sector', 'priority', 'destynation_sector', 'destynation_employee', 'created_at', 'update_at', 'user_created', 'user_update',)
    ordering = ('po',)
