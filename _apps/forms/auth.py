from django import forms

class AuthForm(forms.Form):
    username = forms.CharField(label="", max_length=254, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder':'Username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))
