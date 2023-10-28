from django.forms import ModelForm
from django import forms
from _apps.models.user import User

class FormUser(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        widgets = {
            'username': forms.TextInput({'class':'form-control', 'onfocus':'focused(this)', 'onfocusout':'defocused(this)'}),
            'password': forms.PasswordInput({'class':'form-control', 'onfocus':'focused(this)', 'onfocusout':'defocused(this)'}),
            'email': forms.EmailInput({'class':'form-control', 'onfocus':'focused(this)', 'onfocusout':'defocused(this)'}),
        }
