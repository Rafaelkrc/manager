from django.contrib import admin
from django.contrib.admin import ModelAdmin
from product_caracteristics.models import Group, Brand, UnitMeasure


@admin.register(Group)
class GroupAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Brand)
class BrandAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(UnitMeasure)
class unitMeasureAdmin(ModelAdmin):
    list_display = ('name', 'abreviation',)
    search_fields = ('name', 'abreviation',)
    ordering = ('name',)
