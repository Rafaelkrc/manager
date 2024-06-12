from django import forms
from . import models


class CityForm(forms.ModelForm):

    class Meta:
        model = models.City
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'estate': forms.Select(attrs={'class': 'form-control'}),
        }


class StateForm(forms.ModelForm):

    class Meta:
        model = models.State
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'abbreviation': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
        }


class CountryForm(forms.ModelForm):

    class Meta:
        model = models.Country
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'abbreviation': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RegionForm(forms.ModelForm):

    class Meta:
        model = models.Region
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'abbreviation': forms.TextInput(attrs={'class': 'form-control'}),
        }
