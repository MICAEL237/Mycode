from django import forms
from .models import Sessions



class SessionForm(forms.ModelForm):
    class Meta:
        model =Sessions 
        fields = ['tache']

        widgets = {
            'tache': forms.Select(attrs={'class': 'form-select'}),
        }


class SessionForm2(forms.ModelForm):
    class Meta:
        model =Sessions 
        fields = []
