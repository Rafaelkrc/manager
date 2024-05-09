from django.contrib import admin
from django.contrib.admin import ModelAdmin
from organization.models import Organization


@admin.register(Organization)
class OrganizationAdmin(ModelAdmin):
    list_display = ('register', 'name', 'fantasy_name', 'adress', 'number_adress', 'neighbourhood', 'city', 'state', 'country', 'date_of_fundation', 'logo')
    search_fields = ('register', 'name', 'fatasy_name',)
