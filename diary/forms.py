from django import forms
from .models import bujodb

class bujoform(forms.ModelForm):

    class Meta:
        model = bujodb
        fields = ('text','day')

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'card-text w-100 h-100 text-dark bg-light',
                'style':'border: none; resize: none;',
                
                }),
            'day': forms.Select(attrs={
                'class': 'text-dark bg-light',
                'style':'border: none; resize: none;',
            })
        }