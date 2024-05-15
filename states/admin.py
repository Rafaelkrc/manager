from django.contrib import admin
from django.contrib.admin import ModelAdmin
from states.models import Country, Region, State, City


@admin.register(Country)
class CountryAdmin(ModelAdmin):
    list_display = ('name', 'abbreviation')
    search_fields = ('name', 'abbreviation',)


@admin.register(Region)
class RegionAdmin(ModelAdmin):
    list_display = ('name', 'abbreviation')
    search_fields = ('name', 'abbreviation',)


@admin.register(State)
class StateAdmin(ModelAdmin):
    list_display = ('name', 'abbreviation', 'region', 'country')
    search_fields = ('name', 'abbreviation', 'region', 'country',)


@admin.register(City)
class CityAdmin(ModelAdmin):
    list_display = ('name', 'state')
    search_fields = ('name', 'state',)
