from django import forms
from . import models


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = models.Employee
        fields = ['register', 'name', 'adress', 'adress_number', 'neighbourhood', 'city', 'state', 'country', 'email', 'production_sector']
        widgets = {
            'register': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-control'}),
            'adress_number': forms.TextInput(attrs={'class': 'form-control'}),
            'neighbourhood': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'production_sector': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
