from django import forms
from django.contrib.auth.models import User

from app.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'origin', 'residence',  'born', 'photo', 'latitude', 'longitude']


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm your password")

    class Meta:
        model = User
        fields = ['username', 'email','password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        #check if the passwords match
        if password and password_confirm and password_confirm != password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data
