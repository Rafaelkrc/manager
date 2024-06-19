from django import forms
from . import models


class DispatchProductionForm(forms.ModelForm):

    class Meta:
        model = models.DispatchProduction
        fields = ['po', 'product', 'quantity', 'description', 'priority', 'estimated_date']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'priority': forms.TextInput(attrs={'class': 'form-control'}),
            'estimated_date': forms.DateInput(attrs={'class': 'form-control'}),
        }
