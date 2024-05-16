from django.contrib import admin
from django.contrib.admin import ModelAdmin
from stock_entry.models import StockEntry


@admin.register(StockEntry)
class StockEntryAdmin(ModelAdmin):
    list_display = ('name', 'po', 'quantity', 'description', 'employee', 'origin_sector', 'created_at', 'update_at', 'user_created', 'user_update',)
    search_fields = ('name',)
    ordering = ('po',)
