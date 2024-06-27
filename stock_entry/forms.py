from django import forms
from . import models


class StockEntryForm(forms.ModelForm):

    class Meta:
        model = models.StockEntry
        fields = ['po', 'quantity', 'description', 'employee', 'origin_sector']
        widgets = {
            'po': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'origin_sector': forms.Select(attrs={'class': 'form-control'}),
        }
