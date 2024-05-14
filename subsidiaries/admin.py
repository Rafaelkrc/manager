from django.contrib import admin
from django.contrib.admin import ModelAdmin
from subsidiaries.models import Subsidiary


@admin.register(Subsidiary)
class SubsidiaryAdmin(ModelAdmin):
    list_display = ('register', 'name', 'fantasy_name', 'adress', 'number_adress', 'neighbourhood', 'city', 'state', 'country', 'email', 'date_of_fundation', 'logo')
    search_fields = ('register', 'name', 'fatasy_name',)
    ordering = ('name',)