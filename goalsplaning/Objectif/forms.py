from django import forms

from .models import Goals




class GoalsForm(forms.ModelForm):
    class Meta:
        model = Goals
        fields = ['titre', 'description', 'date_debut', 'date_fin', 'etat']

        widgets = {
            'titre' : forms.TextInput(attrs = {'class': 'form-control'}),
            'description': forms.Textarea(attrs = {'class': 'form-control'}), 
            'date_debut': forms.DateInput(attrs = {'class': 'form-control'}),   
            'date_fin': forms.DateInput(attrs = {'class': 'form-control'}), 
            'etat':forms.Select(attrs={'class':'form-select'})       
        }



class GoalsFormetat(forms.ModelForm):
        class Meta:
             model = Goals
             fields = ['etat']

        widgets = {
             'etat': forms.Select(attrs={'class':'form-control'})
        }








