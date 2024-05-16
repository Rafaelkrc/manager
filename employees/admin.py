from django.contrib import admin
from django.contrib.admin import ModelAdmin
from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = ('register', 'name', 'adress', 'adress_number', 'neighbourhood', 'city', 'state', 'country', 'email',)
    search_fields = ('register', 'name', 'email',)
    ordering = ('name',)
