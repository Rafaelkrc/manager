from django import forms
from . import models


class SubsidiaryForm(forms.ModelForm):

    class Meta:
        model = models.Subsidiary
        fields = '__all__'
        widgets = {
            'organization': forms.Select(attrs={'class': 'form-control', 'default': '1'}),
            'register': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'fantasy_name': forms.TextInput(attrs={'class': 'form-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-control'}),
            'number_adress': forms.TextInput(attrs={'class': 'form-control'}),
            'neighbourhood': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_fundation': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
        }
