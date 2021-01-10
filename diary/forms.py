from django import forms
from .models import bujodb

class bujoform(forms.ModelForm):

    class Meta:
        model = bujodb
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'card-text w-100 h-100 text-dark bg-light',
                'style':'border: none; resize: none;',
                
                }),
        }