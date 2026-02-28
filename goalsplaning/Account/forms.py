from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


from django.contrib.auth.models import User



class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields =  fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
             'class':'form-control'
        })
        self.fields['first_name'].widget.attrs.update({
                    'class':'form-control'
                })
        self.fields['last_name'].widget.attrs.update({
             'class':'form-control'
        })
        self.fields['email'].widget.attrs.update({
             'class':'form-control'
        })
        self.fields['password1'].widget.attrs.update({
             'class':'form-control'
        })
        self.fields['password2'].widget.attrs.update({
             'class':'form-control'
        })

        for field in self.fields.values():
            field.help_text = None

class LoginForm(AuthenticationForm):
    model = User
    fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['username'].widget.attrs.update({
                'class': 'form-control'
            })

            self.fields['password'].widget.attrs.update({
                'class': 'form-control'
            })