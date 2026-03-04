from django import forms
from .models import Tasks
from Objectif.models import Goals




class TasKForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields= '__all__'
        widgets = {
            'titre': forms.TextInput(attrs={'class':'form-control'}),
            'date_debut': forms.DateInput(attrs={'class':'form-control'}),
            'date_fin': forms.DateInput(attrs={'class':'form-control'}),
            'objectif': forms.Select(attrs={'class':'form-select'}),
            'status': forms.Select(attrs={'class':'form-select'})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['objectif'].queryset = Goals.objects.filter(user=user)
    
    

class TaskFormeStatus(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['status']
    
        widgets = {
            'status': forms.Select(attrs={'class':'form-select'})

        }