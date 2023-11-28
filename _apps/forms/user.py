from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class FormUser(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values() :
            field.widget.attrs["class"] = "form-control form-control-lg"

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        import pdb; pdb.set_trace()
        username = cleaned_data["username"]
        email = cleaned_data["email"]
        password1 = cleaned_data["password1"]
        # password2 = cleaned_data["password2"]

        if username != 'password2':
            raise forms.ValidationError({"username": "raise an error"})
        # import pdb; pdb.set_trace()

class FormGroup(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        # fields = ['group', 'desc']

        # widgets = {
        #     'group': forms.TextInput({'class':'form-control form-control-lg mb-2', 'placeholder':'Group'}),
        #     'desc': forms.Textarea({'class':'form-control form-control-lg mb-2', 'placeholder':'Description'}),
        # }
