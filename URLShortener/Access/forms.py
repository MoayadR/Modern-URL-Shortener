from django.forms import ModelForm 
from django.contrib.auth.models import User
from django import forms

class UserSignUpForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required= True
    class Meta:
        model = User
        fields = ['username' , 'first_name' , 'last_name' , 'email' , 'password',]
        widgets = {
            'password' : forms.PasswordInput(),
        }