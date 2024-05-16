from django.contrib import admin
from django.contrib.admin import ModelAdmin
from dispatch_production.models import DispatchProduction


@admin.register(DispatchProduction)
class DispatchProductionAdmin(ModelAdmin):
    list_display = ('po', 'product', 'quantity', 'description', 'priority', 'estimated_date', 'created_at', 'update_at', 'user_created', 'user_update',)
    search_fields = ('po',)
    ordering = ('po',)
