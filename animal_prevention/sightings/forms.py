from django import forms
from .models import Sighting

class SightingForm(forms.ModelForm):
    class Meta:
        model = Sighting
        fields = ['cep', 'animal_type', 'date', 'action_taken']
        widgets = {
            'action_taken': forms.Textarea(attrs={'rows': 4}),
        }
