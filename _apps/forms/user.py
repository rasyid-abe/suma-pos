from django.forms import ModelForm
from django import forms
from _apps.models.user import User, Group

class FormUser(ModelForm):
    class Meta:
        model = User
        exclude = ['email', 'is_active', 'is_delete']

        widgets = {
            'name': forms.TextInput({'class':'form-control form-control-lg mb-2', 'placeholder':'Name'}),
            'username': forms.TextInput({'class':'form-control form-control-lg mb-2', 'placeholder':'Username'}),
            'password': forms.TextInput({'class':'form-control form-control-lg mb-2', 'placeholder':'Password'}),
            'email': forms.EmailInput({'class':'form-control form-control-lg mb-2', 'placeholder':'Email'}),
            'phone': forms.NumberInput({'class':'form-control form-control-lg mb-2', 'placeholder':'Phone +62'}),
            'group': forms.Select({'class':'form-control form-control-lg mb-2', 'placeholder':'Group'}),
        }

class FormGroup(ModelForm):
    class Meta:
        model = Group
        fields = ['group', 'desc']

        widgets = {
            'group': forms.TextInput({'class':'form-control form-control-lg mb-2', 'placeholder':'Group'}),
            'desc': forms.Textarea({'class':'form-control form-control-lg mb-2', 'placeholder':'Description'}),
        }
