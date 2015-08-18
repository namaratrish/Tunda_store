__author__ = 'LT10'

from django import forms
from django.core.exceptions import ValidationError
from .models import UserRegistration
from django.forms import ModelForm
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def __init__(self, data={}):
        super(UserForm, self).__init__(data=data)
        self.fields['password_again'] = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        if cleaned_data.get('password') != cleaned_data.get('password_again'):
            raise ValidationError('Password Mismatch')
        else:
            return cleaned_data

class UserRegistrationForm(ModelForm):

    city = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=50)), label="City")
    address = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=50)), label="Address")

    class Meta:
        model = UserRegistration
        fields = ['city', 'address']



