from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SingUpForm(forms.ModelForm):
    username = forms.CharField(label="Username", widget=forms.TextInput)
    email = forms.CharField(label="Email", widget=forms.EmailInput)
    first_name = forms.CharField(label="Enter your first name", widget=forms.TextInput)
    last_name = forms.CharField(label="Enter your last name", widget=forms.TextInput)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat your password", widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("Passwords don't match!")
        return data['password2']
