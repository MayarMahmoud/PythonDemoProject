from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField,PasswordInput
from django.core.exceptions import ValidationError
from .models import user
from django import forms

class register_form(ModelForm):
    class Meta:
        model = user
        fields = '__all__'
        widgets = {
            'password': PasswordInput(attrs={'class':'form-contro', "min":"8", "max":"20", 'type':'text', 'align':'center', 'placeholder':'password'})
        }

    def __init__(self, *args, **kwargs):
        # first call the 'real' __init__()
        super(register_form, self).__init__(*args, **kwargs)
        self.fields['Password'].widget = forms.PasswordInput(attrs={'placeholder': 'password'})
        self.fields['Password'].widget.attrs['class'] = 'form-control'
        self.fields['Password'].widget.attrs['min'] = '8'
        self.fields['Password'].widget.attrs['max'] = '20'

    def clean_Password(self):
        d = self.cleaned_data['Password']
        print(d)
        if len(d) < 8:
            raise ValidationError("password should be at least 8 characters long")
        return d