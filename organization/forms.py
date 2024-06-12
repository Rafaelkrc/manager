from django import forms
from . import models


class OrganizationForm(forms.ModelForm):

    class Meta:
        model = models.Organization
        fields = ['register', 'name', 'fantasy_name', 'adress', 'number_adress', 'neighbourhood', 'city', 'state', 'country', 'date_of_fundation', 'logo']
        widgets = {
            'register': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'fantasy_name': forms.TextInput(attrs={'class': 'form-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-control'}),
            'number_adress': forms.TextInput(attrs={'class': 'form-control'}),
            'neighbourhood': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'date_of_fundation': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'type': 'file', 'class': 'form-control', 'id': 'inputGroupFile02'}),
        }
