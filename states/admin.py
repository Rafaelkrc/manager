from django.contrib import admin
from django.contrib.admin import ModelAdmin
from states.models import Country, Region, State, City


@admin.register(Country)
class CountryAdmin(ModelAdmin):
    list_display = ('name', 'abreviation')
    search_fields = ('name', 'abreviation',)


@admin.register(Region)
class RegionAdmin(ModelAdmin):
    list_display = ('name', 'abreviation')
    search_fields = ('name', 'abreviation',)


@admin.register(State)
class StateAdmin(ModelAdmin):
    list_display = ('name', 'abreviation', 'region', 'country')
    search_fields = ('name', 'abreviation', 'region', 'country',)


@admin.register(City)
class CityAdmin(ModelAdmin):
    list_display = ('name', 'state')
    search_fields = ('name', 'state',)
